#!/usr/bin/env python3
'''
This scripts parses through (checkpoint) configuration files and creates
a single (network-topology).cfg file that can be imported into 
diagrams.net picture to display a topology map:

Copy/Paste the output of this script to 
https://app.diagrams.net/ > Arrange > Insert > Advanced > CSV...

Location: https://github.com/aredey/AkosNetworkConnectivity
version: 0.1          author: Akos Redey               date: 2020.06.21 
'''

#Node (device and domain) fill and border colours
node_colour = "#dae8fc"
node_border_colour= "#ff0000"
node_shape = "mxgraph.networks.firewall"
domain_colour = "#dae8fc" 
domain_border_colour = "#6c8eba"
domain_shape = "ellipse"

import pprint, pdb
import os, glob, re
 
directory='Configs/'
os.chdir(directory)

########################################################################
#Iterate through the .cfg (firewall) configuration files and import
#interface info into python data structures
########################################################################
domains = ({})                            #Security Domains into a dict
gateways=({})                             #Gateway devices into a dict
node_id=100000      #node_id: arbitrary "large" integer to distinguish
                    #gateway devices from security domains
for file in glob.glob('*.cfg'):
  gateway = file.split('.')[0]
  gateways[gateway]={}                                        #gateway
  for line in open(file, 'r'):
    if re.search('interface.+comments', line):
      interface=line.split()[2]                               #interface
      domain=line.split()[4].replace('"', '')                 #domain
      domains[domain]=node_id              #add domain to domains dict
      node_id += 1
    elif re.search('interface.+ipv4', line):
      ipv4=line.split()[4]                                    #ipv4
      preflen=line.split()[6]                                 #preflen
      gateways[gateway][interface]={}
      gateways[gateway][interface]["domain"]=domain
      gateways[gateway][interface]["ipv4"]=ipv4
      gateways[gateway][interface]["preflen"]=preflen
    else:
      break
#pprint.pprint(gateways); #pdb.set_trace()
#pprint.pprint(domains)

########################################################################
#Print out the config part of the draw.io csv specification
########################################################################
print ('''# label: %node%
# style: shape=%shape%;rounded=1;fillColor=%fill%;strokeColor=%stroke%;
# namespace: csvimport-
# connect: {"from":"domains","to":"id","style":"curved=1;endArrow=none;"}
# width: auto
# height: auto
# padding: 40
# ignore: id,shape,fill,stroke,domains,gateways
# nodespacing: 40
# levelspacing: 40
# edgespacing: 40
# layout: organic
## CSV data starts below this line
id,node,fill,stroke,shape,domains,gateways''')

#Print the CSV data
##Print the gateways
node_id = 0        #small integer for the devices (smaller than domains)
prev_gw = ""
doms = ""
for gw in gateways:
  node_id += 1
  for intf in gateways[gw]:
    if gw != prev_gw:
      prev_gw == ""
      doms = ""
    for if_attr in gateways[gw][intf]:
      if if_attr == 'domain':
        dom = gateways[gw][intf]['domain']
        ref=domains[dom]
        doms += str(ref)+","
        #if_ip = gateways[gw][intf]['ipv4']      #not used at the moment
        #pref_len = gateways[gw][intf]['preflen']#not used at the moment
        prev_gw = gw
##Print the gateways from the gateways dict
  print("{},{},{},\"{}\"".format(node_id, gw, node_colour+","+node_border_colour+","+node_shape, doms.strip(',')))
##Print the domains from the domains dict
for element in domains:
  print("{},{},{}".format(domains[element], element, domain_colour+","+domain_border_colour+","+domain_shape))
