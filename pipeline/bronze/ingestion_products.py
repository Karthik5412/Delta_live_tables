import dlt 

# Expectations 

rules = {
    'rule_1' : 'product_id IS NOT NULL',
    'rule_2' : 'category IS NOT NULL'
}


# Creating Streaming Table

@dlt.table(name='products_brz')
@dlt.expect_all_or_drop(rules)
def products_brz() :
    df = spark.readStream.table('products')

    return df 







