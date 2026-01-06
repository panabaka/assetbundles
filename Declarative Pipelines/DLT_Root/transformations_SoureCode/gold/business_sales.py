import dlt
from pyspark.sql.functions import sum

@dlt.table(
    name="business_sales"
)
def business_sales():
    df_fact = spark.read.table("fact_sales")
    df_dim_cust = spark.read.table("dim_customers")
    df_dim_prod = spark.read.table("dim_product")

    df_join = df_fact.join(df_dim_cust, "customer_id", "inner") \
                     .join(df_dim_prod, "product_id", "inner")

    df_prun = df_join.select("region", "category", "total_amount")

    df_agg = df_prun.groupBy(
        "region",
        "category"
    ).agg(
        sum("total_amount").cast("double").alias("total_sales")
    )
    return df_agg
# Error fixed: join keys simplified, sum cast to double