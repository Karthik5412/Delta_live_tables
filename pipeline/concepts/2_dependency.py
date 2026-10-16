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





