import array, csv, os, telnetlib, getpass, time, datetime

#init variables
byoc=[]

#init class of BYOC device
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

#initialize log with current timestamp
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
log = open('/Users/macadmin/BYOCsync/log_byoc_sync.txt', 'a+')
log.write('---------------- ')
log.write(st)
log.write(' ----------------\n')

#start telnet session
user = raw_input("User: ")
password = getpass.getpass()

#read byoc export from google

with open('/Volumes/DATA/downloads/TECH DEPT BYOC  - Sheet1.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        this_instance=device(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        byoc.append(this_instance)

q = open('/Users/macadmin/BYOCsync/byocimport.txt', 'w+')

for x in range(0,len(byoc)):
    '''
    tn = telnetlib.Telnet('10.10.3.16')
    tn.read_until("User: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password:")
        tn.write(password + "\n")
        '''
    if byoc[x].dateadded == '' and byoc[x].permission == "Yes" :
        s = 'config macfilter add '
        s += byoc[x].mac
        s += ' 8 byoc-phs \"' 
        s += byoc[x].gradyear 
        s += ' ' 
        s += byoc[x].firstname 
        s += ' ' 
        s += byoc[x].lastname 
        s += ' ' 
        s += byoc[x].device 
        s += '\"' 
        s += '\n' 
        q.write(s + '\n')
        log.write(s + '\n')
        '''tn.write(s + '\n')
tn.write("save config \n")
tn.write("y")
tn.write("logout \n")'''
q.close()
log.close()
os.remove("/Volumes/DATA/downloads/TECH DEPT BYOC  - Sheet1.csv")



