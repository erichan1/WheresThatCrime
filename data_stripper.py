import csv

if __name__ == '__main__':
    fp = input("What is the input path? ")
    op = input("What is the output path? ")
    output_file = open(op, 'w')
    output_file.writelines("Date,Location\n")
    with open(fp, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            output_file.write(row['Date'] + " " + row['Location'] + "\n")

    output_file.close()


    