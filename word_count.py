def word_count(sentence):
    words = sentence.split()
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

sentence = "apple orange banana apple orange apple"
print("Word Count:", word_count(sentence))