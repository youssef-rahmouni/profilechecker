
urls = [1, 2, 3, 4]

def sum(number):
    number = number + 1
    return number    
keyandvalue = {sum(i): i for i in urls}
for x in keyandvalue:
    print(f'Key:{x.result()} | Value:{keyandvalue[x]}')
