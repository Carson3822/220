"""
Name: Carson Shields
hw5.py

Problem: Hw 5 problems

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""


def name_reverse():
    name_s = input("enter a name first last: ")

    name = name_s.split()

    name[-1] = name[-1] + ","
    out_names = name[-1] + " " + name[0]

    print(out_names)


def company_name():
    domain_name = input("enter domain name: ")

    parts = domain_name.split(".")

    print(parts[1])


def initials():
    num_students = eval(input("how many students in the class?: "))

    for student in range(num_students):
        inital = ""
        student_name = input("what is the name of student {}?:".format(student+1))
        student_name = student_name.split()

        for j in student_name:
            inital += j[0]

        print(inital)


def names():

    inpt = input("enter a list of names: ")
    lst_names = inpt.split(", ")
    print(lst_names)
    init = ""
    for i in lst_names:
        i = i.split()
        for j in i:
            init += j[0]
        init += " "

    print(init)


def thirds():
    num_sentences = eval(input("enter the number of sentences: "))
    sents = []

    for i in range(num_sentences):
        sentence = input("enter sentence {}:".format(i+1))

        sents.append(sentence)

    for sentence in sents:
        print(sentence[::3])


def word_average():
    sentence = input("enter a sentence: ")
    sentence = sentence.split()
    print(sentence)
    accum_sum = 0
    num_words = 0

    for word in sentence:
        accum_sum += (len(word))
        num_words += 1

    average = accum_sum / num_words
    print(average)

def pig_latin():
    sentence = input("enter a sentence to convert tp pig latin: ")
    sentence = sentence.lower()
    sentence = sentence.split()
    pig_sentence = ""

    for word in sentence:
        pig_sentence += word[1:] + word[0] + "ay" + " "

    pig_sentence = pig_sentence.rstrip()
    print(pig_sentence)

if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
