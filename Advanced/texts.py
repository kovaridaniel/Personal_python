def Sentences(text):
    sentences = []
    while len(text) > 0:
        partitioned = text.partition('!')
        sentences.append(partitioned[0] + partitioned[1])
        remaining = partitioned[2]
        if len(remaining) > 0:
            if remaining[0] == " ":
                text = remaining[1:]
        else:
            text = remaining
    return sentences

# print(Sentences("Have a good day!"))
# print(Sentences("Good day to you! Have a good day!"))
