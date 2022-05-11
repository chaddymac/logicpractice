import csv

# O(n) time and space
# Only works if the input is sorted
def part_b():
    filename = "testfile.csv"
    with open(filename, "r") as csvfile:
        datareader = csv.reader(csvfile)
        next(datareader)  # remove header row
        for i, row in enumerate(datareader):
            if (
                int(row[0].replace(",", "")) != i + 1
                and int(row[1].replace(",", "")) != i + 1
            ):
                print(f"{i+1} is missing from both")
                break


part_b()
