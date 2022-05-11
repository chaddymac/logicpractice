import csv

f = open("testfile2.csv", mode="w")
employee_writer = csv.writer(f, delimiter=",")


with open("testfile.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        row[0] = row[0].replace(",", "")
        row[1] = row[1].replace(",", "")
        employee_writer.writerow(row)
