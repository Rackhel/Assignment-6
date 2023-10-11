#Number 1
print("This is Number 1.\n")
fname = input("Enter the file name: ")
try:
    with open(fname, "r") as file:
        for line in file:
            print(line.upper().rstrip())
except FileNotFoundError:
    print("File does not exist.")
    print("Program terminated.")









        
