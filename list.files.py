import os

# #Get file list of csv's in download direcltory
basedir = '/Users/emmett/Downloads/'
dlfiles = os.listdir(basedir)
#print(type(dlfiles))
#print(dlfiles)
#
ticketnumber = str(input('Ticket Number?: '))
# #ticketnumber = str(1234)
#
# impactcsv = os.popen('ls ~/Downloads/ *{ticketnumber}* |grep impact |grep csv)
# #print(f"The CSV's found in the Download directory are :\n{allcsv}")
# print(f"-------------------")
# print(f'We are looking for {ticketnumber}.')
# for i in allcsv:
#     print(i)
tfiles = []
for i in dlfiles:
    if ticketnumber in i:
        tfiles.append(i)

for i in tfiles:
    if 'impact' in i:
        tfimpact = i
    else:
        tfbase = i



tfimpact = basedir+tfimpact
tfbase = basedir+tfbase

print(tfimpact)
print(tfbase)