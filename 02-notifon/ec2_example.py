# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key_windows'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.meterial
key.material
key.key_material
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', '02-notifon')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('ls', '')
key.key_material
key_path
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '-l')
get_ipython().run_line_magic('ls', '')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l python_automation_key_windows.pem')
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.Image('ami-035b3c7efe6d061d5')
img.name
ami_name = 'amzn-ami-hvm-2018.03.0.20190611-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
ec2.Instance(id='i-036db1d1b3bd99168')
inst = instances[0]
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups
security_group = ec2.create_security_group(
    Description='python automation ec2 sg',
    GroupName='pythonAutomationSG',
    VpcId='vpc-9a10b9e0',
    DryRun=True
)
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId])
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '155.201.42.17'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '155.201.42.17/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
inst.public_dns_name
get_ipython().run_line_magic('history', '')
