#!/usr/bin/env python3

#pip3 install pandas
#pip3 install openpyxl
#pip3 install xlrd

#https://pandas.pydata.org/pandas-docs/dev/user_guide/io.html#excel-files
#https://www.youtube.com/watch?v=C2O3O_GydV4
#https://stackoverflow.com/questions/59897799/remove-leading-comma-in-header-when-using-pandas-to-csv

input_xlsx_file = 'All-networks-list.xlsx'
output_csv_file = 'All-networks-list.csv'

import pandas as pd

# Read xlsx file:
names = ['Firewall','Network','Interface','NetworkAddress','PrefixLength','']
df = pd.read_excel(input_xlsx_file, 
                    'Security Domains', 
                    index_col=None, 
                    header=None, 
                    skiprows=1, 
                    names=names
                    )

# Write xlsx file
with open(output_csv_file, 'w') as file: #couldn't get rid of the leading comma
 [file.write(h+",") for h in names if names]
 file.write("\n")
print()
df.to_csv(output_csv_file,
          header=None,
          mode='a')
print(df.to_csv(header=None))
