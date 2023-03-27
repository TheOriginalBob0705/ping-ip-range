# PING IPs

Ping IP addresses from a text file

## Instructions:
1. Use `generate_ip.py` to generate a list of IP addresses, edit the for loops to change the range of addresses generated
2. Run script
3. Use `ping.py` to ping the addresses from the generated file
4. The output of valid IPs (those that return a ping request) are placed into a file called `ip_output.txt`

## Bugs/Issues:
- Ping requests won't be returned if ICMP packets are blocked on the endpoint
