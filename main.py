# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:45:37 2019 

@author: Windows
"""
import prepro as pre
import termWeighting as weight


# Mengimpor Stopword pada txt
f = open('stopword.txt', 'r')
content = f.read()
spl = content.rstrip()
stop = spl.split()
# Inisialisasi pada setiap dokumen
doc1 = "kupu-kupu terbang di atas pohon"
doc2 = "dia terbang sambil mencari pohon untuk bertelur"
doc3 = "pohon tempat kupu kupu bertelur adalah pohon mangga"
doc4 = "kupu-kupu bertelur untuk berkembang biak"
# Memasukkan dokumen kedalam Array
document = [doc1, doc2, doc3, doc4]


# Proses akan di tokenisation terlebih dahulu kemudian akan difilter yang kemudian akan disimpan pada variabel s
token = pre.tokenisation(document)
print(token)
filtering = pre.filtering(token, stop)
print("filtering",filtering)
stemming = pre.stemming(filtering)
print("Hasil Stemming")
print(stemming)
term = pre.term(stemming)
print("Hasil Term")
print(term)
raw = weight.rawWeighting(stemming, term)
print("Hasil RawWeighting")
print(raw)
log = weight.logFrequency(raw)
print("Hasil LogFrequency")
print(log)
frequncy = weight.frequency(stemming, term)
print("Hasil Frequency")
print(frequncy)
invers = weight.inverse(frequncy, len(document))
print("Hasil Inverse")
print(invers)
dfidf = weight.Dfidf(log, invers)
print("\n")
print(dfidf)
