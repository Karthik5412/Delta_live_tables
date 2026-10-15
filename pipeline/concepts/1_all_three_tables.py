import dlt 

# Creating streaming table

@dlt.table(name='str_tab')
def str_tab() :
    df = spark.readStream.table('dlt_practice.source.orders')

    return df

