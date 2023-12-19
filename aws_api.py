import boto3
from pprint import pprint

s3_instance = boto3.client('s3')
buckets = s3_instance.list_buckets()
pprint(buckets)

iam_instance = boto3.client('iam')
users = iam_instance.list_users()

"""for user in users['Users']:
    print(user['UserName'])
    print(user['CreateDate'])
    """




