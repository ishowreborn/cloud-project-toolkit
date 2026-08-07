# import boto3 #here we called boto3
# # print("connecting to AWS....")

# s3=boto3.client("s3")  #learn the client 
# print("connected successfully")
# response = s3.list_buckets() # AWS sends the response back
# print(response)
# print(response["Buckets"])
# for bucket in response["Buckets"]:
#     print(bucket["Name"])
# s3.upload_file(
#     "aws_test.txt",
#     "ratnesh-s3-sqs-lambda-project-1",
#     "aws_test.txt"
# )
# print("file uploaded successfully")
# import boto3
# Imports the boto3 AWS SDK into Python.
# s3 = boto3.client("s3")
# Creates an S3 client through which Python can communicate with Amazon S3.
# response = s3.list_buckets()
# Calls the S3 list_buckets API operation and stores AWS's response in response.
# response["Buckets"]
# Accesses the Buckets value from the response dictionary.
# for bucket in response["Buckets"]:
# Loops through each bucket in the bucket list.
# bucket["Name"]
# Accesses the name of the current bucket.
# print(bucket["Name"])
# Displays the current bucket's name.


# 📒 Notes to write
# Local file: A file that exists on your computer.
# Path: Tells Python where the file is located.
# Relative path: A path relative to the current project/location, e.g. "backup.txt".
# upload_file(): boto3 S3 operation used to upload a local file to an S3 bucket.
# Syntax:
# s3.upload_file("LOCAL_FILE", "BUCKET_NAME", "S3_OBJECT_NAME")
# Arguments:
# 1. LOCAL_FILE       → file on our computer
# 2. BUCKET_NAME      → destination S3 bucket
# 3. S3_OBJECT_NAME   → name of the object inside S3

# Before uploading a local file, the file must actually exist at the path given to upload_file().
# "aws_test.txt"
#        ↓
# Python searches for the file
#        ↓
# File exists → upload can proceed
# File missing → FileNotFoundError


import boto3
client=boto3.client("Service")
s3=boto3.client("s3")
# response=s3.list_buckets
# response=s3.list_buckets()

# for bucket in response["buckets"]:
# #     print(bucket())
#     list_buckets()  → parentheses → CALL something
# "Buckets"       → quotes      → dictionary key
# "Name"          → quotes      → dictionary key
import os

print(os.path.exists("aws_test.txt"))
s3.upload_file("aws_test.txt", "ratnesh-s3-sqs-lambda-project-1", "aws_test.txt")
print("File uploaded successfully!")