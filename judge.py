#!/usr/bin/python3
# -*- coding: utf-8 -*

import csv
import sys
import pathlib as pl

pass_lact="./lactdata.dat"
#pass_data="./data_e"

#import pathlib as pl

def judge_data(pass_lacttmp,pass_datatmp):

    pass_lacttmp2 = "./" + pass_lacttmp
    f = open(pass_lacttmp2, 'r')


    data = f.readline()
    data = data.replace("\n", "")
    l = data.split(",")

    max_x=l[0]
    max_y=l[1]
    min_x=l[2]
    min_y=l[3]

    dummy_x=0
    dummy_y=0

    p_temp = pl.Path(pass_datatmp).glob("*pca.csv")
    for p in p_temp:
        with p.open() as f_2:

            fcon = 0
            reader=csv.reader(f_2)
            for row in reader:
                if fcon == 0:
                    dummy_x = float(row[0])
                if fcon == 1:
                    dummy_y = float(row[0])
                fcon = fcon + 1

            if dummy_x <= float(max_x) and dummy_x >= float(min_x) and dummy_y <= float(max_y) and dummy_y >= float(min_y):
                print ("nomal")
            else :
                print ("abnomal")

            f_2.close()

    f.close()

if __name__ == '__main__':

    if(len(sys.argv) <= 1):
        pass_data = "data"
    else:
        pass_data = sys.argv[1]

    judge_data(pass_lact,pass_data)
