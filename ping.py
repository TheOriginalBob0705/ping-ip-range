import os
from multiprocessing.pool import ThreadPool

pool_size = 5


def ping_ip(ip_add):
    response = os.popen(f"ping -n 1 {ip_add} ").read()

    if not ("Request timed out." or "unreachable") in response:
        print(response)
        f = open("ip_output.txt", "a")
        f.write(str(ip_add) + '\n')
        f.close()


with open("ip_list_test.txt") as file:
    ip_list = file.read()
    ip_list = ip_list.splitlines()

with open("ip_output.txt", "w") as file:
    pass

pool = ThreadPool(pool_size)

for ip in ip_list:
    pool.apply_async(ping_ip, (ip,))

pool.close()
pool.join()
