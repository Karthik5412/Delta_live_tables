import dlt 
from pyspark.sql.functions import *


# Creating a Streaming View
@dlt.view(name='sales_slv_view')
def sales_slv_view() :
    df = spark.readStream.table('sales_brz')

    df = df.withColumn('amount_per_unit', col('amount')/col('quantity')) 

    return df 

# Creating Streaming Table
dlt.create_streaming_table(name = 'sales_slv')


# Creating Auto CDC 

dlt.create_auto_cdc_flow(
source='sales_slv_view',
target='sales_slv',
keys= ['sales_id'],
sequence_by= 'sale_timestamp',
stored_as_scd_type= 1
)

