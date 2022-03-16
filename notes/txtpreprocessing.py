# chr() takes a number or integer and coverts it to unicode charactre
# ord() takes unicode character and coverts it to integer

# can be used for encription

def name_student():
    name = input("what is your name: ")
    a = "my name is " + name

    b = "my name is {}".format(name)

    c = "my name is {} and i am {} years old.".format(name, 22)
    d = "my name is {0} and i am {1} years old.".format(name, 22)
    e = "my name is {1} and i am {0} years old.".format(name, 22)
    f = "my name is {0:10} and i am {1:10} years old.".format(name,
                                                              22)  # width is how big do we want field to be (num spaces)
    g = "my name is {1:^10} and i am {0:^10} years old.".format(name, 22)  # align <,>,^
    h = "my name is {1:*^10} and i am {0:*^10} years old.".format(name, 22)  # fill * fill blank width with *
    # order must be fill align width but fill will raise error without width

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)


def cost():
    dollars = 12
    cents = 7

    print("i have ${}.{:0>2}".format(dollars, cents))

    # prints i have $12.07
    money = 17.30
    print("i have {:.2f}".format(money))

### opening and closing files

# open(<filename>, <mode>)
# mode = "r" or "w"
# r = read w = write

my_file = open("data.txt", "r")
#assumes data.txt is in same folder as our python file.
# can open files anywhere on computer but have to specifify this when opening file

my_poem = open("poem.txt", "r") #creates something similar to a file object (has info about file but not actual data)

def print_file():
    my_poem = open("poem.txt", "r")
    poem = my_poem.read()
    poem= poem.replace("e", "$")
    print(poem) #<str>

def print_file_lines():
    my_poem = open("poem.txt", "r")
    for i in range(5):
       line = my_poem.readline() #double spaces lines bc each line has new lien charachter at end and print also by defaults prints new line \n
       print(line, end="")
       #or
       print(line[:-1])


def print_file_list():
    my_poem = open("poem.txt", "r")
    for line in my_poem.readlines():
        print(line[:-1])


def print_file_list_2():
    my_poem = open("poem.txt", "r")
    for line in my_poem: #same as above function bc in loop auotomatically loops through eachline but wont be a list
        print(line[:-1])

my_output = open("output.txt", "w") #if file exists in directory will replace contents of the file with whatever you write
print("hello world!", file=my_output)


poem