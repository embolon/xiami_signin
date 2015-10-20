#!/usr/bin/env python

import requests
import re

class xiami:

    def __init__(self, email, password):
        self.se = requests.Session()
        self.login_data = {}
        self.login_data['email'] = email
        self.login_data['password'] = password
        self.login_data['from'] = 'web'
        self.login_data['done'] = 'http://www.xiami.com'
        self.login_data['havanaId'] = ''
        self.login_data['submit'] = '登 录'
        self.URL = {}
        self.URL['login'] = 'https://login.xiami.com/member/login'
        self.URL['web'] = 'http://www.xiami.com/web'

    def initConfig(self):
        self.login_data = dataParser.login_data
        self.URL = dataParser.URL

    def get(self, url):
        headers = {'User-Agent': 'Chrome/45.0.2454.101'}
        return self.se.get(url, headers=headers)

    def post(self, url, data):
        headers = {'User-Agent': 'Chrome/45.0.2454.101'}
        return self.se.post(url, data = data, headers = headers)

    def getMainPage(self):
        return self.get(self.URL['web'])

    def login(self):
        r = self.post(self.URL['login'], data = self.login_data)
        return r

    def signin(self, url):
        headers = {'Referer': 'http://www.xiami.com/web',
                   'User-Agent': 'Chrome/45.0.2454.101'}
        r = self.se.post(url, data = None, headers = headers)
        return r

    def signinAvail(self, page):
        pattern = re.compile(r'每日签到')
        return pattern.search(page)

    def getSignDate(self, page):
        pattern = re.compile(r'<div class="idh">已连续签到(.*?)天</div>')
        return pattern.search(page)
		
    def logNsign(self):
        print('xiami Login ... wait')
        r = self.login()
        try:
            res = r.json()
            if res['message'] == 'success':
                print('login success')
                user_id = res['data']['user_id']
            else:
                print('login failed')
                return
        except:
            print('login failed')
            return
        mainPage = self.getMainPage()
        if self.signinAvail(mainPage.text):
            signUrl = 'http://www.xiami.com/web/checkin/id/{}'.format(user_id)
            mainPage = self.signin(signUrl)
        signDatePattern = self.getSignDate(mainPage.text)
        signDate = signDatePattern.group(1)
        print('Sign in Date: {}'.format(signDate))
        return signDate

if __name__ == '__main__':
    print('Hello World')
