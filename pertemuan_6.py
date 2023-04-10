
# import time
# import math

# def calculate_time(func):

#     def inner1(*args, **kwargs):

#         begin = time.time()

#         func(*args, **kwargs)

#         end = time.time()
#         print("Time total taken in : ", func.__name__, end - begin )

#         return inner1
    
# @calculate_time
# def factorial(num):

#     time.sleep(2)
#     print(math.factorial(num))

# factorial(10)

# import requests
# from pprint import pprint

# r = requests.get('https://jsonplaceholder.typicode.com/posts/101')
# data = r.json()
# pprint(data)

# post = {
#     'Body' : 'Lorem Ipsum',
#     'title' : 'Title',
#     'userId' : 5,
#     # 'id' : 5
# }

# req = requests.post('https://jsonplaceholder.typicode.com/posts',json=post)
# print(req.json())

# update_post = post
# update_post['id'] = 5

# req = requests.put(
#     'https://jsonplaceholder.typicode.com/posts/5', json=update_post)
# print(req.json())

# def square(x): return x ** 2

# print(square(2))

print("Menghitung Luas Segitiga")
print("========================")
print()

a = int(input("Masukan Alas: "))
t = int(input("Masukan Tinggi: "))

luas = 0.5*a*t
print("Luas Segitiga Dari Alas ", a ,"dan Tinggi", t ," Adalah : " + str(luas)) 
    


