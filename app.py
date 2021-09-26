from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('EyYislhcqnBkPRvUN1XumuzQrfMcQpnnmkA/5OoOvme2GTvZVMu7t6iUiAx8h+LaqCvZZJTDQ2RDO2WZ3yuHi5X1fa8Ite8RlYCXlXHJP9INRGn8OP3LSESoj0YE00rLeLGzSN7sqZML0oNPEKz5DAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('6daef92b94f2ff4b7b4643fefe7c298a')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if(event.message.text=="開始遊戲"):
        message = []
        message.append(ImageSendMessage(
            original_content_url="https://1.bp.blogspot.com/-01EYHTNY1L8/YUzFpmtzSyI/AAAAAAAAK6k/hSVh_PRA0I0YCSGRNbmLp6scgEqufHbnwCLcBGAsYHQ/s320/1%2B%25282%2529.jpg",
            preview_image_url="https://1.bp.blogspot.com/-01EYHTNY1L8/YUzFpmtzSyI/AAAAAAAAK6k/hSVh_PRA0I0YCSGRNbmLp6scgEqufHbnwCLcBGAsYHQ/s320/1%2B%25282%2529.jpg"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://1.bp.blogspot.com/-3Ss1iPFYMLQ/YUzFzJDggAI/AAAAAAAAK6o/vgakn2ob-uw1D_KYqje-Yj6BjDW4es1DQCLcBGAsYHQ/s320/2%2B%25282%2529.jpg",
            preview_image_url="https://1.bp.blogspot.com/-3Ss1iPFYMLQ/YUzFzJDggAI/AAAAAAAAK6o/vgakn2ob-uw1D_KYqje-Yj6BjDW4es1DQCLcBGAsYHQ/s320/2%2B%25282%2529.jpg"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://1.bp.blogspot.com/-fjO3u12rZ68/YUzF51j3cpI/AAAAAAAAK6w/Lq3CP63dBSQIzIcsrQobaMOEL1rG1oUvgCLcBGAsYHQ/s320/3%2B%25282%2529.jpg",
            preview_image_url="https://1.bp.blogspot.com/-fjO3u12rZ68/YUzF51j3cpI/AAAAAAAAK6w/Lq3CP63dBSQIzIcsrQobaMOEL1rG1oUvgCLcBGAsYHQ/s320/3%2B%25282%2529.jpg"
        ))
        #message.append(TextSendMessage(text=msg))
        line_bot_api.reply_message(event.reply_token, message)
        #message = TextSendMessage(text=msg)
        #line_bot_api.push_message(to, TextSendMessage(text='Hello World!'))
        #line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="忘記羅技原始碼":
        message=[]
        message.append(TextSendMessage(text="羅技宣傳耳塞的影片名稱是甚麼??"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="Introducing Vista 2 True Wireless Earbuds":
        message=[]
        message.append(TextSendMessage(text="羅技原始碼93413"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="introducing vista 2 true wireless earbuds":
        message=[]
        message.append(TextSendMessage(text="羅技原始碼93413"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="INTRODUCING VISTA 2 TRUE WIRELESS EARBUDS":
        message=[]
        message.append(TextSendMessage(text="羅技原始碼93413"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="忘記supermicro原始碼":
        message=[]
        message.append(TextSendMessage(text="請輸入supermicro的CEO英文名字"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="charles liang":
        message=[]
        message.append(TextSendMessage(text="supermicro原始碼70624"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="Charles Ciang":
        message=[]
        message.append(TextSendMessage(text="supermicro原始碼70624"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="CHARLES CIANG":
        message=[]
        message.append(TextSendMessage(text="supermicro原始碼70624"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="忘記原項原始碼":
        message=[]
        message.append(TextSendMessage(text="請輸入原項致力於生產的高科技晶片英文名稱"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="CMOS Imaging Sensor":
        message=[]
        message.append(TextSendMessage(text="原項原始碼04126"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="CMOS imaging sensor":
        message=[]
        message.append(TextSendMessage(text="原項原始碼04126"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="cmos imaging sensor":
        message=[]
        message.append(TextSendMessage(text="原項原始碼04126"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="CMOS IMAGING SENSOR":
        message=[]
        message.append(TextSendMessage(text="原項原始碼04126"))
        line_bot_api.reply_message(event.reply_token, message)
    elif "我的名字:" in event.message.text:
        message=[]
        message.append(TextSendMessage(text="恭喜!記得截圖兌換獎品喔"))
        line_bot_api.reply_message(event.reply_token, message)
    elif "我的名字：" in event.message.text:
        message=[]
        message.append(TextSendMessage(text="恭喜!記得截圖兌換獎品喔"))
        line_bot_api.reply_message(event.reply_token, message)
    else:
        msg="再想想!!"
        message=[]
        message.append(TextSendMessage(text=msg))
        line_bot_api.reply_message(event.reply_token, message)
        
    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

#if '最新合作廠商' in msg:
       # message = imagemap_message()
        #line_bot_api.reply_message(event.reply_token, message)
    #elif '最新活動訊息' in msg:
        #message = buttons_message()
        #line_bot_api.reply_message(event.reply_token, message)
    #elif '註冊會員' in msg:
       # message = Confirm_Template()
        #line_bot_api.reply_message(event.reply_token, message)
    #elif '旋轉木馬' in msg:
        #message = Carousel_Template()
        #line_bot_api.reply_message(event.reply_token, message)
    #elif '圖片畫廊' in msg:
        #message = test()
        #line_bot_api.reply_message(event.reply_token, message)
    #elif '功能列表' in msg:
       # message = function_list()
        #line_bot_api.reply_message(event.reply_token, message)
    #else:
        #msg="123"
