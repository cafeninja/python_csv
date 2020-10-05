####Single Dataset with _some_ imacted samples####

import os
import pandas as pd
import numpy as np

# #Get file list of csv's in download direcltory
basedir = 'C:/Users/emst/Downloads/'
dlfiles = os.listdir(basedir)

print(f'File should be in the download folder.')
print(f'File name should be in the schema "INC00000.impact.csv".')
ticketnumber = str(input('Ticket Number?: '))
#
#  for test will complete the variable by hand
tfiles = []
for i in dlfiles:
    if ticketnumber in i:
        tfiles.append(i)

for i in tfiles:
    if 'impact' in i:
        tfimpact = i
    else:
        tfbase = i

print(f'We will be using the file: {tfimpact}')
tfimpact = basedir+tfimpact
dfi = pd.read_csv (tfimpact, index_col='_time', parse_dates=['_time'])

### Trouble shooting
#print(f'Data shape: {dfi.shape}')

#print(f'Number of null cells: {dfi.isnull()}')

### Make null fields = NaN
dfi = dfi.fillna("0")
# check if any = True
print(f'Number of null cells: {dfi.isnull()}')
### Make all NaN = 0
# print(dfi)