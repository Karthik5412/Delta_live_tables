import dlt 
from pyspark.sql.functions import *


# Creating a Streaming View
@dlt.view(name='sales_slv_view')
def sales_slv_view() :
    df = spark.readStream.table('sales_brz')

    df = df.withColumn('amount_per_unit', col('amount')/col('quantity')) 

    return df 

#Creating Streaming Table
# dlt.create

