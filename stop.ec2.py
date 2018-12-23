import boto3
client = boto3.client('ec2')
client.start_instances(InstanceIds = ['i-02e09642f07d6e081'])