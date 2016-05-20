import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# logger.setLevel(logging.DEBUG)

cwl = boto3.client('logs')

def list_log_groups(prefix):
    results = []
    response = cwl.describe_log_groups(
        logGroupNamePrefix=prefix
    )
    results.extend(response['logGroups'])

    while 'nextToken' in response:
        response = cwl.describe_log_groups(
            logGroupNamePrefix='/aws/lambda',
            nextToken=response['nextToken']
        )
        results.extend(response['logGroups'])

    return results

def set_retention_policy(group, days):
    cwl.put_retention_policy(
        logGroupName=group,
        retentionInDays=days
    )

# This is the method that will be registered
# with Lambda and run on a schedule
def handler(event={}, context={}):
    for group in list_log_groups('/aws/lambda'):

        # ignore anthing that already has a retention policy
        if 'retentionInDays' in group:
            continue

        # set retention for this group
        set_retention_policy(group['logGroupName'], 7)
