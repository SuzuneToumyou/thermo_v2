#!/usr/bin/python3
# -*- coding: utf-8 -*

import csv
from sklearn.decomposition import PCA
import numpy as np

pass_data = "./data/"
kari = "202206291042"
format_a = ".csv"

file_name = pass_data + kari + format_a

keta = 250

#print(file_name)

def pca_convert():

    csv_file = open(file_name, encoding="utf-8",  newline="" )
    f = csv.reader(csv_file)
    content = [row for row in f]
    #print(content)

    tP2 = sorted(content,reverse=True,key=lambda x: x[0])
    del tP2[keta:]
    #print(tP2)

    pca = PCA(n_components = 1)
    X2D =  pca.fit_transform(tP2)
    X2D.shape

    #print (X2D)

    outfile_name = file_name[:-4] + "pca.csv"

    fout = open(outfile_name, "w")
    np.savetxt(fout,X2D,delimiter=",")
    fout.close()

if __name__ == "__main__":
    pca_convert()
