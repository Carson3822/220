def pig_latin():
    sentence = input("enter a sentence to convert tp pig latin: ")
    sentence = sentence.lower()
    sentence = sentence.split()
    pig_sentence = ""

    for word in sentence:
        pig_sentence += word[1:] + word[0] + "ay" + " "

    pig_sentence= pig_sentence.rstrip()
    print(pig_sentence)



