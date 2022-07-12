#!/usr/bin/python3
# -*- coding: utf-8 -*

import csv
from sklearn.decomposition import PCA
import numpy as np

import sys

import pathlib as pl

keta = 250


def pca_convert(pass_intmp):

    pass_intmp2 = "./" + pass_intmp

    p_temp = pl.Path(pass_intmp2).glob("*.csv")
    for p in p_temp:
        #print(p)

        csv_file = open(p, encoding="utf-8",  newline="" )
        f = csv.reader(csv_file)
        content = [row for row in f]
        
        tP2 = sorted(content,reverse=True,key=lambda x: x[0])
        del tP2[keta:]

        pca = PCA(n_components = 1)
        X2D =  pca.fit_transform(tP2)
        X2D.shape

        outfile_name = str(p)[:-4] + "pca.csv"

        fout = open(outfile_name, "w")
        np.savetxt(fout,X2D,delimiter=",")
        fout.close()

if __name__ == "__main__":

    if(len(sys.argv) <= 1):
        pass_data = "data"
    else:
        pass_data = sys.argv[1]

    pca_convert(pass_data)
