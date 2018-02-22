import os
import boto3
from botocore.vendored import requests

sns_topic = boto3.resource('sns').Topic(os.environ['SNS_TOPIC'])

def lambda_handler(event, context):
    response = requests.get("https://random.dog/woof.json").json()
    pic_url = response['url']
    
    sns_topic.publish(Message=pic_url)
