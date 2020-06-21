#!/usr/bin/env python3

#https://www.w3schools.com/python/python_dictionaries.asp

#Interfaces of a gateway davice
eth1 = {
  "comments" : "V100:CDN",
  "ipv4-address" : "1.2.3.4",
  "mask-length" : 24
}
eth2 = {
 "comments" : "V200:MBN",
 "ipv4-address" : "2.3.4.5",
 "mask-length" : 16,
 "sensitivity" : "high"
}
bond1_234 = {
  "comments" : "Internet",
  "ipv4-address" : "10.2.35.4",
  "mask-length" : 8
}

#Gateways devices
FW_1 = {
  "if1" : eth1,
  "if2" : bond1_234,
  "if3" : eth2
}

for i in FW_1:
  for j in FW_1[i]:
    print("### "+i+":","")
    print(FW_1[i][j])

#print(FW_1)
#print(FW_1['if1']['comments'].lower())
