#Number 1
fhand = open("writefile.txt", "w")
for i in range(1, 11):
    data = "Line number : %d\n" % i
    fhand.write(data)
fhand.close()