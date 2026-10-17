import dlt 

# Expectations 

rules = {
    'rule_1' : 'customer_name IS NOT NULL',
    'rule_2' : 'region IS NOT NULL'
}


# Creating Streaming Table

@dlt.table(name='customers_brz')
@dlt.expect_all_or_drop(rules)
def customer_brz() :
    df = spark.readStream.table('customers')

    return df 
















