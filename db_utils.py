import boto3

class DynamoDbOperations:
  def __init__(self):
    print "init"
    self.dynamodb = boto3.resource('dynamodb',
    aws_access_key_id="anything",
    aws_secret_access_key="anything",
    endpoint_url='http://localhost:8000',region_name='us-west-2')

  def create_table(self, table_name, key_schema, attribute_definitions, provisioned_throughput):
    table = self.dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput=provisioned_throughput
    )
    # table.meta.client.get_waiver('table_exists').wait(TableName=table_name)

  def add_item(self, table_name, item):
    table = self.dynamodb.Table(table_name)
    table.put_item(
      Item=item
    )

  def print_item_count(self, table_name):
    table = self.dynamodb.Table(table_name)
    print("Table item count for = ", table_name , " = " , table.item_count)

  def print_all_table_names(self):
    print("Tables in Local DynamoDb = ", list(self.dynamodb.tables.all()))