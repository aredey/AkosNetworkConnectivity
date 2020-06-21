#!/usr/bin/env python3
'''
This scripts parses through (checkpoint) configuration files and creates
a single (network-topology).cfg file that can be imported into 
diagrams.net picture to display a topology map.
https://app.diagrams.net/ > Arrange > Insert > Advanced > CSV...
'''
import pprint, pdb
import os, glob, re
 
directory='/home/redey/Documents/AkosNetworkConnetctions/'
#directory='/home/redey/Lappy-Documents/AkosNetworkConnetctions/'
os.chdir(directory)

#Parsing through .cfg files
# seq=0
# for file in glob.glob('*.cfg'):
  # gateway = file.split('.')[0].replace('-', '_')
  # for line in open(file, 'r'):
    # if re.search('interface.+comments', line):
      # interface=line.split()[2]
      # domain=line.split()[4].replace('"', '')
    # if re.search('interface.+ipv4-address', line):
      # interface=line.split()[2].replace('.', '_')
      # address=line.split()[4]
      # mask_length=line.split()[6]
      # seq += 1
      # #print(str(seq)+","+gateway+","+interface+","+domain+","+address+","+mask_length)
      # #id,gateway,fill,   stroke, shape,                    domains
      # 1,   Fw_1,#dae8fc,#ff0000,mxgraph.networks.firewall,"5,8,9"
      # print(str(seq)+","+gateway+","+"#dae8fc,#ff0000,mxgraph.networks.firewall"+","+domain)

seq_gwy=0             #MAX gateway devices this program can handle: 999!!!
seq_dom=1000
domains = set({})     #set
for file in glob.glob('*.cfg'):
  gateway = file.split('.')[0]                  #gateway      #FW_1
  seq_gwy +=1
  for line in open(file, 'r'):
    if re.search('interface.+comments', line):
      interface=line.split()[2]                   #interface  #eth1
      domain=line.split()[4].replace('"', '')     #domain     #Internet
      domains.add(domain)               #add domain to domains set
      seq_dom += 1
    elif re.search('interface.+ipv4', line):
      interface=line.split()[2]                   #interface  #eth3
      ipv4=line.split()[4]                        #ipv4   #100.100.100.100
      preflen=line.split()[6]                     #preflen    #24
      gws={}
      gws[gateway]={}
      gws[gateway]["seq"]=seq_gwy
      gws[gateway][interface]={}
      gws[gateway][interface]["domain"]=domain
      gws[gateway][interface]["ipv4"]=ipv4
      gws[gateway][interface]["preflen"]=preflen
      pprint.pprint(gws)
    else:
      break
    #print(line,end="")

print("\ngateways: ")
#pprint.pprint(gws)
for x in gws:
  print(gws[x])

print("\ndomains: ")
pprint.pprint(domains)
