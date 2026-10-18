import dlt 

# Creating Streaming Table for Customers

dlt.create_streaming_table(name='fact_sales')

# Creating auto_cdc_flow for scd 2

dlt.create_auto_cdc_flow(
    target= 'fact_sales',
    source='sales_slv_view',
    keys= ['sales_id'],
    sequence_by= 'sale_timestamp',
    stored_as_scd_type= 2
)



