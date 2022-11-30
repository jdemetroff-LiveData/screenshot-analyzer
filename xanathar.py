import boto3

# Bucket is in livedata-devops
BUCKET_NAME = 'rekognition-demo-jd'
FILE_NAME = 'fwb_sample.png'

rekog_client = boto3.client('rekognition', 'us-east-2')

response = rekog_client.detect_text(Image={'S3Object': {'Bucket': BUCKET_NAME, 'Name': FILE_NAME}})
for finding in response['TextDetections']:
    print(f'Text: {finding["DetectedText"]} - Confidence: {finding["Confidence"]} - Type: {finding["Type"]}')
