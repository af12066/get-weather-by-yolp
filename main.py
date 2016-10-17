#!/usr/bin/env python

import requests


class yolp():
    '''YOLPに関するクラス'''

    def __init__(self, id):
        '''初期化'''
        self.appid = id
        self.main()

    def setCoordinates(self):
        '''緯度・経度の設定'''
        self.__longitude = 139.900620
        self.__latitude = 35.785166
        return str(self.__longitude) + ',' + str(self.__latitude)

    def generateURL(self):
        '''リクエストURLの生成'''
        uri = 'http://weather.olp.yahooapis.jp/v1/place?coordinates=' \
                + self.setCoordinates() \
                + '&appid=' \
                + self.appid \
                + '&output=xml'
        return uri

    def getXML(self):
        '''URLをGETして天気に関するXMLを取得'''
        res = requests.get(self.generateURL())
        print(res.text)

    def main(self):
        '''ここに手順を書く'''
        self.getXML()

if __name__ == '__main__':
    application_id = 'アプリケーションID'
    yolp(application_id)
