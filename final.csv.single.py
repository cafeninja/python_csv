####Single Dataset with _some_ imacted samples####

import os
import pandas as pd
import numpy as np

# #Get file list of csv's in download direcltory
basedir = '/Users/emmett/Downloads/'
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

###  start to do math.

# average the first 3 rows per column.
rowcount = len(dfi)
# print(f'This file has {rowcount} rows.')

columnsi = list(dfi)
# print(columnsi)

bpdelta = 0
todelta = 0
for col in columnsi:
	# print(f'Average of {col} is: {dfi[col].mean()}')
	sample = 0
	bcavg = 0
	bdelta = 0
	bcount = 0
	badsum = 0
	bsum = 0
	for i in range(0, 3):
		sample += dfi[col][i]
	for i in range(rowcount-3, rowcount):
		sample += dfi[col][i]
	bcavg = sample / 6
	bmin = int(bcavg * .85)
	# bad sample count
	bsum = dfi[col] < bmin
	bcount = sum(bsum)

	# sum bad samples
	bsum = dfi[col] < bmin
	bcount = sum(bsum)
	#print(f'Bad sample sum: {bsum}')
	colsum = dfi[col].tolist()
	for i in colsum:
		if i <= bmin:
			badsum += i

	#badsum = np.sum(dfi[col] <= bmin)
	# (bad sample count * average) - bad sum
	bdelta = bcount * bcavg - badsum

	if 'Placed' in col:
		bpdelta += bdelta
	else:
		todelta += bdelta
	# Add delta to running total variable for the column types.
	#bpdelta += bdelta
	#print block
	print('---------------')
	print(f'Baseline average for {col}: {bcavg}')
	print(f'Number of below average samples is: {bcount}')
	print(f'Sum of those {bcount} samples: {badsum}')
	print(f'Delta from below average samples: {round(bdelta, 2)}')
	print(f'-----------------')
	#print(f'Count of bad samples: {bcount}')
# for i in dfi['Placed bets: GameIncCasino']:
# 	print(f'value of row {i}')
print(f'Total Betplacement drop was: {bpdelta}')
print(f'Total Turnover drop was {round(todelta, 2)}')
