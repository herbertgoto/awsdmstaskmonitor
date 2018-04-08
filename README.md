# awsdmstaskmonitor

There is no a Cloudwatch way to monitor DMS replication task status. 

This Lambda allows to ask for the state of any replication task and if one of them is in a failed state, an SNS topic is invoke. 

In the code, the SNS topic is configure for mail but it can be configured to any of other means of notification. 

The role for the lambda must have the AWSLambdaBasicExecutionRole policy and a customer managed policy with the following permissions: dms:DescribeReplicationTasks and sns:Publish; tied to the proper ARN. 

To trigger the Lambda you can use a Cloudwatch rule to check the status periodically or event bases. 
