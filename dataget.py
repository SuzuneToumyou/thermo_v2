#!/usr/bin/python3
# -*- coding: utf-8 -*

import pigpio
import time
#import struct

import math
import csv
import sys

#import numpy as np
#from sklearn.decomposition import PCA
#import pathlib as pl

import datetime

#pass_data = "./data/"

def senser_get(pass_datatmp):
    pi = pigpio.pi()
    addr = 0x0a
    try:
        h = pi.i2c_open(1,addr) # ハンドル取得
        pi.i2c_write_device(h, [0x4d])
        time.sleep(2)
        count, result = pi.i2c_read_device(h,2051)
        time.sleep(2)
    except:
        count = -80
    if count <= 0:
        return(0)
    
    else:
        now_date = datetime.datetime.now()
        now = now_date.strftime("%Y%m%d%H%M")

        tP = []
        file_name= "./" + pass_datatmp + "/" + str(now) + ".csv"
        fout= open(file_name,"w")
        writer = csv.writer(fout)

        readbuff = bytes(result)

        tPTAT = (256*readbuff[1] + readbuff[0])/10

        for i in range(1025):
            if i != 0:
                tmp = (256*readbuff[i*2+1] + readbuff[i*2])/10
                tP.append([tmp, (i-1)%32, math.floor((i-1)/32)])

        writer.writerows(tP)
        fout.close()

        return(1)
    tP.clear()
    pi.i2c_close(h)

if __name__ == "__main__":

    if(len(sys.argv) <= 1):
        pass_data = "data"
    else:
        pass_data = sys.argv[1]
        
    return_data = senser_get(pass_data)
    if return_data == 0:
        num = 0
        while return_data == 0 or num <= 3:
            return_data = senser_get(pass_data)
            num = num + 1
