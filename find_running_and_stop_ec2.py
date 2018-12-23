# all running instances are going to be stop
import boto3
client = boto3.client('ec2','us-east-2')
resp = client.describe_instances()
Filters =  [
              {
                  'Name': 'instance-state-name',
                  'Values': ['running']


              },
        ],
instance_ids = list()
for reservation in resp['Reservations']:
    for instance in reservation["Instances"]:
       instance_id = instance['InstanceId']
       instance_ids.append(instance_id)
       print(f'Instance id is {instance_id} ')
if len(instance_ids):
    client.stop_instances(
           InstanceIds = instance_ids
       )

# task: get all running ec2 instances in a default vpc