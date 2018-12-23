#get instance ids of all ec2 instance in running  state
import boto3
client = boto3.client('ec2','us-east-2')
resp = client.describe_instances()
Filters =  [
              {
                  'Name': 'instance-state-name',
                  'Values': ['running']


              },
        ],
for reservation in resp['Reservations']:
    for instance in reservation["Instances"]:
       instance_id = instance['InstanceId']
       print(f'Instance id is {instance_id} ')
       #  assingment take this code fillter based on availability zone