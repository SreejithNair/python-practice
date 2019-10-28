import json
import os as path

access_json = open(path.getcwd()+'\\json_work\\test.json', 'r')
read_content = json.load(access_json)
# Make list a dictionary
for question_access in read_content:
    replies_access = question_access['Attachment']
    for i in replies_access:
            print(i,"|",replies_access[i])