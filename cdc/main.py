# -*- encoding: UTF-8 -*-
import os

import sys

FILE_NAME = '.cdm'


def cdc_main():
    '''
    移動
    :return:
    '''
    if len(sys.argv) != 2:
        sys.exit(1)

    home = os.path.expanduser('~')
    f = open(home + '/' + FILE_NAME, 'r')

    line = f.readline()
    while line:
        li = line.split('\t')
        if li[0] == sys.argv[1]:
            print(li[1][:-1])
            os.chdir(li[1][:-1])
            break
        line = f.readline()
    f.close()
