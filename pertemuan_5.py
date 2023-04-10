import datetime

# x = datetime.datetime.now()
# x = datetime.datetime.now()
# print(x)
# print(type(x))
# print(x.year)
# print(x.strftime("%d/%m/%Y"))
# print(x.strftime("%m"))
# print(x.strftime("%Y"))

# array = [5,78,2,0]

# assert(min(array)) == 0

# assert(max(array)) == 78

# assert(pow(5,5)) == 3125

# try:
#     f = open("demofile.txt")
#     try:
#         f.write("Lorum Ipsum")
#     except:
#         print("Somethinh went wrong when writing to the file")
#     finally:
#         f.close()
# except:
#     print("Something went wrong when opening the file")

# try:
#     print(x)
# except:
#     print("Something  when wrong")
# finally:
#     print("The'try except' is finished")

import json


# x = {"Name": "John", "Age": "30", "city":"Nweyork"}

# y = json.loads(x)

# print(y["Age"])

# x = {"Name": "John", 
#      "Age": "30", 
#      "city":"Newyork"}

# y = json.dumps(x)

# print(y)

# f = open("demofile3.txt", "w")
# f.write("Now more file has more content!")
# f.close()

# f = open("demofile3.txt", "r")
# print(f.read())
# # print(f.readline())

# # f.close()
# import os
# os.remove("demofile.txt")

f = open("json_read.txt")

json_string = f.read()

print(json_string)

json_dict = json.loads(json_string)
print(json_dict)
print(type(json_dict))
print(json_dict['name'])

users = [
    {
      'email' 
    }
]



 
