# Problem
In our infrastructure there is a production bucket. The security team does not want any user to drop any file that is not a prod file into this bucket. If a user uploads a non_prod file into the production bucket, the security team will like the following
 1. Immediately delete the object if the file name does not contain 'prod' at the end.
 2. Block the user from putting any object in the production bucket in future until another user uploads in that bucket.
 3. Alert Security team about the incident and the remediation (2 points above)

 The Chief sucurity wants this process to be automated


# Solution:
The services we will be making use of in this project will be

  1. IAM

      - Create an IAM role for you
      - Attach the awslambdaexecute, amazons3fullaccess and amazonsnsfullaccess policy to a lambda role.
      - Enter a role name for example 'lambda_access'.

  2. LAMBDA
      - Create a Lambda function
      - Enter a function name for example 's3putdelete'
      - Under 'Runtime' select 'python 3.7'.
      - Under 'permissions' select 'use an existing role' select the lambda role we created in number 1 called 'lambda_access'.

  3. S3 BUCKET
     - Create s3 bucket
     - Enter a bucket name for example 'prod-bucket101'
     - Under permissions uncheck "Block public access"
     - Click 'Create bucket'


  4. CLOUDTRAIL
     - If you do not have a cloudtrail take the steps below
     - Enter a Trail name for example 'object_event'
     - Under storage location select 'Create new S3 bucket. Create a bucket to store logs for the trail.'
     - Under 'additional setting' select 'Enabled' for 'Log file validation'
     - Under 'CloudWatch Logs' select 'Enabled'
     - Under 'Log Group' select 'New'
     - Under 'IAMRole' select 'New' and input:'AWSLambdaExecute'-This automatically creates a cloudwatch role for us by default
     - Click 'Next'
     - Under 'Event Types' select 'Management events' 'Data events' 'Insights events' 
     - Under insight events you select "API calls
     - Under 'Management events' select 'API Activity' click both 'Read' and 'Write'
     - Under s3 un-click 'All current and future S3 buckets' and select the bucket we created in number 3 called 'prod-bucket101'
     - Click 'Next' and 'Create Trail'

  5. CLOUDWATCH
     - Create Cloud Watch Rule
     - Click on 'Create Rule'
     - Under 'Event Source' select 'Event Pattern'
     - Under 'service name' select S3(simple storage service) and under 'event type' select 'object level operation'
     - click on the 'specific operation' we are trying get notifications on which is 'PutObject'
     - select 'specific bucket' which is the bucket we created in number 3 called 'prod-bucket101'
     - Click on 'Target' and under target select 'Lambda Function' Under lambda function select the lambda function we created in number 2.
     - Click 'Configure details'
     - input a customized rule name for example:'putobjectnotification'
     - Click 'Update Rule'

  6. SNS    
     - Create an SNS topic if you don't have one
     - Under 'Type' select 'Standard'
     - Create a Topic Name for example:'s3put'
     - Click 'Create topic'
     - Create subscription. select the 'topic arn' you just created.
     - Under 'protocol' select 'Email'
     - Under 'Endpoint' select the email of the security team that will be receiving the alert


Next step will be to go to the eventfile.py and test your code to see if cloudwatch is being triggereed
