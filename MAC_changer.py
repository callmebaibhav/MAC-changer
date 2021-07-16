###                        ----   Made by INDIAN   ----                        ###


import subprocess

interface = raw_input("interface > ")
new_mac = raw_input("new MAC >")


print("[++] Changing MAC address of " + interface + "to" + new_mac)

subprocess.call(["ifconfig", interface, "down" ])
subprocess.call(["ifconfig", interface, "down hw ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])