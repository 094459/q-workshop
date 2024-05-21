# Create a simple Python class that uloads a file to S3
import boto3
from botocore.exceptions import ClientError

class S3Uploader:
    def __init__(self, bucket_name, file_name, file_path):
        self.bucket_name = bucket_name
        self.file_name = file_name
        self.file_path = file_path
        self.s3 = boto3.client('s3')

    def upload_file(self):
        try:
            self.s3.upload_file(self.file_path, self.bucket_name, self.file_name)
            print(f"File {self.file_name} uploaded to S3 bucket {self.bucket_name}")
        except ClientError as e:
            print(f"Error uploading file: {e}")
            
