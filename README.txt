DEVASC Part 1 – Network Automation

## Description
Cấu hình mạng cơ bản và tự động hóa bằng Python.

## VLAN
- VLAN: 10 – 20
- Cấu hình trên: SW1, SW2
- VLAN name: tùy ý

## Routing
- Routing protocol: OSPF
- Process ID: 1
- Area: 0
- Thiết bị: R1, R2
- Trạng thái neighbor: FULL

## Automation
- Sử dụng Python (Netmiko)
- Tự động cấu hình OSPF trên router

## Verification
```bash
show vlan brief
show ip ospf neighbor


