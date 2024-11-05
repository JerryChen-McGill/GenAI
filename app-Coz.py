#import os 
#from coze import Coze  # type: ignore
#os.environ['COZE_API_TOKEN'] = 'pat_sNrdyeLExBqKoYVJP2Jo87YJSQdbb5iARxLO8JnAGsDmhbypPz6F364VVPLugKeG'
#os.environ['COZE_BOT_ID'] = "7415366036532428806"

import sys
import requests

#import ...
API_TOKEN = 'pat_sNrdyeLExBqKoYVJP2Jo87YJSQdbb5iARxLO8JnAGsDmhbypPz6F364VVPLugKeG'
BOT_ID = "7415366036532428806"
 
 
class Coze:
    def __init__(self,
                 bot_id= BOT_ID,
                 api_token = API_TOKEN,
                 max_chat_rounds=20,
                 stream=True,
                 history=None
                ):
        ...  
    @classmethod
    def build_messages(cls,history=None):
        ...
 
 
    @staticmethod
    def get_response(messages):
        ...
 
 
    def chat(self,query,stream=False):
        ...        
        
    def __call__(self,query):
        ...
 
 
    def register_magic(self):
        ...