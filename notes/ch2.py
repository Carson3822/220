print("hello, world")
print("hello", "world")
variable = "carson"
print("hello", variable)

print("hello\nworld")
print("hello\tworld")

print("hello, world!", end= "\n")

print("hello, world!", end= "@@@@@")

print("hello, world!")
print("good to see you")


print("hello, world!", end=" ")
print("good to see you")


name = input("hello!\nenter your name: ")
print("good to see you", name)

#name, age = eval(input("hello!\nenter your name and age: "))
#print("good to see you", name, "you are", age, "years old")


for i in [1,2,3,4]:
    print(i)

x = [1,2,3,4]
for i in x:
    print(i)
#print(i) because out side of the loop it will give name error as variable i disapears after loop ends

#y = []
#for i in range(x):
    #y += x[i]
    #return(y)


for i in range(10):
    print(i, end=" ")


#def principal_value(p, IR, years):
    #fp = []
principal = eval(input("enter the starting balance: "))
APR = eval(input("enter the IR: "))

for i in range(10):

    principal = principal * (1+APR)

print("your new balance after 10 years is" principal)


