import os

with open("ip_list_test.txt") as file:
    ip_list = file.read()
    ip_list = ip_list.splitlines()
    print(f" {ip_list}  \n")

with open("ip_output.txt", "w") as file:
    pass

# ping for each ip in the file
for ip in ip_list:
    # pinging each IP address 4 times
    response = os.popen(f"ping -n 1 {ip} ").read()

    # save some ping output details to output file
    if not ("Request timed out." or "unreachable") in response:
        print(response)
        f = open("ip_output.txt", "a")
        f.write(str(ip) + '\n')
        f.close()
        # print output file to screen

with open("ip_output.txt") as file:
    output = file.read()
    f.close()
    print(output)
