import boto3
from datetime import datetime

def upload_file_to_s3(file_path, bucket_name):
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Extract file name and extension
    file_name, file_extension = file_path.split('.')

    # Create a new file name with timestamp
    new_file_name = f"{file_name}_{timestamp}.{file_extension}"

    # Create an S3 client
    s3 = boto3.client('s3')

    try:
        # Upload the file with the new name to S3
        s3.upload_file(file_path, bucket_name, new_file_name)

        print(f"File uploaded successfully with timestamp: {timestamp}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")

if __name__ == "__main__":
    # Replace 'your_bucket_name' with your actual S3 bucket name
    bucket_name = "ad-user-cutoff-update"

    # Replace 'logs.txt' with your actual file path
    file_path = "command_id_output.txt"

    upload_file_to_s3(file_path, bucket_name)

