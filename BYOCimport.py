import array, csv, os

class device(object):
    def __init__(self, date, lastname, firstname, gradyear, device, mac, comments, permission, dateadded):
        self.date = date
        self.lastname=lastname
        self.firstname=firstname
        self.gradyear=gradyear
        self.device=device
        self.mac=mac
        self.comments=comments
        self.permission=permission
        self.dateadded=dateadded

byoc=[]


with open('/Users/macadmin/Downloads/TECH DEPT BYOC  - Sheet1.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        this_instance=device(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        byoc.append(this_instance)

f = open('/Users/macadmin/desktop/python projects/BYOC IMPORT/byocimport.txt', 'w+')
for x in range(1,len(byoc)):
	if byoc[x].dateadded == '':
         f.write('config macfilter add ')
         f.write(byoc[x].mac)
         f.write(' 8 byoc-phs \"')
         f.write(byoc[x].gradyear)
         f.write(' ')
         f.write(byoc[x].firstname)
         f.write(' ')
         f.write(byoc[x].lastname)
         f.write(' ')
         f.write(byoc[x].device)
         f.write('\"')
         f.write('\n')
f.close()
os.remove("/Users/macadmin/Downloads/TECH DEPT BYOC  - Sheet1.csv")
