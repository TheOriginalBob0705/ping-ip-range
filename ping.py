import tkinter as tk
from tkinter import simpledialog as sd

root = tk.Tk()
root.withdraw()
ip_1 = sd.askinteger("IP Ping", "Enter first segment: [__].__.__.__", parent=root)
ip_2 = sd.askinteger(f"IP Ping", f"Enter second segment: {ip_1}.[__].__.__", parent=root)
ip_3 = sd.askinteger(f"IP Ping", f"Enter third segment: {ip_1}.{ip_2}.[__].__", parent=root)
ip_4 = sd.askinteger(f"IP Ping", f"Enter fourth segment: {ip_1}.{ip_2}.{ip_3}.[__]", parent=root)

if ip_1 is not None and ip_2 is not None and ip_3 is not None and ip_4 is not None:
    print(f"{ip_1}.{ip_2}.{ip_3}.{ip_4}")
