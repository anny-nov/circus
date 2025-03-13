# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define Adam = Character('Адам', color="#ffffff")
define LuVay = Character('Лю Вэй', color="#ffffff")

default name = "Luidgi"

default money = 0
default item = ""

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    # use the code below to show the "map" button
    show screen mapUI
    show screen characterUI

    "Добро пожаловать! Твоя история начнется совсем скоро. А пока, как тебя зовут?"
    python:
        name = renpy.input((""))
    if name.strip() == "":  
        $ name = "Luidgi"  

    define gg = Character("[name]", color="#ffffff")
    show gg normal
    gg "Я вышел на прогулку по окрестностям цирка."
    hide gg normal


    while True:
        "Свободное время! Сходи к кому-нибудь в гости!"
        "ало"
    return

label arena_pressed:
    scene bg arena
    show bg arena at Transform(zoom=0.5)
    "Arena was pressed!"
    jump after_house_choice

label warehouse_pressed:
    scene bg warehouse
    show bg warehouse at Transform(zoom=1.5)
    "Warehouse was pressed!"
    jump after_house_choice

label gymnastka_pressed:
    scene bg gymnastka
    show bg gymnastka at Transform(zoom=1.88)
    "gymnastka was pressed!"
    jump after_house_choice

label fokusnik_pressed:
    scene bg fokusnik
    show bg fokusnik at Transform(zoom=1.88)
    "fokusnik was pressed!"
    jump fokusnik_house

label clown_pressed:
    scene bg clown
    show bg clown at Transform(zoom=1.88)
    "clown was pressed!"
    jump after_house_choice

label kris_pressed:
    scene bg kris
    show bg kris at Transform(zoom=1.88)
    "kris was pressed!"
    jump after_house_choice

label hoz_pressed:
    scene bg hoz
    show bg hoz at Transform(zoom=3.5)
    "hozyaika was pressed!"
    jump after_house_choice

label psina_pressed:
    scene bg psina
    show bg psina at Transform(zoom=1.88)
    "Psina was pressed!"
    jump after_house_choice

label gg_pressed:
    scene bg gg
    show bg gg at Transform(zoom=1.88)
    "My home was pressed!"
    jump after_house_choice

label dress_pressed:
    scene bg dress
    show bg dress at Transform(zoom=1.88)
    "Dressirovschiza was pressed!"
    jump after_house_choice

label fire_pressed:
    scene bg fire
    show bg fire at Transform(zoom=1.88)
    "Fire was pressed!"
    jump after_house_choice

label after_house_choice:
   
    show gg normal
    gg "О, привет..."
    hide gg normal
    menu:
        "Крис":
            jump choice1_kris
        "Адам":
            jump choice1_adam

    label choice1_kris:

        $ menu_flag = True
        show adam normal
        Adam "Я Адам."

        jump show_choices

    label choice1_adam:

        $ menu_flag = False
        show adam normal
        Adam "Привет."

        jump show_choices

    label choice1_done:
        Adam "Го сексом трахаться?"
        hide adam normal
        "Счастливый финал!"
        return

    label show_choices:
        Adam "Что хочешь узнать?"
        menu:
            "Узнать [boy1.name] имя":
                ## This will update the name in the character screen       
                $ boy1.name = "Адам"
                
                # Notice that the first, "What do you want to know" shows the sayer's name as "stranger".s
                # After choosing this option, the sayer is changed to "Yuki" because of the code above.
                
                Adam "Я Адам, я же сказал"

            "Узнать группу крови [boy1.name]":
                $ boy1.bloodType = "O"
                "Группа крови изучена, weirdo"
            "Узнать [boy1.name] любимую песню":
                $ boy1.song = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                "Песня выучена."
            "Увеличить дружбу [boy1.name] на 5":
                $ boy1.affection += 5
                "Вы больше друзья"
            "Уменьшить дружбу [boy1.name] на 3":
                $ boy1.affection -= 3
                "Вы меньше друзья"
            "Го дальше":
                jump choice1_done
        
        jump show_choices
    
label fokusnik_house:
    play music "Darktown_Strutters_Ball.mp3"
    show fokusnik normal
    LuVay "Что ты хотел?"
    hide fokusnik normal
    menu:
        "Сыграть в игру":
            window hide
            call flash_card_game pass (game_time=30.0)
            show fokusnik normal
            if _return:
                LuVay "Хочешь выйграть еще денег?"
                $ money += 5
            else:
                LuVay "Хочешь отыграться?"
                $ money -= 5
            menu:
                "Давай":
                    jump fokusnik_house
                "С меня хватит":
                    show fokusnik normal
                    LuVay "Пока-пока!"
                    stop music fadeout 1.0
                    hide fokusnik normal
                    jump fokusnik_house
        "Купить вещичек":
            window hide
            call screen shop_screen 
        "Подарить подарок":
            window hide
            call screen presentUI
            LuVay "Вау!"

    return

label fokusnik_thanks:
    show fokusnik normal
    LuVay "Спасибо, родной"
    hide fokusnik normal
    jump fokusnik_house
    
