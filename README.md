# lambder-set-cwl-expirations

set-cwl-expirations is an AWS Lambda function for use with Lambder.

It will iterate through all CloudWatch Logs created by Lambdas and will set a one week retention policy on any that do not already have a policy.

REQUIRES:
* python-lambder

## Getting Started

1) Test the sample lambda function

    python lambda/set-cwl-expirations/set-cwl-expirations.py

2) Deploy the sample Lambda function to AWS

    lambder functions deploy

3) Invoke the sample Lambda function in AWS

    lambder functions invoke --input input/ping.json

4) Add useful code to lambda/set-cwl-expirations/set-cwl-expirations.py

5) Add any permissions you need to access other AWS resources to iam/policy.json

6) Update your lambda and permissions policy in one go

    lambder functions deploy

## Sharing your lambder function

If you decide to share your lambder function, you want to be sure you don't share
the name of your s3 bucket. We suggest you add `lambder.json` to your
`.gitignore` so it won't be commited to your repo. Instead, copy it to
`example_lambder.json` and remove any secrets before pushing to a public
repository.

## Using virtualenvwrapper

Your Lambdas should be as small as possible to reduce spinup time. If you need
to include extra python modules, use virtualenvwrapper.
The deploy script will look for a site-packages directory in
$WORKON_HOME/lambder-set-cwl-expirations and bundle those packages into the zip
that it uploads to AWS Lambda.
