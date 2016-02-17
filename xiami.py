#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#sys.argv[] is the command line input

import webUtil
import sys
import re

# define user standard error: raise UserDefinedError('error discreption')
class UserDefinedError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

    def present(self):
        print('UserDefinedError: {}'.format(self.__str__()))


if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    xm = webUtil.xiami(username, password)
    signDate = xm.logNsign()
    with open('xiami.txt', 'r') as fh:
        line = fh.readline()
    pattern = re.compile(r'<date>(.*?)</date>')
    currDate = pattern.search(line).group(1)
    if currDate != signDate:
        wstr = '<user>{}</user><date>{}</date>'.format(username, signDate)
        with open('xiami.txt', 'w') as fh:
            fh.write(wstr)
