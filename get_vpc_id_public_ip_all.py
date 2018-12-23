# GET VPC ID AND public ip for all ec2
import boto3
client = boto3.client('ec2','us-east-2')
resp = client.describe_instances()
for reservation in resp['Reservations']:
    for instance in reservation["Instances"]:
        vpc_id = instance['VpcId']
        print(f'vpc is is { vpc_id}')
        #ckeck if key 'publicIpAdderss' exits in direct before accessing it
        if 'PublicIpAddress' in instance:
            public_ip = instance['PublicIpAddress']
            print(f'public IP is {public_ip}')
        else:
            print('public IP not found')