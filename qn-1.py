storage=[]    
def Owner():
     size=int(input('ENter the number of new items'))
     for i in range(size):
        item=input('Enter the item')
        storage.append(item)
     print(storage)   

def client():
    print(storage)
    req=input('What item do you want to buy')
    for i in storage:
        if(i==req):
            storage.remove(req)
            print(storage)

for i in range(2):
    person=input('Who are you?') 
    if(person=='owner'):
        Owner()
    if(person=='client'):
        client()