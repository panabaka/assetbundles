# import dlt
# from pyspark.sql.functions import upper

# #creating a end-end basic pipeline

# # Staging Area

# @dlt.table(
#     name="staging_orders"
# )

# def staging_orders():
#     df=spark.readStream.table("dltravi.source.orders")
#     return df


# #Crearing view
# @dlt.view(
#     name="transformed_orders"
# )
# def transformed_orders():
#     df=spark.readStream.table("staging_orders")
#     df=df.withColumn("order_status",upper(df.order_status))
#     return df 


# #creating aggreated table
# @dlt.table(
#     name="aggregated_orders"
# )

# def aggregated_orders():
#     df=spark.readStream.table("transformed_orders")
#     df=df.groupBy("order_status").count()
#     return df

    
    