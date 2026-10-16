import dlt 
import pyspark.sql.functions as f 

# Creating streaming table

@dlt.table(name='dep_1')
def dep_1() :
    df = spark.readStream.table('orders')

    return df


@dlt.table(name='dep_2') 
def dep_2():
    df = spark.read.table('dep_1')

    df_low = df.withColumn('status', f.lower(f.col('status'))) 
    df_low = df.withColumn('dim_key', f.monotonically_increasing_id()+f.lit(1))

    return df_low

@dlt.table(name='agg_dep')
def agg_dep() :
    df = spark.readStream.table('dep_2')

    df_agg = df.groupby(f.col('status'),f.col('order_date')).agg(
        f.sum(f.col('total_amount')).alias('total_cost'),
        f.avg(f.col('total_amount')).alias('avg_cost') 
    )

    return df_agg 





