"""

Name: Carson Shields
lab7.py

Problem: wieghted average
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

def weighted_average(in_file_name, out_file_name):

    file_object = open(in_file_name, 'r')
    file_object_out = open(out_file_name, 'w')
    file_lines = file_object.readlines()

    class_avg = 0
    valid_stud = 0
    class_avg_acum = 0
    for line in file_lines:
        line = line.split(":")
        avg = 0
        weight_acum = 0
        wg = line[1].split()

        for i in range(len(wg)):
            if i % 2 == 0:
                weight_acum += int(wg[i])
                weight = int(wg[i])/100

            elif i % 2 == 1:
                grade = int(wg[i])
                avg += grade * weight

        if weight_acum == 100:
            file_object_out.write(f"{line[0]} average: {avg:.1f}\n")
            class_avg_acum += avg
            valid_stud += 1

        elif weight_acum > 100:
            file_object_out.write(f"{line[0]} average: Error: the weights are greater than 100\n")
            avg = 0

        else:
            file_object_out.write(f"{line[0]} average: Error: the weights are less than 100\n")
            avg = 0

    class_avg = class_avg_acum / valid_stud

    file_object_out.write(f"Class average: {class_avg:.1f}")

    file_object_out.close()
    file_object.close()
