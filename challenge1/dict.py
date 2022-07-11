#create a nested dictionary

data = {
    'student 1': {'Name': 'bobby', 'id': 1, 'Age': '20'},
    'student 2': {'Name': 'tom', 'id': 2, 'Age': '20'},
    'student 3': {'Name': 'jerry', 'id': 3, 'Age': '20'}
}

for i in data:
    print(i)
    # print(data[i])
    # print(data[i].get('id'))
    # print(data[i].keys())
    # print(data[i].values())

for i, j in data.items():
    print(i, j)