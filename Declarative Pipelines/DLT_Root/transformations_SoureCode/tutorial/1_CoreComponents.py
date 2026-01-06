# import dlt

# #creating streaming table 

# @dlt.table(
#     name="first_streaming_table"
# )

# def first_streaming_table():
#     df=spark.readStream.table("dltravi.source.orders")
#     return df


# # Creating materialized views

# @dlt.table(
#     name="first_mat_view"
# )
# def first_mat_view():

#     df=spark.read.table("dltravi.source.orders")
#     return df 

# #creating batch view 

# @dlt.view(
#     name="first_batch_view"
# )

# def first_batch_view():
#     df=spark.read.table("dltravi.source.orders")
#     return df

# #creating streaming view

# @dlt.view(
#     name="first_stream_view"
# )

# def first_stream_view():
#     df=spark.readStream.table("dltravi.source.orders")
#     return df
