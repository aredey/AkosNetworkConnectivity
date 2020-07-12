#!/usr/bin/env python3
'''
This scripts reads in a network (security domains - IP networks) list 
file and an IP address (on the command line) and outputs the associated
security domain

Location: https://github.com/aredey/AkosNetworkConnectivity
version: 0.1          author: Akos Redey               date: 2020.07.05
'''
import pprint
import argparse
import csv
import netaddr  #sudo pip3 install netaddr


########################################################################
#Command line info gathering: 
config_directory = 'Configs/'                 #default for *.cfg
network_list_csv = 'Configs/network-list.csv' #default is network-list.csv

parser = argparse.ArgumentParser(description='Mapping IP address(es) to \
        Networks/Security Domains')
parser.add_argument('ip_addr', type=str, help='Source or "the" IP address')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet',   action='store_true', help='Display minimal information')
group.add_argument('-v', '--verbose', action='store_true', help='Chatty information display')
parser.add_argument('-d','--dst_addr', type=str, metavar='', help='Destination IP address')
parser.add_argument('-a','--all', action='store_true', help='Print all matching domains not only the longest prefix')
#parser.add_argument('-c','--cfg_dir',type=str, metavar='', help='Directory containg *.cfg files')
parser.add_argument('-n','--net_list',type=str, metavar='', help='Network list .csv file')
args = parser.parse_args()

source = args.ip_addr
destination = args.dst_addr
#if args.cfg_dir:
#  config_directory = args.cfg_dir
if args.net_list:
  network_list_csv = args.net_list

if args.quiet:
#  print(source)
#  print(destination)
#  print(config_directory)
#  print(network_list_csv)
  pass
elif args.verbose:
  print("### Input parameters/info:")
  print("[Source] IP:                           {}".format(source))
  print("Destination IP:                        {}".format(destination))
  #print("Location of *.cfg configuration files: {}".format(config_directory))
  print("Network definition csv file:           {}".format(network_list_csv))
#else:                                     #default command lin display
#  print("source:           {}".format(source))
#  print("destination:      {}".format(destination))
#  print("config_directory: {}".format(config_directory))
#  print("network_list_csv: {}".format(network_list_csv))

########################################################################
#Importing the .csv network definition file and get the IP address from 
#the command line and print out the longest match network and associated
#domain where the IP address belongs
domains = ({})
with open(network_list_csv, 'r') as csvfile:
  records = csv.DictReader(csvfile)
  for row in records:
    dom = row['Network']
    net_address = row['NetworkAddress']+"/"+row['PrefixLength']
    try:
      domains[dom]
    except KeyError:
      domains[dom] = set()
    domains[dom].add(net_address)

if args.verbose:
  print("### Domains and constituent networks:")
  for doms, nets in domains.items():
    #print(doms, nets)
    print(doms,":")
    for n in nets:
      print("\t",n)

########################################################################
# Display network address and domain for matches
def match_network(ip_address):
  for sec_domain, nets in domains.items():
    for ip_network in nets:
      if netaddr.IPAddress(ip_address) in netaddr.IPNetwork(ip_network):
        if args.all:
          if args.quiet:
            print(sec_domain)
          else:
            print('"{}" is a host on "{}" that is part of the "{}" domain'.format(ip_address, ip_network, sec_domain))
        else: #no --all so only print the last longest prefix length match
          longest_ip_network = ip_network
          longest_sec_domain = sec_domain
  if not args.all:
    if args.quiet:
      print(longest_sec_domain)
    else:
      print('"{}" is a host on "{}" that is part of the "{}" domain'.format(ip_address, ip_network, sec_domain))
          

if destination:
  match_network(source)
  match_network(destination)
else:
  match_network(source)
  
