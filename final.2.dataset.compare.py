import pandas as pd
import os

########### Select Files ###################################

# #Get file list of csv's in download direcltory
basedir = '/Users/emmett/Downloads/'
dlfiles = os.listdir(basedir)
#print(type(dlfiles))
#print(dlfiles)
#
print(f'For this script to work, you need two CSV files.')
print(f'Use the naming schema "INC000000.impacted.csv" and "INC000000.baseline.csv"')
ticketnumber = str(input('Ticket Number?: '))
#

tfiles = []
for i in dlfiles:
    if ticketnumber in i:
        tfiles.append(i)

###### Add logic for gracefull exit if two files aren't found.

for i in tfiles:
    if 'impact' in i:
        tfimpact = i
    else:
        tfbase = i

###### Add logic for gracefull exit if impacted and base files aren't found.


tfimpact = basedir+tfimpact
tfbase = basedir+tfbase

# print(tfimpact)
# print(tfbase)
########################################################

dfi = pd.read_csv (tfimpact, index_col='_time', parse_dates=['_time'])
dfb = pd.read_csv (tfbase, index_col='_time', parse_dates=['_time'])
#print (df)
columnsi = list(dfi)
# print(columnsi)
columnsb = list(dfb)
# print(columnsb)


############GET SUM OF IMPACTED COLUMNS#####################
# Get the sum of all columns which have "placed" in the column title.
bpsumi = 0
for i in columnsi:
	if 'Placed' in i:
		bpsumi += dfi[i].sum()

#Get the sum of all the columns which have "amount" in the columntitle.
tosumi = 0
for i in columnsi:
	if 'amount' in i:
		tosumi += dfi[i].sum()

#print block
print(f'Sum of all Bets Placed in impacted sample: {bpsumi}')
print(f'Sum of all Turnover in impacted sample: {"%.2f" % tosumi}')
print('-------------------')

############GET SUM OF BASELINE COLUMNS#####################
# Get the sum of all columns which have "placed" in the column title.
bpsumb = 0
for i in columnsb:
	if 'Placed' in i:
		bpsumb += dfb[i].sum()

#Get the sum of all the columns which have "amount" in the columntitle.
tosumb = 0
for i in columnsb:
	if 'amount' in i:
		tosumb += dfb[i].sum()

#print block
print(f'Sum of all Bets Placed in baseline sample: {bpsumb}')
print(f'Sum of all Turnover in baseline sample: {"%.2f" % tosumb}')
print('-------------------')

######## Print SUMMARY ########
print(f'The difference in Betplacement was: {bpsumb-bpsumi}')
print(f'The difference in Turnover was: {"%.2f" % (tosumb-tosumi)}')
####################ABOVE IS WORKING########################


##Examples

# # block 1 - simple stats
# mean1 = df['Salary'].mean()
# sum1 = df['Salary'].sum()
# max1 = df['Salary'].max()
# min1 = df['Salary'].min()
# count1 = df['Salary'].count()
# median1 = df['Salary'].median() 
# std1 = df['Salary'].std() 
# var1 = df['Salary'].var()  

# # block 2 - group by
# groupby_sum1 = df.groupby(['Country']).sum() 
# groupby_count1 = df.groupby(['Country']).count()

# # print block 1
# print ('Mean salary: ' + str(mean1))
# print ('Sum of salaries: ' + str(sum1))
# print ('Max salary: ' + str(max1))
# print ('Min salary: ' + str(min1))
# print ('Count of salaries: ' + str(count1))
# print ('Median salary: ' + str(median1))
# print ('Std of salaries: ' + str(std1))
# print ('Var of salaries: ' + str(var1))

# # print block 2
# print ('Sum of values, grouped by the Country: ' + str(groupby_sum1))
# print ('Count of values, grouped by the Country: ' + str(groupby_count1))