import boto3
import os
from datetime import datetime

def upload_to_s3(file_path, bucket_name):
    s3_resource = boto3.resource('s3')
    date = str(datetime.today().strftime('%Y-%m-%d(%H:%M:%S)'))
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    s3_object_key = f'{file_name}_{target_date}{file_extension}'
    s3.upload_file(file_path, bucket_name, s3_object_key)
    print(f'Succefully uploaded {file_path} to {bucket_name}/{s3_object_key}')

upload_to_s3(f'{date}-command_id_output.txt', "ad-user-cutoff-update")
