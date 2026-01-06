import dlt

#product expectations
customer_expectations={
    "rule1":"customer_id IS NOT NULL",
    "rule2":"region IS NOT NULL"
}

# Ingestion Products 

@dlt.table(name="customer_stg")
@dlt.expect_all_or_drop(customer_expectations)
def customer_stg():
    df=spark.readStream.table("dltravi.source.customers")
    return df