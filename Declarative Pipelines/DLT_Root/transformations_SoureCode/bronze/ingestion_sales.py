import dlt 

sales_expectations={
    "rule1":"sales_id IS NOT NULL"
}

#Empty streaming table
dlt.create_streaming_table(name="sales_stg",
                           expect_all_or_drop=sales_expectations,
                           comment="Appending sales data from east and west regions")


#creating East Sales Flow
@dlt.append_flow(target="sales_stg")
def east_sales():
    df=spark.readStream.table("dltravi.source.sales_east") 
    return df 


#creating West Sales Flow

@dlt.append_flow(target="sales_stg")
def west_sales():
    return spark.readStream.table("dltravi.source.sales_west")
     
   
