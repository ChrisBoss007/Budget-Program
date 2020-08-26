import clx.xms
import requests

client = clx.xms.Client(service_plan_id='9b87dfe9dd7d4529babc379cdedbf2f1', token='cd04b03a2b76466faa0101c537ed401b')

create = clx.xms.api.MtBatchTextSmsCreate()
create.sender = '447537404817'
create.recipients = {'64224362039'}
create.body = 'This is a test message from your Sinch account'

try:
  batch = client.create_batch(create)
except (requests.exceptions.RequestException,
  clx.xms.exceptions.ApiException) as ex:
  print('Failed to communicate with XMS: %s' % str(ex))

import time
from time import sleep 
from sinchsms import SinchSMS 
  
# function for sending SMS 
def sendSMS(): 
  
    # enter all the details 
    # get app_key and app_secret by registering 
    # a app on sinchSMS 
    number = 'your_mobile_number'
    app_key = 'your_app_key'
    app_secret = 'your_app_secret'
  
    # enter the message to be sent 
    message = 'Hello Message!!!'
  
    client = SinchSMS(app_key, app_secret) 
    print("Sending '%s' to %s" % (message, number)) 
  
    response = client.send_message(number, message) 
    message_id = response['messageId'] 
    response = client.check_status(message_id) 
  
    # keep trying unless the status retured is Successful 
    while response['status'] != 'Successful': 
        print(response['status']) 
        time.sleep(1) 
        response = client.check_status(message_id) 
  
    print(response['status']) 
  
if __name__ == "__main__": 
    sendSMS()
