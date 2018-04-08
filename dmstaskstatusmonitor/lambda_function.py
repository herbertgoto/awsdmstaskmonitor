# Automates DMS status
#
#
# This script will check a replication task status on demand and invoke SNS to alert in case of failure

from __future__ import print_function

import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info("Loading function")

# --------------- Main handler ------------------

def lambda_handler(event, context):
    
    logger.info("Received event: %s" + json.dumps(event, indent=2))

    # get dms client
    clientDMS = boto3.client('dms')
    clientSNS = boto3.client('sns')
    
    logger.info("DMS client created")

    # ask task status
    response = clientDMS.describe_replication_tasks(
        Filters=[
            {
            'Name': 'replication-task-id',
            'Values': [
                '', ''
                ]
            },
        ]
    )
    
    reptasks = response.get('ReplicationTasks')
    
    for i in reptasks:
        if i.get('Status') == 'failed':
            responseNOK = clientSNS.publish(
                TopicArn='',
                Message='',
                Subject=''
            )
#        else:
#            responseOK = clientSNS.publish(
#                TopicArn='',
#                Message='',
#                Subject=''
#            )
    
    return 'DMS replication task status checked.'
