import boto3
client = boto3.client('ec2')
resp = client.describe_instances(InstanceIds=['i-0eb79bfbd7fdaf3cb'])

vpc_id = resp['Reservations'][0]['Instances'][0]['VpcId']
public_ip = resp['Reservations'][0]['Instances'][0]['PublicIpAddress']
print(vpc_id)
print(public_ip)