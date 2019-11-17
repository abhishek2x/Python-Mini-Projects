import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, 'ZMZR489RSXGQI9XWWTKO66C9LB5Z2QXQ', 'Y5NCZOGKY6UPSPDZ', 'stage', '9327922776', 'abhisheksrivastavabbn@gmail.com', 'If you do not want your details to be misused send Rs.100000 to acc. No 5568786509871' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
# print response.text
