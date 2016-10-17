#!/usr/bin/env python

import requests

class yolp():
    def __init__(self, id):
        self.appid = id
        print(self.appid)

if __name__ == '__main__':
    application_id = 'アプリケーションID'
    yolp(application_id)

