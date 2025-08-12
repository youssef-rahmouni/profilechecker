
urls = [1, 2, 3, 4]

def sum(number):
    number = number + 1
    return number    
keyandvalue = {sum(i): i for i in urls}
for x in keyandvalue:
    print(f'Key:{x.result()} | Value:{keyandvalue[x]}')

''' 
###############

from concurrent.futures import ThreadPoolExecutor, as_completed

urls = [1,2,3,4]

def sum(number):
    number = number + 1
    return number

with ThreadPoolExecutor() as executor:
    keyandvalue = {executor.submit(sum, i): i for i in urls}
    for future in as_completed(keyandvalue):
        print(f'Key: {future.result()} | Value: {keyandvalue[future]} ')
    
###############
from concurrent.futures import ThreadPoolExecutor, as_completed

urls = [1, 2, 3, 4]

def sum(number):
    number = number + 1
    return number

with ThreadPoolExecutor() as executor:
    futures = {executor.submit(sum, i): i for i in urls}
    for future in as_completed(futures):
        print(f"Input: {futures[future]}, Output: {future.result()}")
   ''' 