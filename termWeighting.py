import math


def rawWeighting(document, term):
    doc = []
    for i in range(len(document)):
        word = []
        for j in range(len(term)):
            word.append(document[i].count(term[j]))
        doc.append(word)
    return doc


def logFrequency(document):
    doc = []
    for i in range(len(document)):
        word = []
        for j in range(len(document[i])):
            count = document[i][j]
            if count > 0:
                word.append(1 + math.log10(count))
            else:
                word.append(0)
        doc.append(word)
    return doc


def frequency(document, term):
    df = []
    for i in range(len(term)):
        dfWeight = 0
        for j in range(len(document)):
            for k in range(len(document[j])):
                if term[i] in document[j][k]:
                    dfWeight += 1
        df.append(dfWeight)
    return df


def inverse(frequen, dataLength):
    idf = []
    for i in range(len(frequen)):
        idft = math.log10(dataLength/frequen[i])
        idf.append(idft)
    return idf


def Dfidf(logFrequency, inverse):
    tf_idf = []
    for document in logFrequency:
        temp = []
        for i in range(0,len(inverse)):
            temp.append(document[i]*inverse[i])
        tf_idf.append(temp)
    return tf_idf

