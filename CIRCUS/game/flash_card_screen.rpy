##### The game screen
screen flash_card_screen:  
    timer 1.0 action If (memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("game_lose") ) repeat True
    
    text "Оставшееся время: " + str(memo_timer) xalign 0.5 yalign 0.02
    
    #Cards
    grid 4 3:
        xalign 0.5 yalign 0.5
        for card in cards_list:
            button:
                background None

                if card["c_chosen"]:       
                    add card["c_value"]    
                else:                      
                    add "G"                

                action If ( (card["c_chosen"] or not can_click), None, [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )
 

init:
    python:
        # Тасовка карт
        def cards_shuffle(x):
            renpy.random.shuffle(x)
            return x

    # Графика
    image A = "cards/card-1.png"
    image B = "cards/card-2.png"
    image C = "cards/card-3.png"          
    image D = "cards/card-4.png"
    image E = "cards/card-5.png" 
    image F = "cards/card-6.png"
    image G = "cards/card-9.png"


# Вход в игру
label flash_card_game (game_time=50.0):
    # Номинал карт
    $ values_list = ["A", "A", "B", "B", "C", "C", "D",  "D", "E", "E", "F", "F"]
    
    # Перемешать
    $ values_list = cards_shuffle(values_list)
    
    $ cards_list = []
    python:
        for i in range (0, len(values_list) ):
            cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":False} )   

    # Время игры
    $ memo_timer = game_time
    
    # Показать саму игру с графикой
    show screen flash_card_screen
    
    label game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        
        $ turns_left = 2
        
        label turns_loop:
            if turns_left > 0:
                $ result = ui.interact() 
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append (cards_list[result]["c_number"])
                $ turned_cards_values.append (cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop
        
        $ can_click = False

        # Закрыть карту, если не совпадает
        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
            $ renpy.pause (0.5, hard = True)
            python:
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False
        # Если карты одинаковые
        else:
            $ renpy.pause (0.5, hard = True)
            python: 
                # Удалить одинаковые
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_value"] = Null()

                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump ("game_loop")
                renpy.jump ("game_win")
                
        jump game_loop


# Пройгрыш
label game_lose:
    hide screen flash_card_screen
    show fokusnik normal
    LuVay "Вот незадача!"
    $ renpy.pause (0.1, hard = True)
    $ renpy.pause (1.0, hard = True)
    return (0)

# Выйгрыш
label game_win:
    hide screen flash_card_screen
    show fokusnik normal
    $ renpy.pause (0.1, hard = True)
    $ renpy.pause (0.1, hard = True)
    LuVay "Молодец!"
    return (1)