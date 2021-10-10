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
    #開關
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
        line_bot_api.reply_message(event.reply_token, message)
    #實驗室(羅技)
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
    #實驗室(supermicro)
    elif event.message.text=="忘記supermicro原始碼":
        message=[]
        message.append(TextSendMessage(text="請輸入supermicro的CEO英文名字"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="charles liang":
        message=[]
        message.append(TextSendMessage(text="supermicro原始碼70624"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="Charles Liang":
        message=[]
        message.append(TextSendMessage(text="supermicro原始碼70624"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="CHARLES LIANG":
        message=[]
        message.append(TextSendMessage(text="supermicro原始碼70624"))
        line_bot_api.reply_message(event.reply_token, message)
    #實驗室(原相)
    elif event.message.text=="忘記原相科技原始碼":
        message=[]
        message.append(TextSendMessage(text="請輸入原相致力於生產的高科技晶片英文名稱"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="CMOS Sensor":
        message=[]
        message.append(TextSendMessage(text="原相原始碼04126"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="CMOS sensor":
        message=[]
        message.append(TextSendMessage(text="原相原始碼04126"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="cmos sensor":
        message=[]
        message.append(TextSendMessage(text="原相原始碼04126"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="CMOS SENSOR":
        message=[]
        message.append(TextSendMessage(text="原相原始碼04126"))
        line_bot_api.reply_message(event.reply_token, message)
    #實驗室(美光)
    elif event.message.text=="忘記美光原始碼":
        message=[]
        message.append(TextSendMessage(text="請輸入美光在甚麼領域有領先地位"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="DRAM":
        message=[]
        message.append(TextSendMessage(text="美光原始碼53234"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="dram":
        message=[]
        message.append(TextSendMessage(text="美光原始碼53234"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="忘記NXP原始碼":
        message=[]
        message.append(TextSendMessage(text="請輸入NXP主要的四大市場"))
        line_bot_api.reply_message(event.reply_token, message)
    #實驗室(NXP)
    elif ("automotive" in event.message.text) & ("communication infrastructure" in event.message.text) & ("industrial" in event.message.text) & ("mobile" in event.message.text) :
        message=[]
        message.append(TextSendMessage(text="NXP原始碼88332"))
        line_bot_api.reply_message(event.reply_token, message)
    elif ("Automotive" in event.message.text) & ("Communication Infrastructure" in event.message.text) & ("Industrial" in event.message.text) & ("Mobile" in event.message.text) :
        message=[]
        message.append(TextSendMessage(text="NXP原始碼88332"))
        line_bot_api.reply_message(event.reply_token, message)
    elif ("AUTOMOTIVE" in event.message.text) & ("COMMUNICATION INFRASTRUCTURE" in event.message.text) & ("INDUSTRIAL" in event.message.text) & ("MOBILE" in event.message.text) :
        message=[]
        message.append(TextSendMessage(text="NXP原始碼88332"))
        line_bot_api.reply_message(event.reply_token, message)
    #40趴收關
    elif ("羅技原始碼93413" in event.message.text) & ("supermicro原始碼70624" in event.message.text) & ("原相原始碼04126" in event.message.text) & ("美光原始碼53234" in event.message.text) & ("NXP原始碼88332" in event.message.text):
        message = []
        message.append(ImageSendMessage(
            original_content_url="https://1.bp.blogspot.com/-1LLFrpwPzbY/YU3TYbtHAoI/AAAAAAAAK7A/WU86jyFCECsPPZpTqIbiwrkMiDKP8P-AwCLcBGAsYHQ/s320/4%2B%25282%2529.jpg",
            preview_image_url="https://1.bp.blogspot.com/-1LLFrpwPzbY/YU3TYbtHAoI/AAAAAAAAK7A/WU86jyFCECsPPZpTqIbiwrkMiDKP8P-AwCLcBGAsYHQ/s320/4%2B%25282%2529.jpg"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://1.bp.blogspot.com/-hInuenMa3oM/YU3TgvZNbbI/AAAAAAAAK7E/okawr7CIyFMb76vNW9gu_1TjkfOMu3cEgCLcBGAsYHQ/s320/5%2B%25281%2529.jpg",
            preview_image_url="https://1.bp.blogspot.com/-hInuenMa3oM/YU3TgvZNbbI/AAAAAAAAK7E/okawr7CIyFMb76vNW9gu_1TjkfOMu3cEgCLcBGAsYHQ/s320/5%2B%25281%2529.jpg"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://1.bp.blogspot.com/-ttAoh7DB_T0/YU3To0FXMrI/AAAAAAAAK7M/pgkhiPEJg6MINzSZw0qHwti_MRUjO5KHQCLcBGAsYHQ/s320/6%2B%25281%2529.jpg",
            preview_image_url="https://1.bp.blogspot.com/-ttAoh7DB_T0/YU3To0FXMrI/AAAAAAAAK7M/pgkhiPEJg6MINzSZw0qHwti_MRUjO5KHQCLcBGAsYHQ/s320/6%2B%25281%2529.jpg"
        ))
        message.append(TextSendMessage(text="QQ..CPU超載，請\"聯繫\"維修工人並跟他說\"CPU超載\"，以便繼續運作"))
        line_bot_api.reply_message(event.reply_token, message)
    #70趴收關
    elif event.message.text=="CPU修復碼58126":
        message = []
        message.append(ImageSendMessage(
            original_content_url="https://1.bp.blogspot.com/-yCqXt7vB1Q8/YU3TzyeHmRI/AAAAAAAAK7Q/FP1ekyjssSMTkUmhGBoCnu25D5GHabAiACLcBGAsYHQ/s320/7%2B%25281%2529.jpg",
            preview_image_url="https://1.bp.blogspot.com/-yCqXt7vB1Q8/YU3TzyeHmRI/AAAAAAAAK7Q/FP1ekyjssSMTkUmhGBoCnu25D5GHabAiACLcBGAsYHQ/s320/7%2B%25281%2529.jpg"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://1.bp.blogspot.com/-yrF_CrbYV_U/YU3T7yc4CBI/AAAAAAAAK7U/RaDvg7Fp1DgQCi9xg0QrburBqcOWkyWAQCLcBGAsYHQ/s320/8%2B%25281%2529.jpg",
            preview_image_url="https://1.bp.blogspot.com/-yrF_CrbYV_U/YU3T7yc4CBI/AAAAAAAAK7U/RaDvg7Fp1DgQCi9xg0QrburBqcOWkyWAQCLcBGAsYHQ/s320/8%2B%25281%2529.jpg"
        ))
        message.append(TextSendMessage(text="進行最後身分驗證，請輸入五位驗證碼"))
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/241397758_4693290240682338_4295708469528341812_n.png?_nc_cat=101&ccb=1-5&_nc_sid=e3f864&_nc_ohc=7eV05bUhWuMAX8Uh5Rr&_nc_oc=AQnC6bfaYAU4eY4diTGxvStcO5PAzVoPMxbDF_h1f5U4DOvZy7JXYqZMlWy2GYOsiV8&_nc_ht=scontent-tpe1-1.xx&oh=0a3b0e5ca6d3bd404424d66fc7a79aab&oe=6173C441",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/241397758_4693290240682338_4295708469528341812_n.png?_nc_cat=101&ccb=1-5&_nc_sid=e3f864&_nc_ohc=7eV05bUhWuMAX8Uh5Rr&_nc_oc=AQnC6bfaYAU4eY4diTGxvStcO5PAzVoPMxbDF_h1f5U4DOvZy7JXYqZMlWy2GYOsiV8&_nc_ht=scontent-tpe1-1.xx&oh=0a3b0e5ca6d3bd404424d66fc7a79aab&oe=6173C441"
        ))
        line_bot_api.reply_message(event.reply_token, message)
    #100趴收關
    elif event.message.text=="梅竹黑客松":
        message = []
        message.append(ImageSendMessage(
            original_content_url="https://1.bp.blogspot.com/-O-ZyXcPHLaY/YU3UF-z8wwI/AAAAAAAAK7c/MaDKYnFcHo4TL_kOSsz-FtUzDvA6Y_HJQCLcBGAsYHQ/s320/9%2B%25281%2529.jpg",
            preview_image_url="https://1.bp.blogspot.com/-O-ZyXcPHLaY/YU3UF-z8wwI/AAAAAAAAK7c/MaDKYnFcHo4TL_kOSsz-FtUzDvA6Y_HJQCLcBGAsYHQ/s320/9%2B%25281%2529.jpg"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://1.bp.blogspot.com/-7trIijD2VMU/YU3UNkw2EPI/AAAAAAAAK7k/Gr77rUsobqYbkfnRgGqy1iNDqjGmEL5xwCLcBGAsYHQ/s320/10%2B%25281%2529.jpg",
            preview_image_url="https://1.bp.blogspot.com/-7trIijD2VMU/YU3UNkw2EPI/AAAAAAAAK7k/Gr77rUsobqYbkfnRgGqy1iNDqjGmEL5xwCLcBGAsYHQ/s320/10%2B%25281%2529.jpg"
        ))
        message.append(TextSendMessage(text="您已完成第一階段，請輸入\"我的名字:_____\"並截圖最後通關的對話紀錄，便能擁有抽獎機會"))
        line_bot_api.reply_message(event.reply_token, message)
    #一階default
    elif event.message.text=="忘記line原始碼":
        message=[]
        message.append(TextSendMessage(text="Line原始碼78326"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="忘記Line原始碼":
        message=[]
        message.append(TextSendMessage(text="Line原始碼78326"))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="忘記nuarl原始碼":
        message=[]
        message.append(TextSendMessage(text="nuarl原始碼90357"))
        line_bot_api.reply_message(event.reply_token, message)
    #收關
    elif "我的名字:" in event.message.text:
        message=[]
        message.append(TextSendMessage(text="恭喜!記得截圖至抽獎台抽獎喔"))
        message.append(TextSendMessage(text="若想繼續下一階的遊戲，請打\"開始第二階遊戲\""))
        line_bot_api.reply_message(event.reply_token, message)
    elif "我的名字：" in event.message.text:
        message=[]
        message.append(TextSendMessage(text="恭喜!記得截圖至抽獎台抽獎喔"))
        message.append(TextSendMessage(text="若想繼續下一階的遊戲，請打\"開始第二階遊戲\""))
        line_bot_api.reply_message(event.reply_token, message)
    else:
        msg="再想想!!"
        message=[]
        message.append(TextSendMessage(text=msg))
        line_bot_api.reply_message(event.reply_token, message)
#message.append(TextSendMessage(text=msg))     
#message = TextSendMessage(text=msg)
#line_bot_api.push_message(to, TextSendMessage(text='Hello World!'))
#line_bot_api.reply_message(event.reply_token, message)   

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
