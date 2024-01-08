import json

data_holder = []

def read():
    global data_holder
    try:
        with open('data.json','r') as fobj:
            data_holder = json.load(fobj)
    except:
        data_holder = []

def write():
    while True:
        todo = input("Enter the Todo: ")
        if todo == "quit":
            break
        else:
            data = {
                'todo': todo,
                'done': False
            }
            data_holder.append(data)
        with open('data.json','w') as fobj:
            json.dump(data_holder,fobj,indent=2)
        print("done")

def marktodo(mktodo):
    todo_found = False
    for i in data_holder:
        keylst = list(i.values())
        if mktodo in keylst:
            todo_found = True
            break
    if todo_found:
        return 'yes'
    else:
        return 'nah'