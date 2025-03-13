##### The game screen
screen shop_screen:  
    add "bg/bg shop.png" xalign 0.5 yalign 0.5:
        size (1920, 1080)

    text "Money = [money]"

    imagebutton:
        xpos 1600 
        ypos 50
        idle "shop/back_button.png"
        hover "shop/back_button.png"
        action Jump("fokusnik_pressed")

    imagebutton:
        xpos 100 
        ypos 300
        idle "shop/duda.png"
        hover "shop/duda-2.png"
        action Jump("buy_item")

    imagebutton:
        xpos 500
        ypos 300
        idle "shop/rice.png"
        hover "shop/rice-2.png"
        action Jump("buy_item")

    imagebutton:
        xpos 850
        ypos 300
        idle "shop/wine.png"
        hover "shop/wine-2.png"
        action Jump("buy_item")

    imagebutton:
        xpos 1100
        ypos 300
        idle "shop/book.png"
        hover "shop/book-2.png"
        action Jump("buy_item")

   
    imagebutton:
        xpos 200
        ypos 700
        idle "shop/meal.png"
        hover "shop/meal-2.png"
        action Jump("buy_item")

    imagebutton:
        xpos 500
        ypos 700
        idle "shop/ring.png"
        hover "shop/ring-2.png"
        action Jump("buy_item")

    imagebutton:
        xpos 700
        ypos 700
        idle "shop/light.png"
        hover "shop/light-2.png"
        action Jump("buy_item")

    imagebutton:
        xpos 1000
        ypos 600
        idle "shop/knife.png"
        hover "shop/knife-2.png"
        action Jump("buy_item")

    imagebutton:
        xpos 1200
        ypos 700
        idle "shop/bear.png"
        hover "shop/bear-2.png"
        action Jump("buy_item")



label buy_item:
    if money < 5:
        "У тебя не хватает денег."
    else:
        "Продукт куплен!"
        $ money -= 5
    call screen shop_screen


