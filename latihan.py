#print('hello, world')

#a = 6
#b = 5
#if a == 5:
    #print('sama')
#else:
    #print('tidak sama')

#print(str(1))
#print(int("3"))
#print(float(3))

#x = 5
#y = "john"
#print(type(x))
#print(type(y))

#x,y,z = "orange", "banana", "cherry"
#print(x)
#print(y)
#print(z)

#fruits = ["apple", "banana", "cherry"]
#x,y,z = fruits
#print(x)
#print(y)
#print(z)

#x = "python"
#y = "is"
#z = "awesome"
#print(x,y,z) ini pake spasi
#print(x+y+z) outputnya jadi nggak pake spasi

#x = 5
#y = 10
#print(x + y)

#x = 5
#y = 10
#print(x,y)

#x = "awesome"
#def myfunc():
    #print("python is " + x)
#myfunc()

#functional scope
#x = "awesome"
#def myfunc():
    #x = "fantastic"
    #print("python is " + x)
#myfunc()

#for x in "banana":
 #   print(x)

#a = "hello, world!"
#print(len(a))


#===========Mengecek sebuah kata dalam variabel ada atau tidaknya===========
#txt = "the best things in life are free!" //akan true jika yang di print itu ada dalam function
#print("best" in txt)

# txt = "the best things in life are free!"
# if "free" in txt:
#     print("yes, 'free' is present.")

#txt = "the best things in life are free!" //akan true jika yang di print tidak ada dalam function
#print("exvensive" not in txt)

# txt = "the best things in life are free!"
# if "exvensive" not in txt:
#     print("NO, 'exvensive' is NOT ")
#================================================================




#========================================================
# a = "Hello World" 
# print (a.lower()) agar hurufnya jadi kecil,KALO PAKE UPPER JADI BESAR

#a = "hello, world!"
#print(a.upper())
 
#a = " Hello, World!"
#print(a.split("!"))

# a = "Hello World" 
# print (a.strip()) 

# a = "Hello World" 
# print (a.replace("H", "J")) //mengganti h menjadi j

# b = "hello world" outpunya muncul dari hurf 2 sampai 6 
# print(b[2:6])

# b = "hello world" 
# print(b[:6]) outputnya dari 0 sampai 6

# b = "hello world" 
# print(b[2:]) outputnya dari 2 sampai selesai

# b = "hello world" 
# print(b[-5:-2])  outpunta dari kanan dulu
#==========================================================



#==========================================================
# age = "18"
# txt = "my name is john,and im ()"

# print(txt.format(age))

# age = 18
# txt = "my name is john,and im " + age

# print(txt)
#==========================================================



#buah = ["apple","banana","cherry"]
#print(buah[1])


# def sum_int_or_str(a,b):
#     return int(a) + int(b) 

# assert(sum_int_or_str(1, '2')) == 3
# assert(sum_int_or_str(2, 2)) == 4

# def get_second_character(a):
#     if len(a) > 1:
#         return a[1]
#     else:
#         return 0

#     "get second character, if only 1 character return 0"

# assert(get_second_character("ab")) == "b"
# assert(get_second_character("a")) == 0

# car = {
#     'brand': 'toyota',
#     'year' : 2022
# }

# assert(car['brand']) == 'toyota'

# cars = [
#     {
#         'brand' : 'toyota'
#     },
#     {
#         'brand' : "honda",
#         'products': [
#          'civic'
#         ]
#     }
# ]
# assert(cars[1]['products'][0]) == 'civic'

# raw_cars = 'toyota,honda,indiacar'

# assert(raw_cars.split(',')) == ['toyota','honda','indiacar']

# raw_cars = raw_cars.upper()
# #def function_a(a):
#     #return

# assert(raw_cars.split(',')) == ['TOYOTA','HONDA','INDIACAR']

# raw_cars = 'toyota,honda,indiacar,indiacar,indiacar'

# raw_cars = raw_cars.split(',')
# raw_cars = set(raw_cars)
# raw_cars = list(raw_cars)

# assert(raw_cars) == ['toyota', 'honda', 'indiacar']

# raw_cars = 'toyota,honda,indiacar,indiacar,indiacar'
# raw_cars = raw_cars.split(',')
# raw_cars = set(raw_cars)
# raw_cars = len(raw_cars)
# assert(raw_cars) == 3


#data yang dmasukan string
#nama = input("masukan nama anda:")

#print("nama anda:", nama)

#umur_int = int(input("berapa umur anda:" ))
#umur = float(input("masukan umur anda:"))

#print("umur anda :",umur_int, "type :",type(umur_int))

#biner = bool(int(input("masukan nilai boolean: ")))

#print("data :",biner, "type",type(biner))



#==========================OPERASI ARITMATIKA======================

# a = 5
# b = 3

#penambahan
#hasil = a + b
#print(a,"+",b,"=",hasil)

#pengurangan
#hasil = a - b
#print(a,"-",b,"=",hasil)

#perkalian
#hasil = a * b
#print(a,"*",b,"=",hasil)

#pembagian
#hasil = a / b
#print(a,"/",b,"=",hasil)

#berpangkat/eksponen
#hasil = a ** b
#print(a,"**",b,"=",hasil)

#modulus
#hasil = a % b
#print(a,"%",b,"=",hasil)

#floor division
#hasil = a // b
#print(a,"//",b,"=",hasil)
#========================================================




#=================untuk mengambil salah satu huruf dari function================
#a = ("hello world") 
#print (a[0])
#===============================================================================



#=======================urutan hurufnya jadi kebawah[==========================]
#for x in "banana": 
    #print(x)
#=============================================================================\



#=========================untuk menghitung jumlah huruf dalam function=======
#a = "hello world"  
#print(len(a))
#============================================================================



#=============================================================================
# thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon","mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon","mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon","mango"]
# print(thislist[:4])
#===========================================================================

