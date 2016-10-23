#!/usr/bin/env python

import requests
import xml.etree.ElementTree as ET


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

    def findText(self, root, xpath):
        '''XPathから要素中のテキストを取得'''
        for string in root.findall(xpath):
            print(string.tag)
            print(string.text)

    def getXML(self, tag):
        '''URLをGETして天気に関するXMLを取得'''
        res = requests.get(self.generateURL())
        root = ET.fromstring(res.text)
        # XPathにはXMLの名前空間を含める必要あり
        xpath = './/{http://olp.yahooapis.jp/ydf/1.0}' + tag
        self.findText(root, xpath)
        return root

    def main(self):
        '''ここに手順を書く'''
        response_date = self.getXML('Date')
        print(response_date)

if __name__ == '__main__':
    application_id = 'アプリケーションID'
    yolp(application_id)
