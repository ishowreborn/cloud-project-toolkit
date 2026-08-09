# CLOUD automation project
import boto3
s3=boto3.client("s3")
s3.download_file(
    "project-s3-buckx1",
    "csv-uploadx1/top_industries_last_decade.csv",
    "top_industries_downloaded.csv"
)
