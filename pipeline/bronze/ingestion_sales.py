import dlt
from pyspark.sql.functions import * 

# Expectations 

rules = {
    'rule_1' : 'sales_id IS NOT NULL',
    'rule_2' : 'customer_id IS NOT NULL'
}

# Creating an empty stream table

dlt.create_streaming_table(name='sales_brz', expect_all_or_drop=rules )

# East region table

@dlt.append_flow(target='sales_brz')
def east() :
    df = spark.readStream.table('sales_east')

    df_reg = df.withColumn('region', lit('east'))

    return df_reg

    
# West region table

@dlt.append_flow(target='sales_brz')
def west() :
    df = spark.readStream.table('sales_west')

    df_reg = df.withColumn('region', lit('west'))

    return df_reg

