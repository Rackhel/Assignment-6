#Number 2
print("This is Number 2.\n")
fhand_2 = open("mbox.txt", "r")
host_name = set()
count = 0 
for line in fhand_2:
    if line.startswith("From:"):
        name1 = line.split()
        if len(name1) > 1:
                    host = name1[1]
                    username, hostname = host.split('@', 1)
                    host_name.add(hostname)
                    count += 1
                    
for hostname in host_name:
    print("Host names:", hostname)

print(f"Total {count} Hosts printed.")