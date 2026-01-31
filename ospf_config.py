from netmiko import ConnectHandler

r1 = {
    "device_type": "cisco_ios",
    "host": "192.168.78.131",   # R1 NAT
    "username": "cisco",
    "password": "cisco",
}

ospf_cmds = [
    "router ospf 1",
    "network 0.0.0.0 255.255.255.255 area 0"
]

print("Connecting to R1...")
net = ConnectHandler(**r1)
output = net.send_config_set(ospf_cmds)
print(output)
net.disconnect()
