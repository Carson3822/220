"""
Name: Carson Shields
lab3.py

Problem: traffic
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

def traffic():
    print("how many roads were serveyed?:\t")
    num_roads_serv = eval(input(" "))
    total_cars = 0


    for i in range(num_roads_serv):

        print("how many days was road", i+1, "serveyed?:\t")
        num_days_serv = eval(input(" "))

        print()
        num_cars_tot_day = 0
        avg_cars_road = 0

        for j in range(num_days_serv):

            print("how many vehicles used road", j+1," each day?:\t")
            num_cars_day = eval(input(" "))
            num_cars_tot_day += num_cars_day
            total_cars += num_cars_day

        avg_num_cars = num_cars_tot_day/(num_days_serv)


        print("road", i+1 , "average number of vehicles per day:\t", avg_num_cars)

    print("total number of vehicles on all roads:\t\t", total_cars)

    print("average number of vehicles per road:\t\t", (total_cars/num_roads_serv))