host_file = "/etc/hosts"
redirect = "127.0.0.1"

blocked = ["www.facebook.com", "www.makemytrip.com", "www.reddit.com"]

block = 0

if block:
    print("Try visiting one of the following sites")
    print(blocked)

    with open(host_file, "r+") as file:
        content = file.read()
        for site in blocked:
            if site in content:
                pass
            else:
                file.write(redirect+" "+site+"\n")
else:
    print("Unblocked all the sites")

    with open(host_file, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for lines in content:
            if not any(site in lines for site in blocked):
                file.write(lines)
            file.truncate()
