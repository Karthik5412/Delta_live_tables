import dlt 

# Creating streaming table

@dlt.table(name='str_tab')
def str_tab() :
    df = spark.readStream.table('dlt_practice.source.orders')

    return df

# Creating Mat view

@dlt.table(name='mat_view')
def mat_view() :
    df = spark.read.table('dlt_practice.source.orders')

    return df


# Creating Streaming View 

@dlt.view(name='str_view')
def str_view() :
    df = spark.readStream.table('dlt_practice.source.orders')

    return df

# Creating Batch view 

@dlt.table(name='bat_view')
def bat_view() :
    df = spark.read.table('dlt_practice.source.orders')

    return df

