"""
Name: Carson Shields
lab2.py

Problem: lab 2 1 work
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
def means():
    n = eval(input("Enter numbers that are given: "))
    values = 0
    accum_rms = 0
    accum_harmonic_mean = 0
    accum_geo_mean = 1



    for i in range(n):
        values = (eval(input("Enter value: ")))

        accum_rms += values ** 2
        accum_harmonic_mean += 1/values
        accum_geo_mean = (values * accum_geo_mean)
    rms = (accum_rms / n) ** (1 / 2)
    harmonic_mean = (n / accum_harmonic_mean)
    geo_mean = (accum_geo_mean) ** (1 / n)



    print("Root-Mean-Square: ", rms, end= "\n")
    print("Harmonic Mean: ", harmonic_mean, end="\n")
    print("Geometric Mean: ", geo_mean, end="\n")