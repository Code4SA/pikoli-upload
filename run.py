from __future__ import print_function
import os
import sys
from md5 import md5
from documentcloud import DocumentCloud

def hash(s):
    return md5(s).hexdigest()

print("Enter your Document Cloud Credentials")
sys.stdout.write("Username: ")
username = raw_input().strip()
sys.stdout.write("Password: ")
password = raw_input().strip()

base_uri = "https://sourceafrica.net/api/"
client = DocumentCloud(username, password, base_uri)


project = "60"
source = "SAPS"

if not os.path.exists("log"):
    os.mkdir("log")

total = 0
count = 0
for (path, _, filenames) in os.walk("saps/"):
    total += len(filenames)

for (path, _, filenames) in os.walk("saps/"):
    spath = path.split("/", 1)[1]
    logpath = os.path.join("log", spath)

    for fn in filenames:
        count += 1
        data = {"path" : spath}
        logfn = hash(os.path.join(path, fn))

        fullpath = os.path.join(path, fn)
        full_log_path = os.path.join("log", logfn)
        if os.path.exists(full_log_path):
            continue

        print("\rUploading: %s - (%d / %d)" % (fullpath, count, total))
        obj = client.documents.upload(
            fullpath, project=project, data=data, source="SAPS"
        )
        fp = open(full_log_path, "w")
        fp.write(path)
        fp.write("\n")
        fp.close()
