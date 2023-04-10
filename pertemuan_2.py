# thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon","mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon","mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon","mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon","mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon","mango"]
# print(thislist[2:])
# thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon","mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon","mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon","mango"]
# thislist[1:3] =["blackcurrant","watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2,"watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("watermelon") menambahkan di akhr
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist2 = ["blackcurrant","watermelon"]

# thislist2.extend(thislist)
# print(thislist)


#===================== UNTUK MENGHAPUS===========================
# thislist = ["apple", "banana"]
# thislist.pop(0) untuk menhapus
# print(thislist)

#thislist = ["apple", "banana"]
#thislist.clear() #menghapus semua isi dalam variabel thislist
#print(thislist)

# thisset = {"apple","banana","cherry"}
# thisset.remove("banana") sama juga menhapus hanya ini langsung sebutkan namnya
# print(thisset)
#======================================================================



# thislist = ["apple", "banana"]
# for x in thislist:
#     print(x)


# thislist = ["apple", "banana"]
# i = 0
# while i < len(thislist):
#     print(thislist[1])

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# thislist = ["apple", "banana","cherry"]
# thislist.pop(1)
# print(thislist)

# assert(thislist) == ["apple","cherry"]

# thislist.append("kiwi")

# assert(thislist) == ["apple","cherry","kiwi"]

# new_list = ['apple','apple','apple','apple',
#              'cherry','kiwi','apple','apple','cherry','kiwi','apple','apple']
# assert(thislist[4:6]) == ['cherry','kiwi']

# assert([x for x in new_list if x == 'apple']) ==[
#     'mango','kiwi','mango','kiwi']

# list1 = ['mango']
# list2 = ['apple']

#



# list1 = [1, 4, 5, 6, 2, 4]

# assert([x for x in list1 if x != 4]) == [1, 5, 6, 2]

# assert([x for x in list1 if x == 4]) == [4,4]

# list1 = [1, 4, 5, 6, 2, 4]
# list2 = list1.copy()
# list2.pop()

# print(list1, list2)

# list3 = [1, 4, 5, 6, 2, 4]


#=========OUTPUTNYA ITU X=APPLE,YELLOW=BANANA, DAN  RED ITU SISANYA KARENA PAKE BINTANG========
# fruits = ("apple","banana","cherry","strawberry","raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)
#==========================================================


# cars = {
#     'brand' : 'honda',
#     'product' : 'civic'
# }

# print(cars['brand'])

# (cars.keys())

# for key in cars.keys():
#     print(cars[key])

#     cars = {
#         'brand' : 'honda',
#         'product' : 'civic'
#     }

#     assert(list(cars.keys()[1])) == 'product'
# print(cars.values())

# print(cars.get('year',None))
# print('Tidak akan dijalankan')

# if 'year' in cars:
#     print(cars['year'])

# cars.update(
#     {
#        'year' : 2020,
#        'key2' : 2121
#     }
# ) 

# cars['year'] = 2020
# print(cars)

# cars['brand'] = 'Toyota'
# print(cars)

#def my_function(fname,lname):
    # print(fname + " refsnes")
    #return fname + lname

# result = my_function("emil", "refer")

# my_function("emil")
# my_function("tobias")
# my_function("linus")

# def my_function(*kids):
#     print(kids) sampe sini pake dalam kurunb
#     for kid in kids:
#         print(kid)sampe sini gk pake kurung + kebawah

# my_function("emil", "tobias")

# def my_function_2(child1, child2):
#     print(child2) outputnya emil doang

# my_function_2(child2="emil", child1="tobias")

# def full_name(first_name, last_name):
#     print(first_name + " " + last_name)

#     full_name(last_name="tobias", first_name="emil")

# def detail_people(**data):
#     print(data)

# detail_people(
#               nama_depan="emil",
#               nama_belakang="tobias",
#               status="bekerja")

