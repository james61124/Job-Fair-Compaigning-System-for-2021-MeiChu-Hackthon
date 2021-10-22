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
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244746076_1523729284648354_2814710021989982106_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=730e14&_nc_ohc=LvQr8pRQjaMAX_QZVP4&_nc_ht=scontent-tpe1-1.xx&oh=00674243940fbdba7dcef7959d516cd4&oe=6188DF9D",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244746076_1523729284648354_2814710021989982106_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=730e14&_nc_ohc=LvQr8pRQjaMAX_QZVP4&_nc_ht=scontent-tpe1-1.xx&oh=00674243940fbdba7dcef7959d516cd4&oe=6188DF9D"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244483680_1523729587981657_6057869114533392314_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=730e14&_nc_ohc=hdETSZ0DO1AAX-O1LII&tn=iTBmPKelHvVMj8qw&_nc_ht=scontent-tpe1-1.xx&oh=e9ed580f10f5a6c737620fe8cd4b96a2&oe=6186DE8A",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244483680_1523729587981657_6057869114533392314_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=730e14&_nc_ohc=hdETSZ0DO1AAX-O1LII&tn=iTBmPKelHvVMj8qw&_nc_ht=scontent-tpe1-1.xx&oh=e9ed580f10f5a6c737620fe8cd4b96a2&oe=6186DE8A"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244746075_1523729727981643_7513390045428172144_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=730e14&_nc_ohc=9GlKHATj53UAX_1jFUt&_nc_ht=scontent-tpe1-1.xx&oh=449ef3d7c1569aa5e1f7a1305b5013a7&oe=6188B13F",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244746075_1523729727981643_7513390045428172144_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=730e14&_nc_ohc=9GlKHATj53UAX_1jFUt&_nc_ht=scontent-tpe1-1.xx&oh=449ef3d7c1569aa5e1f7a1305b5013a7&oe=6188B13F"
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
    elif event.message.text=="Charles liang":
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
    elif event.message.text=="忘記原相原始碼":
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
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244534559_1523731361314813_3028525321590764396_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_ohc=go144GVvO8gAX_VmpKv&_nc_ht=scontent-tpe1-1.xx&oh=3b707ae8586feaba5a82e0ec73c8fb5b&oe=6188C2FD",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244534559_1523731361314813_3028525321590764396_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_ohc=go144GVvO8gAX_VmpKv&_nc_ht=scontent-tpe1-1.xx&oh=3b707ae8586feaba5a82e0ec73c8fb5b&oe=6188C2FD"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244440627_1523731534648129_4640469324812149714_n.jpg?_nc_cat=109&ccb=1-5&_nc_sid=730e14&_nc_ohc=9wQvbAWa2jYAX_89crk&tn=iTBmPKelHvVMj8qw&_nc_ht=scontent-tpe1-1.xx&oh=9a59103f2316bc83e1dca048971def2a&oe=6186F79C",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244440627_1523731534648129_4640469324812149714_n.jpg?_nc_cat=109&ccb=1-5&_nc_sid=730e14&_nc_ohc=9wQvbAWa2jYAX_89crk&tn=iTBmPKelHvVMj8qw&_nc_ht=scontent-tpe1-1.xx&oh=9a59103f2316bc83e1dca048971def2a&oe=6186F79C"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244538726_1523731657981450_3917339840482423888_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=730e14&_nc_ohc=k4YZYGgtktUAX9ncVM_&_nc_ht=scontent-tpe1-1.xx&oh=4e1b519c345deeeb09b23850e39d3a8a&oe=6188E4E7",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244538726_1523731657981450_3917339840482423888_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=730e14&_nc_ohc=k4YZYGgtktUAX9ncVM_&_nc_ht=scontent-tpe1-1.xx&oh=4e1b519c345deeeb09b23850e39d3a8a&oe=6188E4E7"
        ))
        message.append(TextSendMessage(text="QQ..CPU超載，請\"聯繫\"維修工人並跟他說\"CPU超載\"，以便繼續運作"))
        line_bot_api.reply_message(event.reply_token, message)
    #70趴收關
    elif event.message.text=="CPU修復碼58126":
        message = []
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244679561_1523733927981223_8056673617022392423_n.jpg?_nc_cat=104&ccb=1-5&_nc_sid=730e14&_nc_ohc=YKjTfSs6p7YAX9EMIy3&tn=iTBmPKelHvVMj8qw&_nc_ht=scontent-tpe1-1.xx&oh=58ac8f80fe363aa94e52a6a2cfbb85d0&oe=61883DE0",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244679561_1523733927981223_8056673617022392423_n.jpg?_nc_cat=104&ccb=1-5&_nc_sid=730e14&_nc_ohc=YKjTfSs6p7YAX9EMIy3&tn=iTBmPKelHvVMj8qw&_nc_ht=scontent-tpe1-1.xx&oh=58ac8f80fe363aa94e52a6a2cfbb85d0&oe=61883DE0"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244465604_1523734361314513_2597882015681817780_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=730e14&_nc_ohc=_TYsOaJHm6EAX-4Uh1M&tn=iTBmPKelHvVMj8qw&_nc_ht=scontent-tpe1-1.xx&oh=a38bbb7522915f72245f4e339059fcdc&oe=6189B57C",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244465604_1523734361314513_2597882015681817780_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=730e14&_nc_ohc=_TYsOaJHm6EAX-4Uh1M&tn=iTBmPKelHvVMj8qw&_nc_ht=scontent-tpe1-1.xx&oh=a38bbb7522915f72245f4e339059fcdc&oe=6189B57C"
        ))
        message.append(TextSendMessage(text="進行最後身分驗證，請輸入五位驗證碼"))
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/241397758_4693290240682338_4295708469528341812_n.png?_nc_cat=101&ccb=1-5&_nc_sid=e3f864&_nc_ohc=9nEdOGrzYVgAX8U9Yt0&_nc_ht=scontent-tpe1-1.xx&oh=3f53c375abd413801f83e26c209c25a3&oe=61878AC1",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/241397758_4693290240682338_4295708469528341812_n.png?_nc_cat=101&ccb=1-5&_nc_sid=e3f864&_nc_ohc=9nEdOGrzYVgAX8U9Yt0&_nc_ht=scontent-tpe1-1.xx&oh=3f53c375abd413801f83e26c209c25a3&oe=61878AC1"
        ))
        line_bot_api.reply_message(event.reply_token, message)
    #100趴收關
    elif event.message.text=="梅竹黑客松":
        message = []
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244470340_1523735634647719_5174180938226191416_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=730e14&_nc_ohc=advF76HgIDoAX8fOwe2&_nc_ht=scontent-tpe1-1.xx&oh=bccd59be5f4fa9b1c685698d1caceb95&oe=618934F8",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244470340_1523735634647719_5174180938226191416_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=730e14&_nc_ohc=advF76HgIDoAX8fOwe2&_nc_ht=scontent-tpe1-1.xx&oh=bccd59be5f4fa9b1c685698d1caceb95&oe=618934F8"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244468949_1523735737981042_2427317202944832377_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=730e14&_nc_ohc=tEyvvIpHrSkAX9KNGFm&tn=iTBmPKelHvVMj8qw&_nc_ht=scontent-tpe1-1.xx&oh=537fb7c22a4cea34c34625d663c53efb&oe=6189A5D0",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244468949_1523735737981042_2427317202944832377_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=730e14&_nc_ohc=tEyvvIpHrSkAX9KNGFm&tn=iTBmPKelHvVMj8qw&_nc_ht=scontent-tpe1-1.xx&oh=537fb7c22a4cea34c34625d663c53efb&oe=6189A5D0"
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
    elif event.message.text=="開始第二階遊戲":
        message=[]
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244143118_1523737334647549_5404780947260375426_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=730e14&_nc_ohc=EdTo9UY_Gh8AX941TIw&_nc_ht=scontent-tpe1-1.xx&oh=219dd009f59980f640cd848bb1838763&oe=61896FF0",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244143118_1523737334647549_5404780947260375426_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=730e14&_nc_ohc=EdTo9UY_Gh8AX941TIw&_nc_ht=scontent-tpe1-1.xx&oh=219dd009f59980f640cd848bb1838763&oe=61896FF0"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244013932_1523737471314202_952905935827290928_n.jpg?_nc_cat=109&ccb=1-5&_nc_sid=730e14&_nc_ohc=CXop1z8zMckAX_Mpg7h&_nc_ht=scontent-tpe1-1.xx&oh=1b5e87586d661d3b0f5e82d343a31313&oe=618714F6",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244013932_1523737471314202_952905935827290928_n.jpg?_nc_cat=109&ccb=1-5&_nc_sid=730e14&_nc_ohc=CXop1z8zMckAX_Mpg7h&_nc_ht=scontent-tpe1-1.xx&oh=1b5e87586d661d3b0f5e82d343a31313&oe=618714F6"
        ))
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="時空彈跳系統修復碼9384235":
        message=[]
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244520711_1523742171313732_7087740408732141861_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_ohc=7Y02XM3BxQUAX9dbh4y&_nc_ht=scontent-tpe1-1.xx&oh=487b7c29a42ba37cbd1e7caf7bf5c722&oe=6186742C",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244520711_1523742171313732_7087740408732141861_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_ohc=7Y02XM3BxQUAX9dbh4y&_nc_ht=scontent-tpe1-1.xx&oh=487b7c29a42ba37cbd1e7caf7bf5c722&oe=6186742C"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244345826_1523742634647019_7509040325766939356_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=730e14&_nc_ohc=rTCJIEIJMi8AX_V90OR&_nc_ht=scontent-tpe1-1.xx&oh=ad8ae6556f5f6363502ed63a5dde2b2a&oe=61868E3C",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244345826_1523742634647019_7509040325766939356_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=730e14&_nc_ohc=rTCJIEIJMi8AX_V90OR&_nc_ht=scontent-tpe1-1.xx&oh=ad8ae6556f5f6363502ed63a5dde2b2a&oe=61868E3C"
        ))
        message.append(ImageSendMessage(
            original_content_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244469852_1523742721313677_93520568350537129_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=730e14&_nc_ohc=0t6_a2jbNhoAX-E0Vs4&_nc_ht=scontent-tpe1-1.xx&oh=52f17c98b4d70fea518a88c1a0cf8877&oe=6187FB1B",
            preview_image_url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/244469852_1523742721313677_93520568350537129_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=730e14&_nc_ohc=0t6_a2jbNhoAX-E0Vs4&_nc_ht=scontent-tpe1-1.xx&oh=52f17c98b4d70fea518a88c1a0cf8877&oe=6187FB1B"
        ))
        message.append(TextSendMessage(text="您已完成第二階段，請輸入\"我的gather town名字:_____\"並截圖最後通關的對話紀錄，便能再次擁有抽獎機會"))
        line_bot_api.reply_message(event.reply_token, message)
    elif "我的gather town名字:" in event.message.text:
        message=[]
        message.append(TextSendMessage(text="感謝您完成RPG遊戲，黑客松祝您比賽順利"))
        line_bot_api.reply_message(event.reply_token, message)
    elif "我的gather town名字：" in event.message.text:
        message=[]
        message.append(TextSendMessage(text="感謝您完成RPG遊戲，黑客松祝您比賽順利"))
        line_bot_api.reply_message(event.reply_token, message)
    elif "我的gather town 名字:" in event.message.text:
        message=[]
        message.append(TextSendMessage(text="感謝您完成RPG遊戲，黑客松祝您比賽順利"))
        line_bot_api.reply_message(event.reply_token, message)
    elif "我的 gather town 名字:" in event.message.text:
        message=[]
        message.append(TextSendMessage(text="感謝您完成RPG遊戲，黑客松祝您比賽順利"))
        line_bot_api.reply_message(event.reply_token, message)
    elif "我的 gather town名字:" in event.message.text:
        message=[]
        message.append(TextSendMessage(text="感謝您完成RPG遊戲，黑客松祝您比賽順利"))
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
