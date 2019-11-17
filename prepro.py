from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()


def tokenisation(document):
    doc1 = []
    i = 0
    for i in range(len(document)):
        rep = document[i].replace("-", " ")
        spl = rep.lower().split(" ")
        doc1.append(spl)
    return doc1


def filtering(document, stop):
    doc = []
    for documents in document:
        word = []
        for temp in documents:
            if temp not in stop:
                word.append(temp)
        doc.append(word)
    return doc


def stemming(document):
    doc = []
    for documents in document:
        word = []
        for temp in documents:
            word.append(stemmer.stem(temp))
        doc.append(word)
    return doc


def term(document):
    doc = []
    for documents in document:
        for word in documents:
            if word not in doc:
                doc.append(word)

    return doc

