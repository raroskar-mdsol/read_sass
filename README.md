This is private repo for dumping python code to use sas files and create json or write to local dynamo db
Please refer [here](https://docs.google.com/document/d/1nlIk2q8SURTlDmmLUXyDIXV-obRj2E6VuK6W96eM-Z0/edit#heading=h.q7uu4xu75ft6)
for table structure in dynamodb.


Need to download the .sas7bdat files and store in a folder.
use python write_to_json_files.py to dump that data in json files metadata.json and data.json
use python write_to_dynamo.py to create tables metadata and data in local dynamodb and add some data
Please check [local dynamodb setup](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html)
