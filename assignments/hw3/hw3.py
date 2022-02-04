"""
Name: Carson Shields
hw3.py

Problem: Hw 3 problems

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""


def average():
    num_grades = eval(input("How many grades will you enter?: "))
    accum_grade = 0
    for i in range(num_grades):
        accum_grade += eval(input("enter grade: "))

        i += 1

    avg_grade = accum_grade/num_grades
    print("the average grade is:", avg_grade)





def tip_jar():
    accum_donations = 0
    for i in range(5):
        accum_donations += eval(input("How much would you like to donate?: "))

        i+= 1

    print("total tips:", accum_donations)



def newton():
    num_for_eval = eval(input("what number do you want to square root?: "))
    num_times_improve = eval(input("how many times should we improve the approximation?: "))
    approx = num_for_eval
    for i in range(num_times_improve):
        approx = (approx + (num_for_eval/approx))/2

        i += 1

    print("the square root is approximately",approx)



def sequence():
    num_terms = eval(input("how many terms would you like: "))
    num = 1
    num_list = []

    while len(num_list) < (num_terms):
        num_list.append(num)
        if len(num_list) < num_terms:
            num_list.append(num)
            num += 2




    print(num_list)








def pi():
    num_terms = eval(input("how many terms in the series: "))

    answer_pi = 2

    for i in range(num_terms):
        numerator = 2 + (i // 2 * 2)
        denomanator = 1 + ((i+1) // 2 * 2)

        answer_pi = (numerator / denomanator) * answer_pi

    print("pi is approximately", answer_pi)




if __name__ == '__main__':
    pass
