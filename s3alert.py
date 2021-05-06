import json
import boto3
s3= boto3.client('s3')
sns= boto3.client('sns')


def lambda_handler(event, context):
    event_time   = event['detail']['eventTime']
    principal_id = event['detail']['userIdentity']['arn']
    ip_address   = event['detail']['sourceIPAddress']
    bucket_name  = event['detail']['requestParameters']['bucketName']
    object_name  = event['detail']['requestParameters']['key']


    TopicArn='arn:aws:sns:us-east-1:715804921220:s3put'
    Msg='Good Afternoon Admin, the user with the principalId ' + principal_id + ' has breached security protocal at ' + event_time +\
        ' time. This user uploaded an object called:' + object_name + ' in ' + bucket_name +\
        ' This operation was detected on this IpAdress:' + ip_address + ' The user has been blocked from uploading any file into the '+\
        bucket_name + ' bucket.'

    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'AddPerm',
            'Effect': 'Deny',
            'Principal': {'AWS': [principal_id]},
            'Action': ['s3:PutObject'],
            'Resource': f'arn:aws:s3:::{bucket_name}/*'
    }]
    }

    bucket_policy = json.dumps(bucket_policy)



    object_name_split = object_name.split('.')
    if object_name_split[0][-5:] != '_prod':
        del_obj(bucket_name, object_name)
        add_bucketpolicy(bucket_name, bucket_policy)
        s3_sns(TopicArn, Msg)



def del_obj(buck_name, obj_name):
    object_deletion=s3.delete_object(Bucket=buck_name, Key=obj_name)
    return object_deletion

def add_bucketpolicy(buck_name, buck_policy):
    add_policy=s3.put_bucket_policy(Bucket=buck_name, Policy=buck_policy)
    return add_policy


def s3_sns(topic_arn, body_msg):
    sns= boto3.client('sns')
    response = sns.publish(TopicArn=topic_arn, Message=body_msg)
    return response
