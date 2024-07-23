
**Blog generation**
Blog generation using llama2 model using AWS Bedrock, and saving the generated blog in S3 bucket.

**API Request for Lamma2 in bedrock with 13b parameters**
```json
{
    "modelId": "meta.llama2-13b-chat-v1",
    "contentType": "application/json",
    "accept": "application/json",
    "body": "{\"prompt\":\"this is where you place your input text\",\"max_gen_len\":512,\"temperature\":0.5,\"top_p\":0.9}"
}
```

To update the boto3 library necessary to run the lambda function in aws, we need to update the old boto3 that is already there.
But we can use our custom installation of a new boto3 version.
Here we take that route.
Make a folder called `python` where we install our new boto3 library using: 
`pip install boto3 -t python/`
We need to zip this folder and add it as a Layer in Lambda on AWS.

> This recipe is same for all custom packages that aren't pre-installed on AWS.

Then choose 'Custom layers' to add the layer in Lambda.

-------------

We have to create API for interacting with Lambda layers.

To create an API in AWS, 
1. Go to API Gateway
2. Create an API
3. Give an API name
4. Create API

Once API is create, we have to create Route
1. Create a route
2. Add Method and api-end-point
3. In Route detail, you can add Authorization (`Attach Authorization`)
4. Add Integration (`Attach Integration`)
5. In the Integration details, `Create and attach an integration`
6. In `Create an integration` window, select the route and add the lambda function as `Integration target`


To add changes in the api functionality depending on stages in Production (Eg. Dev, Production).
These are done through APIs' `Stages`
By default it will be under `default` stage.

Stages can be added by,
1. Go to `Create Stages`
2. Add `Stage details`
3. Add `Stage variables`
4. Add other stuffs if we want to.

This stage can be deployed by clicking `Deploy` and selecting the proper stage name.
The url can be found on this same page where the `Deploy` button was there.

---------------

We are left to do create the S3 bucket where we can store our generated blog contents.

To create S3 bucket, 
1. Search for `S3` and click on it under Services
2. Give a bucket with the same name as that of the bucket name given in the lambda function code (For this project this is `aws_bedrock_llama2_project1`)
   This name should be unique throughout the region where the bucket is created. Means for given a particular user and a geographical region, there cannot be no two S3 buckets with the same name.
3. Create the bucket.

----------

Deploy the Lambda function too! You have to deploy the code in order to use it.

----------

# Test out the API using Postman as raw data!

```json
{
    "blog_topic": "The benefits of drinking Tea regularly"
}
```

If the api fails due to the code. 
Go to the lambda function page and there click on `Monitor` tab.
Click on `View CloudWatch Logs`
Now to see log, click on `Log Groups`
Select the lambda app name to find the respective logs.

-----

For Permission related issue,
Go to the lambda function page and there click on `Configuration` tab.
Select the `Role name` under `Execution role`
`Add permissions` in `Permissions policies`
Add the `AdministratorAccess`.

Now you can go back and see that under `Execution role`, there will be updated `Resource summary` with the new accesses. 
