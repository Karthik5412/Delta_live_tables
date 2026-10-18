import dlt 

# Creating Streaming Table for Customers

dlt.create_streaming_table(name='dim_customers')

# Creating auto_cdc_flow for scd 2

dlt.create_auto_cdc_flow(
    target= 'dim_customers',
    source='customers_slv_view',
    keys= ['customer_id'],
    sequence_by= 'last_updated',
    stored_as_scd_type= 2
)



