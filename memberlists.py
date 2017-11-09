import json, re, sys, os
from shutil import copyfile
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
    valid = ["20%s-%02d"%(sys.argv[1][1:], x) for x in range(1,7)]

if "h" in sys.argv[1]:
    valid = ["20%s-%02d"%(sys.argv[1][1:], x) for x in range(7,13)]

sort_lis = sorted([User(a['name'], a['date_joined'], a['lifetime']) for a in data], key=lambda lm: lm.get_name().upper())

if os.path.isfile(sys.argv[1]+".tex"):
        os.remove(sys.argv[1]+".tex")

copyfile("template.tex", sys.argv[1]+".tex")

f = open(sys.argv[1]+'.tex', 'a')


width = 35
for a in sort_lis:
    if str(a.get_date())[:7] in valid or a.get_lifetime():
        f.write("{} & {} & {} & \\\ \\hline \n".format(a.get_name(),\
                re.sub(r'T(.*)', '', str(a.get_date())),\
                str(a.get_lifetime())))

f.write("\\end{longtabu} \n \\end{document}")
f.close()
