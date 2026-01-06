import dlt 
from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

#Transform sales_data
@dlt.view(
    name="customers_enr_view"
)
def customers_enr_view():
    df=spark.readStream.table("customer_stg")
    df=df.withColumn("customer_name",upper(col("customer_name")))
    df=df.withColumn("last_updated",current_timestamp())
    return df


#Creating Destination Silver
dlt.create_streaming_table(
    name="customers_enr"
)
dp.create_auto_cdc_flow(
  target = "customers_enr",
  source = "customers_enr_view",
  keys = ["customer_id"],
  sequence_by = "last_updated",
  ignore_null_updates = False,
  apply_as_deletes = None,
  apply_as_truncates = None,
  column_list = None,
  except_column_list = None,
  stored_as_scd_type = 1,
  track_history_column_list = None,
  track_history_except_column_list = None,
  name = None,
)