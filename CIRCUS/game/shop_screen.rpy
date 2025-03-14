##### The game screen
screen shop_screen:  

    add "bg/bg shop.png" xalign 0.5 yalign 0.5:
        size (1920, 1080)

    hbox:
        add "shop/coin.png" xalign 50 yalign 50:
            size (50, 50)
        text "Money = [money]" xalign 50 yalign 50


    imagebutton:
        xpos 1700 
        ypos 50
        idle Transform("shop/back_button.png", zoom=0.3)  
        hover Transform("shop/back_button.png", zoom=0.3)
        action Jump("fokusnik_pressed")

    imagebutton:
        xpos 100 
        ypos 200
        idle Transform("shop/duda.png", zoom=2)  
        hover Transform("shop/duda-2.png", zoom=2)
        action [SetVariable("item", "duda"), Jump("buy_item")]

    imagebutton:
        xpos 600
        ypos 200
        idle Transform("shop/rice.png", zoom=2)  
        hover Transform("shop/rice-2.png", zoom=2)
        action [SetVariable("item", "rice"), Jump("buy_item")]

    imagebutton:
        xpos 1150
        ypos 200
        idle Transform("shop/wine.png", zoom=2)  
        hover Transform("shop/wine-2.png", zoom=2)
        action [SetVariable("item", "wine"), Jump("buy_item")]

    imagebutton:
        xpos 1500
        ypos 400
        idle Transform("shop/book.png", zoom=2)  
        hover Transform("shop/book-2.png", zoom=2)
        action [SetVariable("item", "book"), Jump("buy_item")]

   
    imagebutton:
        xpos 200
        ypos 700
        idle Transform("shop/meal.png", zoom=2)  
        hover Transform("shop/meal-2.png", zoom=2)
        action [SetVariable("item", "meal"), Jump("buy_item")]

    imagebutton:
        xpos 600
        ypos 700
        idle Transform("shop/ring.png", zoom=2)  
        hover Transform("shop/ring-2.png", zoom=2)
        action [SetVariable("item", "ring"), Jump("buy_item")]

    imagebutton:
        xpos 900
        ypos 700
        idle Transform("shop/light.png", zoom=2)  
        hover Transform("shop/light-2.png", zoom=2)
        action [SetVariable("item", "light"), Jump("buy_item")]

    imagebutton:
        xpos 1300
        ypos 600
        idle Transform("shop/knife.png", zoom=1)  
        hover Transform("shop/knife-2.png", zoom=1)
        action [SetVariable("item", "knife"), Jump("buy_item")]

    imagebutton:
        xpos 1500
        ypos 700
        idle Transform("shop/bear.png", zoom=2)  
        hover Transform("shop/bear-2.png", zoom=2)
        action [SetVariable("item", "bear"), Jump("buy_item")]



label buy_item:
    if money < 5:
        "У тебя не хватает денег."
    else:
        $ items.append(item)
        "Продукт куплен!"
        $ money -= 5
    jump fokusnik_pressed


