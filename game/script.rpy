# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define Adam = Character('Адам', color="#ffffff")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg circus day
    "Добро пожаловать! Твоя история начнется совсем скоро. А пока, как тебя зовут?"
    python:
        name = renpy.input(_(""))
    define gg = Character("[name]", color="#ffffff")
    "Я вышел на прогулку по окрестностям цирка."
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

        jump choice1_done

    label choice1_adam:

        $ menu_flag = False
        show adam normal
        Adam "Привет."

        jump choice1_done

    label choice1_done:

        Adam "Го сексом трахаться?"
        hide adam normal
        "Счастливый финал!"



    return
