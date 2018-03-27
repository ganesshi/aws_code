#iam code 
import boto3

iam = boto3.client('iam')
for i in range(1,10):
	iam.create_user(UserName='User'+str(i))
	print ("User "+'User'+str(i)+" created successfully.")

for i in iam.list_users()['Users']:
	print (i['UserName'])
