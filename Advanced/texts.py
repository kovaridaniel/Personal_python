def Sentences(text):
    sentences = []
    index = 0
    while len(text) > 0:
        for char in text:
            if char == "!" or char == "." or char == "?":
                sentences.append(text[:index+1])
                text = text[index+1:]
            index += 1
        print(sentences)
    return sentences

