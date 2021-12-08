import os, socket, ipaddress, math, time
from termcolor import colored as c

good = c("[", 'green') + "+" + c("]", 'green')
bad = c("[", 'red') + "-" + c("]", 'red')


# Visual effects
def load():
    x = ["L", "O", "A", "D", "I", "N", "G"]
    z = ""
    time.sleep(1)
    for i in range(1, 8):
        time.sleep(0.5)
        y = "*" * i
        z = z + x[i - 1]
        print(c(y + " " + z + " " + y, 'blue'))
    time.sleep(1.5)
    print("\n" + good + c(" LOADED SUCCESSFULLY !\n", 'green'))


# Scanning for hosts !
def scan(network, prefix):
    print(good + c(" SCANNING : ", 'red') + c(network, 'green' + c(prefix, 'blue')))
    time.sleep(2)
    for host in ipaddress.ip_network(str(network) + str(prefix)):
        print(good + c(" HOST FOUND : ", 'red') + c(host, 'green'))


# Determine subnet prefix
def getPrefix(network, sub):
    print("LOADING PREFIX SETTINGS !")
    time.sleep(1)
    load()
    prefix = ""
    if str(sub) == "255.255.255.252":
        prefix = "/30"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 2), 'green'))
    elif str(sub) == "255.255.255.248":
        prefix = "/29"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 3), 'green'))
    elif str(sub) == "255.255.255.240":
        prefix = "/28"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 4), 'green'))
    elif str(sub) == "255.255.255.224":
        prefix = "/27"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 5), 'green'))
    elif str(sub) == "255.255.255.192":
        prefix = "/26"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 6), 'green'))
    elif str(sub) == "255.255.255.128":
        prefix = "/25"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 7), 'green'))
    elif str(sub) == "255.255.255.0":
        prefix = "/24"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 8), 'green'))
    elif str(sub) == "255.255.254.0":
        prefix = "/23"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 9), 'green'))
    elif str(sub) == "255.255.252.0":
        prefix = "/22"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 10), 'green'))
    elif str(sub) == "255.255.248.0":
        prefix = "/21"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 11), 'green'))
    elif str(sub) == "255.255.240.0":
        prefix = "/20"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 12), 'green'))
    elif str(sub) == "255.255.224.0":
        prefix = "/19"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 13), 'green'))
    elif str(sub) == "255.255.192.0":
        prefix = "/18"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 14), 'green'))
    elif str(sub) == "255.255.128.0":
        prefix = "/17"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 15), 'green'))
    elif str(sub) == "255.255.0.0":
        prefix = "/16"
        print(good + c(" PREFIX FOUND, NUMBER OF CLIENTS : ", 'red') + c(math.pow(2, 16), 'green'))
    elif str(sub) == "255.255.255.255":
        print("SORRY !\n" + bad + c(" ITS SEEMS LIKE YOUR HOME ALONE KID !", 'red'))
        print(bad + c(" ABORTING ! NO CLIENTS TO SEARCH FOR ! ", 'red'))
        quit()
    scan(network, prefix)


# Turning back these lists into values
def unlist(listy, mask):
    print("Getting router's IP Address !")
    time.sleep(2)
    router = ""
    for i in listy:
        if router == "":
            router = router + str(i)
        else:
            router = router + "." + str(i)
    print(good + c(" ROUTER'S IP FOUND : ", 'red') + c(router, 'green') + "\n")
    getPrefix(router, mask)


# Turn those values into lists
def listIT(ip, mask):
    ip = str(ip).split(".")
    mask1 = str(mask).split(".")
    network = []
    for i in [0,1,2,3]:
        if mask1[i] == "255" and i != 3:
            network.append(ip[i])
        elif i == 3 and mask1[i] == "255":
            network.append(1)
        else:
            network.append(0)
    unlist(network, mask)


# Storing client's IP Address and retrieve subnet mask
def getIP(operation):
    print("Getting client's IP Address and Subnet !")
    time.sleep(2)
    if operation == "Unix":
        local_ip = os.popen("hostname -I | awk '{print $1}'").read()
    elif operation == "Windows":
        local_ip = socket.gethostbyname(socket.gethostname())
    subnet = ipaddress.IPv4Network(0).netmask
    print(good + c(" IP ADDRESS FOUND : ", 'red') + c(local_ip, 'green'))
    print(good + c(" SUBNET FOUND : ", 'red') + c(subnet, 'green') + "\n")
    time.sleep(1)
    listIT(local_ip,subnet)


# Determine what operation system client is using.
def getOS():
    if os.name == "NT":
        OS = "Windows"
    elif os.name == "posix":
        OS = "Unix"
    else:
        OS = os.name
    print(good + c(f" OPERATION SYSTEM FOUND : ", 'red') + c(OS + "\n", 'green'))
    time.sleep(1)
    getIP(OS)


if __name__ == "__main__":
    try:
        print('SEARCHING FOR OPERATION SYSTEM !')
        time.sleep(2)
        getOS()
    except IOError or ValueError as err:
        print(err + " Error acquired : " + c(err, "red"))
        quit()