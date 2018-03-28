#date, 28/03/2018
import boto3

ec2 = boto3.client('ec2')

print (ec2.describe_vpcs()['Vpcs'][0]['VpcId'])
print (ec2.describe_vpcs()['Vpcs'][1]['VpcId'])
print (ec2.describe_vpcs()['Vpcs'][2]['VpcId'])
