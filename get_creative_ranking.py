# ec2実行ロールにpersonalize:GetRecommendationsの権限が必要

import boto3
import sys
import os
from dotenv import load_dotenv
from random import randint

load_dotenv()

item_len = 10
userId = str(randint(1, 31))
itemId = [str(i) for i in range(1, item_len + 1)]

session = boto3.Session(aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', None),
                        aws_secret_access_key=os.getenv(
                            'AWS_SECRET_ACCESS_KEY', None),
                        aws_session_token=os.getenv('AWS_SESSION_TOKEN', None))
personalizert = session.client('personalize-runtime',
                               region_name=os.getenv('REGION_NAME', None))

ranking_response = personalizert.get_personalized_ranking(
    campaignArn=os.getenv('CAMPAIGN_ARN_RANKING', None),
    inputList=itemId,
    userId=userId
)

ranking_result = ranking_response['personalizedRanking']

print("- Ranking items user Id: [{}]".format(userId))

for item in ranking_result:
    print('[{:>2s}] {}'.format(item['itemId'], item['score']))
