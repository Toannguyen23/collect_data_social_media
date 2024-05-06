import json
import pandas as pd

with open('D:/HK_2_2023_2024/Insta/out/people.json', 'r') as file:
    data = json.loads(file.read())
    print(data)

nodes =[]
edges = []

# for person in data['id']:
#     nodes.append({'id' : person['pk_id'],
#                   'username': person['username'],
#                   'fullname': person['full_name'],
#                   'is_private': person['is_private']})

# for person_id in data['id']:
#     edges.append({
#         'source': person_id['pk'],
#         'target': person_id['id']
#     })
#Chinh lai:
for person in data:
    nodes.append({'id' : person['pk_id'],
                  'username': person['username'],
                  'fullname': person['full_name'],
                  'is_private': person['is_private']})

for person_id in data:
    edges.append({
        'source': person_id['pk'],
        'target': person_id['id']
    })
    
#luu file 
nodes_df = pd.DataFrame.from_dict(nodes)
edges_df = pd.DataFrame.from_dict(edges)
edges_dfs = edges_df.sort_values(by=['target'], ascending= False)

def save_csv(person: str):
    
    nodes_df.to_csv(f'D:/HK_2_2023_2024/Insta/out/{person}/nodes.csv', index=False, header=True)
    edges_dfs.to_csv(f'D:/HK_2_2023_2024/Insta/out/{person}/edges.csv', index=False, header=True)

save_csv('Accam')
