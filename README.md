# Problem




Solution:


- Step for this process
        1. I created an s3 bucket "prod-data10"
        2. create in iam lambda role and give it awslambdaexecute access,amazons3fullaccess,administratoraccess and amazonsnsfullaccess
        3. Create Lambda function, for the runtime choose python 3.7 and attach the role you created above to the lambda function
        4. Turned on cloudtrail log 
        5. create a cloudwatch rule
        6. Go to the "prod-data10" bucket under "properties" create event notifications
        7. Create a topic arn, create a subscription and attach the email of the security team
        8. Go in our lamda funtion, in the "Code" tabh import json and import boto3 after doing this paste the trail log below in the test tab to help us populate the information we need to get. the information we should be getting is [event_time, principal_id, ip_address, bucket_name, object_name]

  
