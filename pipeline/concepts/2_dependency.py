import dlt 

# Creating streaming table

@dlt.table(name='dep_1')
def dep_1() :
    df = spark.readStream.table('orders')

    return df