import json, re, sys
from api import CybApi

from settings import api_url, api_client_id, \
        api_client_secret, api_password, api_username

class User(object):
    def __init__(self, name, date, lifetime):
        self.name = name
        self.date = date
        self.lifetime = lifetime
    def get_name(self):
        return self.name
    def get_date(self):
        return self.date
    def get_lifetime(self):
        return self.lifetime

if not len(sys.argv) is 2:
    print("Usage:\n$ python "+sys.argv[0]+" \"<semester>\"")
    exit()

api = CybApi(
        api_username, api_password,
        api_client_id, api_client_secret
        )

data = api.get_members()

valid = []
if "v" in sys.argv[1]:
    for x in range(1,7):
        valid.append("20"+sys.argv[1][1:]+"-0"+str(x))

if "h" in sys.argv[1]:
    valid = ["20%s-%02d"%(sys.argv[1][1:], x) for x in range(1,7)]
'''
    for x in range(7,13):
        if x > 9:
            valid.append("20"+sys.argv[1][1:]+"-"+str(x))
        else:
            valid.append("20"+sys.argv[1][1:]+"-0"+str(x))
            '''
lis = []
for a in data:
    tmp = User(a['name'], a['date_joined'], a['lifetime'])
    lis.append(tmp)

sort_lis = sorted(lis, key=lambda lm: lm.get_name())

width = 35
print("{} | {} | {}".format("Name".ljust(width), "Date".ljust(width-20), "Lifetime".ljust(width)))
print("")
for a in sort_lis:
    if str(a.get_date())[:7] in valid or a.get_lifetime():
        print("{} | {} | {}".format(a.get_name().ljust(width),\
                re.sub(r'T(.*)', '', str(a.get_date())).ljust(width-20),\
                str(a.get_lifetime()).ljust(width)))
