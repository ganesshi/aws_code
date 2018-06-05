#iam code 
import boto3

iam = boto3.client('ec2')
for i in range(1,10):
	iam.create_user(UserName='User'+str(i))
	print ("User "+'User'+str(i)+" created successfully.")

for i in iam.list_users()['Users']:
	print (i['UserName'])

group_name = iam.create_group(GroupName='Users')['Group']['GroupName']
for i in iam.list_users()['Users']:
	iam.add_user_to_group(UserName=i['UserName'],GroupName=group_name)
	print("added user "+i['UserName'] + "to group "+ group_name + " successfully.")

