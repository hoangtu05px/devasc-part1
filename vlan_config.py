from netmiko import ConnectHandler

r1 = {
    "device_type": "cisco_ios",
    "host": "192.168.78.131",
    "username": "cisco",
    "password": "cisco",
}

vlan_cmds = []
for vlan in range(10, 21):
    vlan_cmds.append(f"vlan {vlan}")
    vlan_cmds.append(f"name VLAN_{vlan}")

print("Connecting to R1...")
net = ConnectHandler(**r1)

print("Sending VLAN config to SWITCH (telnet already opened)...")
output = net.send_config_set(vlan_cmds)
print(output)

net.disconnect()
