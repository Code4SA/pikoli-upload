from __future__ import print_function
import os
import sys 
from documentcloud import DocumentCloud

print("Enter your Document Cloud Credentials")
sys.stdout.write("Username: ")
username = raw_input().strip()
sys.stdout.write("Password: ")
password = raw_input().strip()

base_uri = "https://sourceafrica.net/api/"
client = DocumentCloud(username, password, base_uri)
import pdb; pdb.set_trace()
print(client.projects.all())

