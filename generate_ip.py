import os

f = open("ip_list.txt", 'w')

for seg2 in range(204, 209):
    for seg3 in range(0, 31):
        for seg4 in range(2, 255):
            gen_ip = f"10.{seg2}.{seg3}.{seg4}"
            print(gen_ip, file=f)
            print(f"Added ip address: {gen_ip}")
