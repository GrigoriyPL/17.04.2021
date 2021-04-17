class Human: # Создание класса # Название класса с заглавной буквы
    def __init__(self,age,height,hair_color): # функция задаваемых параметров __init__ Обязателен
        self.age = age
        self.height = height
        self.hair_color = hair_color
    def say_hello(self): # Функция внутри класс  self - является обязательным, self означает то, что разные переменные у разныъ переменных
        print(f"HI. im {self.age}")

Max = Human(18,125,"red") # 18,125,"red" задали параметры функции
print(f"i'm {Max.hair_color}")
