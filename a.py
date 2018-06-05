
import boto3
s3 = boto3.resource('s3')
for i in s3.buckets.all():
	print(i.name)

#-------
s3 = boto3.client('s3')
print ("--------Using client methodds---------")
print("Bucket List in AWS account: ",)
# for i in s3.list_buckets()['Buckets']:
# 	print(i['Name'])
# 	if i['Name'].startswith("ganesshi"):
# 		change_bucket_versioning = s3.put_bucket_versioning(Bucket=i['Name'], VersioningConfiguration={'MFADelete':'Disabled','Status':'Suspended'})
# 		s3.delete_bucket(Bucket=i['Name'])

# print ("Creating New buckets: ")
# for new_bucket in range(1,10):
# 	bucket_location = s3.create_bucket(ACL='public-read-write',Bucket='ganesshi-druva-1511-' + str(new_bucket), CreateBucketConfiguration={'LocationConstraint':'us-west-1'})
# 	print(bucket_location)
# object1 = s3.get_object(Bucket='ganesshi8087-1', Key='file_lock.py')
# print("get object method returns :", )
# print(object1)

upload_response = s3.put_object(Key='Resume_KP', Bucket='druva-1511', \
								Body='/home/ganesh/Downloads/Kaiwalya _Pethe_CV.docx')
print (upload_response)

download_response = s3.get_object(Key='Resume_KP', Bucket='druva-1511')
print (download_response)

print ("--------------")
bucket_versioning = s3.get_bucket_versioning(Bucket='druva-1511')
print (bucket_versioning['Status'])

bucket_tag = s3.get_bucket_tagging(Bucket='druva-1511')
print (bucket_tag)
print ("Delete bucket tagging")
delete_tag = s3.delete_bucket_tagging(Bucket='druva-1511')

object1 = s3.get_object(Bucket='druva-1511', Key='07.log')
print (object1)

#To change the versioning state, first delete the replication configuration.
replication_status = s3.get_bucket_replication(Bucket='druva-1511')
print ("------------Replication Status for bucket druva-1511------")
print (replication_status)
if replication_status['ReplicationConfiguration']['Rules'][0]['Status'] == 'Enabled':
	delete_replication = s3.delete_bucket_replication(Bucket='druva-1511')

bucket_versioning = s3.get_bucket_versioning(Bucket='druva-1511')
print (bucket_versioning['Status'])
if bucket_versioning['Status'] == 'Enabled':
	change_bucket_versioning = s3.put_bucket_versioning(Bucket='druva-1511', VersioningConfiguration={'MFADelete':'Disabled','Status':'Suspended'})
	print (change_bucket_versioning)

print ("---------------------------")


if __name__ == '__main__':
	None


