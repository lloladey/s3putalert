#After following the instructions in the readme file go ahead aand do the following
#Go to s3 and upload a file
#Go to your lambda funtion, click on lambda_function.py and clear all the codes in there and paste the code below
import json

def lambda_handler(event, context):
    print(event)
    
#After inputing the code above at the top of your code we have different tabs like "monitor" "test" "code". click on monirtoring. under monitor click on "view cloudwatch logs"
#this shows the log event of the s3 bucket we just uploaded. under this log event click on "view as text" and copy the log. 
#After copying the log go on google and type "pretty json" click on the second option "JSON Formatter & Validator"
#paste the log you copied earlier in the box. The formated log appear down below in a json format. copy this new format, go in your lambda function and paste this in your "Test tab" save the 
#changes, go on the "code" tab click on the "deploy" button and click on the "test" button the json file you copied in your test tab should appear in the "execution result"

#you can go ahead and execute the code in the s3alert.py! kindly clear out the code above before moving foward. this was for testing
