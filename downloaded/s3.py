import os

os.system('pip install sagemaker')


# Define IAM role
import boto3
import re
import sagemaker
from sagemaker import get_execution_role

role = get_execution_role()
region=us-east-2
sess = sagemaker.Session()

s3 = boto3.resources('s3', region_name = 'us-east-1')



#region_name = self.boto_session.region_name
#boto3.Session().resource('s3', region_name=region).Bucket('chicken-nuggets {}'.format(region))

bucket = 'chicken-nuggets'
prefix = 'data'

#my_bucket = 's3://{}/{}'.format(bucket, prefix)

#data = s3://chicken-nuggets/data/

data = s3.Bucket('chicken-nuggets/data')
print(data)