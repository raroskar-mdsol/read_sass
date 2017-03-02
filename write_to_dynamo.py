from db_utils import DynamoDbOperations
metadata_table_name = 'metadata'
data_table_name = 'data'
db = DynamoDbOperations()
# Create table metadata
# db.create_table(metadata_table_name,
#   [
#     {
#       'AttributeName': 'study_uuid',
#       'KeyType': 'HASH'
#     },
#     {
#       'AttributeName': 'dataset_uuid',
#       'KeyType': 'RANGE'
#     }
#   ],
#   [
#     {
#       'AttributeName': 'study_uuid',
#       'AttributeType': 'S'
#     },
#     {
#       'AttributeName': 'dataset_uuid',
#       'AttributeType': 'S'
#     }
#   ],
#   {
#     'ReadCapacityUnits': 5,
#     'WriteCapacityUnits': 5
#   }
# )

# Create table data
# db.create_table(data_table_name,
#   [
#     {
#       'AttributeName': 'study_uuid',
#       'KeyType': 'HASH'
#     },
#     {
#       'AttributeName': 'dataset_uuid',
#       'KeyType': 'RANGE'
#     }
#   ],
#   [
#     {
#       'AttributeName': 'study_uuid',
#       'AttributeType': 'S'
#     },
#     {
#       'AttributeName': 'dataset_uuid',
#       'AttributeType': 'S'
#     }
#   ],
#   {
#     'ReadCapacityUnits': 5,
#     'WriteCapacityUnits': 5
#   }
# )


# Insert data from sas7bdat files to metdata table
import os
import sas_reader
data = {}
data["datasets"] = []
#rootdir = '/Users/raroskar/Downloads/sample_docs/'

rootdir = raw_input("Please enter absolute path for folder containing .sas7bdat files: ")

for filename in os.listdir(rootdir):
    if filename.endswith(".sas7bdat"):
      print os.path.join(rootdir, filename)
      metadata, data = sas_reader.get_dataset_metadata(os.path.join(rootdir, filename), 'my_sample_study_1')
      # db.add_item(metadata_table_name, metadata)
      for obj in data:
          db.add_item(data_table_name, obj)

# Print list of tables in db and item count for metadata table
db.print_all_table_names()
db.print_item_count(metadata_table_name)
db.print_item_count(data_table_name)