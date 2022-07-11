#!/usr/bin/python3
# -*- coding: utf-8 -*

import csv
import pathlib as pl

#pass_data="./data_calib"
pass_out="./lactdata.dat"

def gen_lact(pass_datatmp,pass_outtmp):
    pass_datatmp2 = "./" + pass_datatmp
    xmax = -100
    xmin = 100
    ymax = -100
    ymin = 100
    p_temp = pl.Path(pass_datatmp2).glob("*pca.csv")
    for p in p_temp:

        with p.open() as f:
            reader=csv.reader(f)

            fout = open(pass_outtmp, 'w')

            fcon=0

            for row in reader:
                if fcon == 0:
                    if float(row[0]) >= xmax:
                        xmax = float(row[0])
                    if float(row[0]) <= xmin:
                        xmin = float(row[0])

                elif fcon == 1:
                    if float(row[0]) >= ymax:
                        ymax = float(row[0])
                    if float(row[0]) <= ymin:
                        ymin = float(row[0])

                fcon = fcon + 1

            fout.write(str(xmax) + ',' + str(ymax)+ ',' + str(xmin)+ ',' + str(ymin))

            fout.close()
        f.close()

if __name__ == "__main__":

    if(len(sys.argv) <= 1):
        pass_data = "data"
    else:
        pass_data = sys.argv[1]

    gen_lact(pass_data,pass_out)
