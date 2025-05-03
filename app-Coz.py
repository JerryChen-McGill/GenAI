#import os 
#from coze import Coze  # type: ignore
#os.environ['COZE_API_TOKEN'] = 'pat_sNrdyeLExBqKoYVJP2Jo87YJSQdbb5iARxLO8JnAGsDmhbypPz6F364VVPLugKeG'
#os.environ['COZE_BOT_ID'] = "7415366036532428806"

import sys
import requests
import os

#import ...
# 从环境变量获取Coze API凭据
API_TOKEN = os.environ.get('API_KEY')
BOT_ID = os.environ.get('COZE_BOT_ID')

# 检查环境变量是否设置
if not API_TOKEN or not BOT_ID:
    print("错误: 未设置API_KEY或COZE_BOT_ID环境变量")
    print("请设置所需的环境变量再运行程序")
    sys.exit(1)
 
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