import json
import boto3
s3_client= boto3.client("s3",)



def lambda_handler(event, context):
    record=event["Records"][0]
    event_time=record["eventTime"]
    user_identity=record["userIdentity"]["principalId"]
    ip_address=record["requestParameters"]["sourceIPAddress"]
    bucket_name=record["s3"]["bucket"]["name"]
    object_name=record["s3"]["object"]["key"]
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'AddPerm',
            'Effect': 'Deny',
            'Principal': {'AWS':f'arn:aws:iam::{user_identity}:root'},
            'Action': ['s3:PutObject'],
            'Resource': f'arn:aws:s3:::{bucket_name}/*'
        }]
    }

    bucket_policy = json.dumps(bucket_policy)

    #--------------------------------------------------------------------#
    #send sns notification
    add_bucketpolicy(bucket_name, bucket_policy)
    delete_object(bucket_name, object_name)
    send_sns(msg, "arn:aws:sns:us-east-1:262987825063:CloudTrailTopic")


def delete_object(buck_name, obj_name):
    objectdeletion=s3_client.delete_object(Bucket=buck_name, Key=obj_name)
    return objectdeletion

def add_bucketpolicy(buck_name, buck_policy):
    add_policy=s3_client.put_bucket_policy(Bucket=buck_name, Policy=buck_policy)
    return add_policy


def send_sns(msg, topic_arn):
    sns_client = boto3.client("sns",)
    response=sns_client.publish(Message=msg, TopicArn=topic_arn)
    msg="Dear Admin the user with the ID " + user_identity + " breached user account protocol at " + event_time +\
    " from IP " + ip_address + ". The user uploaded object: " + object_name + " in " + bucket_name + " bucket."
    return msg
