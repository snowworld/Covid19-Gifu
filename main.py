import os

from flask import request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReplyButton, MessageAction, QuickReply,
)

import getNumberOf

# get channel_secret and channel_access_token from your environment variable
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

def main(request):
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:

        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        userText = event.message.text

        dict = {"陽性者数": "最新の陽性者数は？",
                "死亡者数": "最新の死亡者数は？",
                "検査数": "最新の検査数は？",
                "健康相談件数": "最新の健康相談件数は？",
                "コロナ相談数": "最新のコロナ相談数は？"}

        # get statistic data
        stat = getNumberOf.getNumberOf(userText)

        items = [QuickReplyButton(action=MessageAction(label=key, text=value)) for key, value in dict.items()]

        messages = TextSendMessage(text=f'{ stat }\n他に知りたい情報は？', quick_reply=QuickReply(items=items))

        line_bot_api.reply_message(event.reply_token, messages)

    return 'OK'