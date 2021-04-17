class Human: # Создание класса # Название класса с заглавной буквы
    age = 18
    height = 125
    hair_color = "Orange"
    def say_hello(self): # Функция внутри класс  self - является обязательным, self означает то, что разные переменные у разныъ переменных
        print(f"HI. im {self.age}")


Max = Human() # присвоение переменной класа

print(f'i am {Max.age}') # Вывод переменной Max.age Max.hair_color Max.height

Dima = Human()
Dima.age = 16
print(f"Dima age {Dima.age}")


Dima.say_hello() # вызов функции из класса
Max.say_hello()

