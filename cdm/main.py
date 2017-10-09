# -*- encoding: UTF-8 -*-
import os

import sys

FILE_NAME = '.cdm'

def cdm_main():
    '''
    登録
    :return:
    '''
    if len(sys.argv) != 2:
        sys.exit(1)

    home = os.path.expanduser('~')
    f = open(home + '/' + FILE_NAME, 'a+')

    line = f.readline()
    while line:
        li = line.split('\t')
        if li[0] != sys.argv[1]:
            f.write(line)

    arg = sys.argv[1]
    c = os.getcwd()
    f.write(arg + '\t' + c + '\n')
    f.close()
