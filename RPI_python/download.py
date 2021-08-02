import logging
import boto3
from botocore.exceptions import ClientError
from secret import access_key, secret_access_key
from boto3.session import Session

client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)
bucket = 'projectyazan'
client.download_file(bucket,'project/threshold.txt', 'threshold.txt')
print("done downloading configration values" + "\n")
