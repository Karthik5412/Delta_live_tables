import dlt 
from pyspark.sql.functions import *
from pyspark.sql.types import * 


# Creating a Streaming View
@dlt.view(name='customers_slv_view')
def customers_slv_view() :
    df = spark.readStream.table('customers_brz')

    df = df.withColumn('customer_name', upper(col('customer_name'))) 

    return df 

# Creating Streaming Table
dlt.create_streaming_table(name = 'customers_slv')


# Creating Auto CDC 

dlt.create_auto_cdc_flow(
source='customers_slv_view',
target='customers_slv',
keys= ['customer_id'],
sequence_by= 'last_updated',
stored_as_scd_type= 1
)

