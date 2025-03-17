label gg_pressed:
    scene bg gg
    show screen mapUI
    show screen characterUI
    while True:
        "Свободное время! Сходи к кому-нибудь в гости!"
        "ало"

label arena_pressed:
    hide screen mapUI
    scene bg arena
    jump after_house_choice

label warehouse_pressed:
    hide screen mapUI
    scene bg warehouse
    jump after_house_choice

label gymnastka_pressed:
    hide screen mapUI
    scene bg gymnastka
    jump gymnastka_house

label fokusnik_pressed:
    hide screen mapUI
    scene bg fokusnik
    jump fokusnik_house

label clown_pressed:
    hide screen mapUI
    scene bg clown
    jump clown_house

label adam_pressed:
    hide screen mapUI
    scene bg adam
    jump adam_house

label hoz_pressed:
    hide screen mapUI
    scene bg hoz
    jump hoz_house

label psina_pressed:
    hide screen mapUI
    scene bg psina
    jump psina_house

label dress_pressed:
    hide screen mapUI
    scene bg dress
    jump dress_house

label fire_pressed:
    hide screen mapUI
    scene bg fire
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
        jump gg_pressed

    label show_choices:
        Adam "Что хочешь узнать?"
        menu:
            "Узнать [adam.name] имя":
                ## This will update the name in the character screen       
                $ adam.name = "Адам"
                $ Adam.name = "Адам"
                
                # Notice that the first, "What do you want to know" shows the sayer's name as "stranger".s
                # After choosing this option, the sayer is changed to "Yuki" because of the code above.
                
                Adam "Я Адам."

            "Узнать, что нравится [adam.name]":
                $ adam.bloodType = "O"
                "Ты узнал."
            "Узнать [adam.name] любимую песню":
                $ adam.song = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                "Песня выучена."
            "Увеличить дружбу [adam.name] на 5":
                $ adam.affection += 5
                "Вы больше друзья"
            "Уменьшить дружбу [adam.name] на 3":
                $ adam.affection -= 3
                "Вы меньше друзья"
            "Го дальше":
                jump choice1_done
        
        jump show_choices
    
label fokusnik_house:
    play music "Darktown_Strutters_Ball.mp3"
    show fokusnik normal
    LuVay "Что ты хотел?"
    hide fokusnik normal
    show screen characterUI
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
            hide screen characterUI
            call screen shop_screen 
        "Подарить подарок":
            window hide
            hide screen characterUI
            jump call_invscreen
        "Я пошел":
            stop music
            jump gg_pressed

    return

label fokusnik_thanks:
    show fokusnik normal
    LuVay "Спасибо, родной"
    hide fokusnik normal
    jump fokusnik_house
    

label gymnastka_house:
    show gymnastka normal
    Amanda "Ну привет."
    hide gymnastka normal
    show screen characterUI
    menu:
        "Подарить подарок":
            window hide
            hide screen characterUI
            jump call_invscreen
        "Я пошел":
            stop music
            jump gg_pressed

label clown_house:
    show clown normal
    Fred "Заходи."
    hide clown normal
    show screen characterUI
    menu:
        "Подарить подарок":
            window hide
            hide screen characterUI
            jump call_invscreen
        "Я пошел":
            stop music
            jump gg_pressed

label adam_house:
    show adam normal
    Adam "Рад тебя видеть!"
    hide adam normal
    show screen characterUI
    menu:
        "Подарить подарок":
            window hide
            hide screen characterUI
            jump call_invscreen
        "Я пошел":
            stop music
            jump gg_pressed

label hoz_house:
    show hoz normal
    Madam "Здравствуй, [name]"
    hide hoz normal
    show screen characterUI
    menu:
        "Подарить подарок":
            window hide
            hide screen characterUI
            jump call_invscreen
        "Я пошел":
            stop music
            jump gg_pressed

label psina_house:
    show psina normal
    Kyle "Что ты тут забыл?"
    hide psina normal
    show screen characterUI
    menu:
        "Подарить подарок":
            window hide
            hide screen characterUI
            jump call_invscreen
        "Я пошел":
            stop music
            jump gg_pressed

label dress_house:
    show dress normal
    Mary "Привет, бродяга!"
    hide dress normal
    show screen characterUI
    menu:
        "Подарить подарок":
            window hide
            hide screen characterUI
            jump call_invscreen
        "Я пошел":
            stop music
            jump gg_pressed
