import dlt

#product expectations
product_expectations={
    "rule1":"product_id IS NOT NULL",
    "rule2":"price>=0"
}

# Ingestion Products 

@dlt.table(name="product_stg")
@dlt.expect_all_or_drop(product_expectations)
def product_stg():
    df=spark.readStream.table("dltravi.source.products")
    return df
