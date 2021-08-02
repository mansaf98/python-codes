import logging
import boto3
from botocore.exceptions import ClientError
from secret import access_key, secret_access_key
from boto3.session import Session
client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)
bucket = 'projectyazan'
client.upload_file("output.txt", bucket, 'project/output.txt')
print("done uploading output values" + "\n")
client.upload_file("test.jpg", bucket, 'project/detection.jpg')
print("done uploading capture" + "\n")