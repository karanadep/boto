from boto.s3.connection import S3Connection
from boto.s3.key import Key

#aws_key 		= "<aws_key>"
#secret_key 	= "<secret_key>"

s3_connection  = S3Connection(aws_key,secret_key)

#get buckets
'''
source_bucket  = s3_connection.get_bucket("karan-input")
target_bucket  = s3_connection.get_bucket("karan-output-one")
reject_bucket  = s3_connection.get_bucket("karan-output-two")
'''

#list objects in bucket
#for key in source_bucket.list():
#	print(key.name)

#delete keys in bucket
#for key in target_bucket.list():
#	key.delete()
	
#delete bucket
#s3_connection.delete_bucket("karan-output-one")

#create bucket
#s3_connection.create_bucket("karan-output-one")

#upload local files to S3	
'''
testfile	= "readme.txt"
k 			= Key(target_bucket)
k.key 		= 'readme.txt'
k.set_contents_from_filename(testfile)
'''

#copy between buckets
'''
for k in source_bucket.list():
	#copy from source to destination
	target_bucket.copy_key(k.name,source_bucket.name,k.name)
'''