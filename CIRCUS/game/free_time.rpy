label gg_pressed:
    if meeting_time:
        jump meeting_gg_pressed
    else:
        scene bg gg
        show screen mapUI
        show screen characterUI
        while True:
            "Свободное время! Сходи к кому-нибудь в гости!"
            "ало"

label arena_pressed:
    hide screen mapUI
    hide screen characterUI
    scene bg arena
    if meeting_time:
        jump meeting_arena
    else:
        jump after_house_choice

label warehouse_pressed:
    hide screen mapUI
    hide screen characterUI
    scene bg warehouse
    if meeting_time:
        jump meeting_warehouse
    else:
        jump after_house_choice

label food_pressed:
    hide screen mapUI
    hide screen characterUI
    scene bg food
    if meeting_time:
        jump meeting_food
    else:
        jump after_house_choice

label gymnastka_pressed:
    hide screen mapUI
    hide screen characterUI
    if meeting_time:
        scene bg sunny trailer
        jump meeting_gymnastka
    else:
        scene bg gymnastka
        jump gymnastka_house

label fokusnik_pressed:
    hide screen mapUI
    hide screen characterUI
    if meeting_time:
        scene bg sunny trailer
        jump meeting_fokusnik
    else:
        scene bg fokusnik
        jump fokusnik_house

label clown_pressed:
    hide screen mapUI
    hide screen characterUI
    if meeting_time:
        scene bg sunny trailer
        jump meeting_clown
    else:
        scene bg clown
        jump clown_house

label adam_pressed:
    hide screen mapUI
    hide screen characterUI
    if meeting_time:
        scene bg sunny trailer
        jump meeting_adam
    else:
        scene bg adam
        jump adam_house

label hoz_pressed:
    hide screen mapUI
    hide screen characterUI
    scene bg hoz
    if meeting_time:
        jump meeting_hoz
    else:
        jump hoz_house

label psina_pressed:
    hide screen mapUI
    hide screen characterUI
    if meeting_time:
        scene bg sunny trailer
        jump meeting_psina
    else:
        scene bg psina
        jump psina_house

label dress_pressed:
    hide screen mapUI
    hide screen characterUI
    if meeting_time:
        scene bg sunny trailer
        jump meeting_dress
    else:
        scene bg dress
        jump dress_house

label fire_pressed:
    hide screen mapUI
    hide screen characterUI
    scene bg fire
    if meeting_time:
        jump meeting_fire
    else:
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
                $ adam.favoriteItems = "Шашлык."
                "Ты узнал."
            "Узнать, что [adam.name] не любит":
                $ adam.hatedItems = "Рыба."
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
            call flash_card_game pass (game_time=30.0) from _call_flash_card_game
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
    Charlotte "Ну привет."
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
