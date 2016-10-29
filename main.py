#!/usr/bin/env python

import requests
import xml.etree.ElementTree as ET


class yolp():
    '''YOLPに関するクラス'''

    def __init__(self, appid, location):
        '''初期化'''
        self.appid = appid
        self.location = location
        self.main()

    def setCoordinates(self):
        '''緯度・経度の設定'''
        coordinates = {
                'toyosu': {
                    'lat_deg': 35.654559,
                    'lng_deg': 139.796384
                    },
                'matsudo': {
                    'lat_deg': 35.785168,
                    'lng_deg': 139.900644
                    },
                'shinjuku': {
                    'lat_deg': 35.690559,
                    'lng_deg': 139.699574
                    }
                }
        return str(coordinates[self.location]['lng_deg']) + ',' + \
                str(coordinates[self.location]['lat_deg'])

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
        # response_field = [気象情報の区分, 日付と時刻, 降水強度[mm/h]]
        response_field = ['Type', 'Date', 'Rainfall']
        response_date = self.getXML(response_field[1])
        print(response_date)

if __name__ == '__main__':
    application_id = 'アプリケーションID'
    region = 'matsudo'
    yolp(application_id, region)
