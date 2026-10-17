import dlt 
from pyspark.sql.functions import *
from pyspark.sql.types import * 


# Creating a Streaming View
@dlt.view(name='products_slv_view')
def sales_slv_view() :
    df = spark.readStream.table('products_brz')

    df = df.withColumn('price', col('price').cast(IntegerType())) 

    return df 

# Creating Streaming Table
dlt.create_streaming_table(name = 'products_slv')


# Creating Auto CDC 

dlt.create_auto_cdc_flow(
source='products_slv_view',
target='products_slv',
keys= ['product_id'],
sequence_by= 'last_updated',
stored_as_scd_type= 1
)

