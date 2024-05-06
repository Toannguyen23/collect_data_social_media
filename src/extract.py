import json
import re
import base64
import os

def extract_following(data) -> list:
    friendship_api_url = r'https://www.instagram.com/api/v1/friendships/.*/following'
    contents = [entry['response']['content'] for entry in data['log']['entries']
         if re.match(friendship_api_url, entry['request']['url'])]
    
    #trich xuat tu contents
    users=[]
    for content in contents:
        if 'text' not in content:
            continue
        text = content['text']
        if 'encoding' in content:
            encoding = content['encoding']
            if encoding == 'base64':
                decodedBytes = base64.b64decode(text)
                decodeStr = str(decodedBytes,'utf-8')
                user_json = json.loads(decodeStr)
                users.extend(user_json['users'])
        else:
            user_json = json.loads(text)
            users.extend(user_json['users'])
    return users

def extract_person(person: str):
   
    with open(f'D:/HK_2_2023_2024/Insta/data/{person}/following.har', 'r', errors='ignore') as file:
        data = json.loads(file.read())
        
    users = extract_following(data)
    #them vao
    with open('D:/HK_2_2023_2024/Insta/out/people.json', 'w') as f:
        f.write(json.dumps(users))  
   
    # return users
        
def extract_all():
    persons = os.listdir('D:/HK_2_2023_2024/Insta/data')
    users = {}
    for person in persons:
        users['id'] = extract_person(person)
    
    with open('D:/HK_2_2023_2024/Insta/out/people.json', 'w') as f:
        f.write(json.dumps(users))  




#chinh lai people.json
extract_person("Accam")
