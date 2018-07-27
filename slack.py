#coding:utf-8
#!/usr/bin/env python

import requests, bs4, os
import json

slack_token = "xoxp-41888577685-164597196115-360693330051-bba97f8524c1065e466011d7535de70a"

web_hook = "https://hooks.slack.com/services/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"

requests.post(web_hook, data = json.dumps({
    'text': u'Test', # 投稿するテキスト
    'username': u'Ghost', # 投稿のユーザー名
    'icon_emoji': u':ghost:', # 投稿のプロフィール画像に入れる絵文字
    'link_names': 1, # メンションを有効にする
}))
