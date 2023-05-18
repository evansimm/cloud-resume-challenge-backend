#!/usr/bin/env python3

import json  # import the json module
import boto3  # import the boto3 module for AWS SDK

# create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
# set the name of the table to 'VisitorCount'
ddbTableName = 'VisitorCount'
# create a Table resource with the specified table name
table = dynamodb.Table(ddbTableName)

# define the Lambda function handler
def lambda_handler(event, context):
	# retrieve the item from the DynamoDB table with the specified primary key
	response = table.get_item(Key={'id': 'count'})
	# extract the visitor count from the item and convert it to an integer
	count = int(response["Item"]["visitor_count"])
	# increment the count by 1
	new_count = count + 1
	# convert the incremented count to a string
	new_count_str = str(new_count)
	# update the visitor count in the DynamoDB table
	table.update_item(
		Key={'id': 'count'},
		UpdateExpression='set visitor_count = :c',
		ExpressionAttributeValues={':c': new_count_str},
		ReturnValues='UPDATED_NEW'
	)
	# return a dictionary containing the new count value
	return {'Count': new_count_str}