# detail_people(nama_depan="emil",
#               nama_belakang="tobias",
#               umur=20)

# def upper_case_country(country="norway"):
#     print(country.upper())

# upper_case_country('swiss')

# def multiply_by_two(a):
#     return a * 2

# assert(multiply_by_two(3)) == 6

# def multiply_by_x(y,a = 2):
#     "if x not passed,then define the default value to 2"
#     return y * a


# assert(multiply_by_x(3)) == 6
# assert(multiply_by_x(3, 1)) == 3

# user_input = input('input dikali dengan 2 : ')
# print(multiply_by_two(int(user_input)))

# how_many_input = input('berapa kali ingin input data? ')
# i = 0
# while i < int(how_many_input):
#     user_input = input("input dikali dengan 2: " )
#     print(multiply_by_two(int(user_input)))
#     i += 1


# how_many_input = input("berapa kali ingin input data?")
# i = 0
# while True:

#     if i == 0:
#         break

#     user_input = input('input dikali dengan 2: ')
#     print(multiply_by_two(int(user_input)))
#     i += 1







#================STUDYCASE MENCARI NILAI RATA RATA DARI SISWA==================
# def avg(grades):
#     grade = 0
#     grades = grades.split(',')
#     for i in grades :
#         grade += float(i)
#     grade = grade/len(grades)
#     return grade

# how_many_input = input ("Enter the number of studends of the class : ")

# students = []

# for i in range(int(how_many_input)):
#     name = input('Enter the name : ' + str(i+1) + ':')
#     grades = input('Enter the grades ' + str(i+1) + '(comma-separated) : ')
#     students.append(
#         {
#            'nama' : name,
#            'grade' : grades,
#            'avg' : avg(grades)
#         }
#     )
#
# print()
# print("average grades : ")
# for x in students:
#     print(x['nama'], ":", x["avg"])
 #================================================================


#=====================MENGGANTI SALAH SATU DARI X===============
# x = ("apple","banana","cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y) 

# print(x)
#================================================================


#================menambahkan isi dari variabel tropical ke dalam variabel thisset========
# thisset = {"apple","banana","cherry"}
# tropical = {"pineappel","manggo","pepaya"}

# thisset.update(tropical)

# print(thisset)
#======================================================================================



#====================================================================================
# thisdict  = {
#     'brand' : 'ford',
#     'model' : 'mustang',
#     'year'  : 1964
# }

# print(thisdict) outpunya akan muncul semua dari variabel thisdict

# thisdict  = {
#     'brand' : 'ford',
#     'model' : 'mustang',
#     'year'  : 1964
# }

# print(thisdict['brand']) outpunya hanya brand saja yaitu ford

# thisdict  = {
#     'brand' : 'ford',
#     'model' : 'mustang',
#     'year'  : 1964,
#     'year'  : 2020
# }

# print(thisdict) mengganti year nya saja menjadi 2020

# thisdict  = {
#     'brand' : 'ford',
#     'electric' : False,
#     'year'  : 1964,
#     'color' : ["red","white","blue"]
# }

# print(len(thisdict)) menghitung jumlah baris yang ada di dalam variabel thisdict

# thisdict  = {
#     'brand' : 'ford',
#     'model' : 'mustang',
#     'year'  : 1964
# }

# print(type(thisdict))
#=================================================================



# thisdict = dict(name = "john", age = "36", country = "hayawang")
# print(thisdict)


# car = {
#     'brand' : 'ford',
#     'model' : 'mustang',
#     'year'  : 1964
# }

# x = car.keys()
# print(x)

# car['color'] = 'white'
# print(x)

# car = {
#     'brand' : 'ford',
#     'model' : 'mustang',
#     'year'  : 1964
# }

# x = car.values()
# print(x)

# car['year'] = 2020
# print(x)

# i = 0
# while i < 0:
#     i += 1
#     if i == 3:
#         continue
#     print(i)



  

















