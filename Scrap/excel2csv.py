#!/usr/bin/env python3

#pip3 install pandas
#pip3 install openpyxl
#pip3 install xlrd
#https://pandas.pydata.org/pandas-docs/dev/user_guide/io.html#excel-files
#https://www.youtube.com/watch?v=C2O3O_GydV4

import pandas as pd

# Read xlsx file:
#df = pd.read_excel('All-networks-list.xlsx', 'Security Domains', index_col=0)
names = ['Firewall','Network','Interface','NetworkAddress','PrefixLength','']
df = pd.read_excel('All-networks-list.xlsx', 'Security Domains', index_col=0, header=None, skiprows=1, names=names)
# Write xlsx file
#df.to_excel('test.xlsx')

df.to_csv('All-networks-list.csv',header=True)
#print(df.to_csv())



'''
print(df)
print(df.head(0))             #1st row: column headers
print(df['Firewall'][101])    #print 100th cell of 'Firewall' column (starts from 0)
print(df.columns[0])        #1st column header: Firewall

#Header:  All-net-list  > net-list.csv
Firewall,               Firewall                          ok
NetworkName/DMZ/VLAN,   Network                           x
Interface,              (InterfaceAddress)                ok
DMZ/Network,            NetworkAddress                    x
PrefixLength,           PrefixLength                      ok
Notes                   PrivilegeLevel,Weight,AdminCost   rest is ok
'''
