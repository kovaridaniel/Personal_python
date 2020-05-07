def Sentences(text):
    sentences = []
    index = 0
    sentence = ""
    while len(text) > 0:
        for char in text:
            if char == "!" or char == "." or char == "?":
                sentence = text[:index+1]
                if sentence[0] == " ":
                    sentence = sentence[1:]
                text = text[index+1:]
                sentences.append(sentence)
                index = 0
                continue
            index += 1
    return sentences
