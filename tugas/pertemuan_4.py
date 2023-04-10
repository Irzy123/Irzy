# import datetime
# class person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age  = age

#         def say_my_name(self):
#             print("Hello my name is " + self.name)

#         def change_my_name(self, new_name):
#             self.name = new_name

# class student(person):

#     def __init__(self,nisn,name,age):
#         super().__init__(name, age)
#         self.nisn = nisn

#     def say_my_name(self):
#         super().say_my_name()
#         print("Im Student with name " + self.name)



# person_1 = person('Jhon',36)
# print(person_1.name)
# print(person_1.age)
# print(person_1.say_my_name())

# student_1  = student('09876', 'emil', 12)
# student_1.say_my_name()

# class mathematic:

#     def __init__ (self):
#         self.value = 0

#     def increment(self):
#         self.value += 2

#     def decrement(self):
#         self.value -= 2

#     def add(self,a,b):
#         return a + b
    
#     def substraction(self, a, b):
#         return a - b
    
#     def multiply(self, a, b):
#         return a + b
    
# math = mathematic()
# print(math.add(1, 2))
# print(datetime.datetime.now())

    
class car():

    def __init__(self,brand,year):

        self.brand = brand
        self.year = year

    pintu = "tertutup"
    mobil = "mati"

    def membukapintu(self):
        if self.pintu == "tertutup":
           print("Pintu berhasil dibuka")
           self.pintu = "terbuka"
        else:
            print("Pintu telah terbuka")

    def menutuppintu(self):
        if self.pintu == "terbuka":
            print("pintu berhasil ditutup")
            self.pintu = "tertutup"
        else:
            print("pintu telah tertutup")

    def menyalakanMobil(self):
        if self.mobil == "mati":
            print("Mobil berhasil dinyalakan")
            self.mobil = "menyala" 
        else:
            print("Mobil sudah menyala")

    def mematikanMobil(self):
        if self.mobil == 'menyala':
            print("Mobil Berhasil dimatikan")
            self.mobil = "mati"
        else:
            print("Mobil sudah mati")



    


mobilku = car("honda", 2020)

mobilku.membukapintu()
mobilku.menutuppintu()
mobilku.menyalakanMobil()
mobilku.mematikanMobil()



