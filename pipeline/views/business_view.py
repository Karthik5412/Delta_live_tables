import dlt
from pyspark.sql.functions import *

# Creating a Mat view for Business View

@dlt.table(name='bussiness_mat_view') 
def bussiness_mat_view() :
    df_cust = spark.sql('select customer_id, region from dim_customers')
    df_pro = spark.sql('select product_id, category from dim_products')
    df_sales = spark.sql('select customer_id as fact_cust_id, product_id as fact_pro_id, region, amount from fact_sales')

    df_cust = df_cust.withColumnRenamed('region','cust_region')
    df_sales = df_sales.withColumnRenamed('region','sale_region')


    df_join = df_sales.join(df_cust, df_sales['fact_cust_id'] == df_cust['customer_id'], how='inner').join(df_pro,df_sales['fact_pro_id'] == df_pro['product_id'], how= 'inner') 

    df_want = df_join.select('cust_region','sale_region','category','amount')

    df_agg = df_want.groupby('cust_region','sale_region','category').agg(sum('amount').alias('total_sales'))

    return df_agg
