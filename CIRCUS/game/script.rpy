# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define Farmer = Character('Фермер', color="#ffffff")
define Adam = Character('Адам', color="#ffffff")
define LuVay = Character('Лю Вэй', color="#ffffff")
define Kyle = Character("Кайл", color="#ffffff")
define Charlotte = Character("Аманда", color="#ffffff")
define Fred = Character("Фред", color="#ffffff")
define Mary = Character("Мэри", color="#ffffff")
define Gabriel = Character("Габриэль", color="#ffffff")
define Madam = Character("Миссис Дюморье", color="#ffffff")


define gg = Character("", color="#ffffff")


default name = "Luidgi"

default money = 20
default items = []

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    # use the code below to show the "map" button
    #show screen mapUI
    #show screen characterUI

    jump start_forest





