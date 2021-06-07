def sentencereverse(sentence):
    sen = sentence[:-1]
    word_list = sen.split()
    reversed_list = word_list[:: -1]
    reversed_sentence = " ".join(reversed_list)
    reversed_sentence = reversed_sentence + "."
    return(reversed_sentence)

#print(sentencereverse("My name is V Tadimeti."))

#print(sentencereverse("Happy Birthday To You."))

#print(sentencereverse("My name is Sally."))