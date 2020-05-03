import pandas
import csv

# import pandas
# df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
# print(df)

impact = pandas.read_csv('impacted.csv', index_col='_time', parse_dates=['_time'])
# print(impact)

baseline = pandas.read_csv('baseline.csv', index_col='_time', parse_dates=['_time'])
# print(baseline)

# Get the 2 values for the betplacement and for the turnover in the impact file.
totalibet = 0
with open('impacted.csv', 'r') as f:
  next(f) #skips the first row
  for row in csv.reader(f):
    totalibet += float(row[1])
  print('The total betplacement in the impacted sample is {}'.format(totalibet))

totalito = 0
with open('impacted.csv', 'r') as f:
  next(f) #skips the first row
  for row in csv.reader(f):
    totalito += float(row[2])
  print('The total betplacement in the impacted sample is {}'.format("%.2f" % totalito))

#Get the 2 values for the betplacement and the turnover in the baseline file.
totalbbet = 0
with open('baseline.csv', 'r') as f:
  next(f) #skips the first row
  for row in csv.reader(f):
    totalbbet += float(row[1])
  print('The total betplacement in the baseline sample is {}'.format(totalbbet))

totalbto = 0
with open('baseline.csv', 'r') as f:
  next(f) #skips the first row
  for row in csv.reader(f):
    totalbto += float(row[2])
  print('The total betplacement in the baseline sample is {}'.format("%.2f" % totalbto))

# get the difference
print(f'The difference in betplacement is: {totalbbet - totalibet}')
print(f'The difference in turnover is: {totalbto - totalito}')



