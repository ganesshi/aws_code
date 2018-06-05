
import boto3
import time

dynamodb = boto3.client('dynamodb')

dynamodb.create_table(TableName='stars',AttributeDefinitions=[{'AttributeName':'FirstName','AttributeType':'S'}],\
					  KeySchema=[{'AttributeName':'FirstName','KeyType':'HASH'}],\
					  ProvisionedThroughput={'ReadCapacityUnits':2,'WriteCapacityUnits':2})
time.sleep(50)
# for i in dynamodb.list_tables()['TableName']:
# 	backup = dynamodb.create_backup(TableName=i,BackupName=i+"-backup")

dynamodb.put_item(TableName='stars',Item={'string':{'FirstName':'Chris'}})