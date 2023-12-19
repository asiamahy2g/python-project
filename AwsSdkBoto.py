import boto3

region="us-east-1"
_ec = boto3.client('ec2',region_name=region)

def listInstances():
    try:
        list_of_instances=[]
        instances= _ec.describe_instances()
        for item in instances['Reservations']:
            for instance in item['Instances']:
                list_of_instances.append(instance['InstanceId'])
        return list_of_instances
    except Exception as e:
        print(e)

def StopInstances(Instance_list):
    try: 
         _ec.stop_instances(InstanceIds=Instance_list) 
    except Exception as e:
        print(e)
        
def StartInstances(Instance_list):
    _ec.start_instances(InstanceIds=Instance_list)
    

          