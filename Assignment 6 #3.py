#Number 3
print("This is Number 3.\n")
total = 0.0
count = 0

try:
    file_name = input("Enter a file name: ")
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                try:
                    number = float(line.split(":")[1])
                    total += number
                    count += 1
                except ValueError:
                    pass

    average = total / count
    print("Total:", total)
    print("Count:", count)
    print("Average spam confidence:", average)

except FileNotFoundError:
    print("The file cannot be opened:", file_name)

