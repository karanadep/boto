from boto.ec2 import EC2Connection

aws_key 		= "<aws_key>"
secret_key 		= "<secret_key>"

# connects to default region
ec2_connection = EC2Connection(aws_key, secret_key)

# to connect to different region
#conn = boto.ec2.connect_to_region("us-west-1")

#launch instance
#ec2_connection.run_instances('ami-6869aa05', instance_type='m3.large')

#list instances

reservations = ec2_connection.get_all_instances()
for r in reservations:
	for i in r.instances:
		print(r.id, i.id, i.state)

		
#start instance

#stop instance

#terminate instance
#reservations = ec2_connection.get_all_instances(instance_ids=['i-f72b4ac6'])
#reservations[0].instances[0].terminate()