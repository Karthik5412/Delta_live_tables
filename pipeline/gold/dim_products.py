import dlt 

# Creating Streaming Table for Customers

dlt.create_streaming_table(name='dim_products')

# Creating auto_cdc_flow for scd 2

dlt.create_auto_cdc_flow(
    target= 'dim_products',
    source='products_slv_view',
    keys= ['product_id'],
    sequence_by= 'last_updated',
    stored_as_scd_type= 2
)



