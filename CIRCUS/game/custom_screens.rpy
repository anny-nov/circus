## Screen with Stats Button
screen mapUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        action Jump ("call_mapUI")

## Screen with character screen button
screen characterUI:
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        auto "UI/stats_%s.png"
        action ShowMenu("character_screen")


# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.
label call_mapUI:
    window hide
    call screen MapUI

screen MapUI:
    add "map/bg map.jpg" xalign 0.5 yalign 0.5:
        size (1920, 1080)

    imagebutton:
        xpos 678 
        ypos 440
        idle "map/arena.png"
        hover "map/arena-2.png"
        action Jump("arena_pressed")

    imagebutton:
        xpos 720
        ypos 850
        idle "map/fire.png"
        hover "map/fire-2.png"
        action Jump("fire_pressed")

    imagebutton:
        xpos 560
        ypos 335
        idle "map/warehouse.png"
        hover "map/warehouse-2.png"
        action Jump("warehouse_pressed")
   
    imagebutton:
        xpos 1200
        ypos 800
        idle "map/trailer_gg.png"
        hover "map/trailer_gg-2.png"
        action Jump("gg_pressed")

    imagebutton:
        xpos 300
        ypos 800
        idle "map/trailer_dress.png"
        hover "map/trailer_dress-2.png"
        action Jump("dress_pressed")

    imagebutton:
        xpos 1300
        ypos 600
        idle "map/trailer_psina.png"
        hover "map/trailer_psina-2.png"
        action Jump("psina_pressed")

    imagebutton:
        xpos 250
        ypos 520
        idle "map/trailer_gymnastka.png"
        hover "map/trailer_gymnastka-2.png"
        action Jump("gymnastka_pressed")

    imagebutton:
        xpos 1590
        ypos 720
        idle "map/trailer_adam.png"
        hover "map/trailer_adam-2.png"
        action Jump("adam_pressed")

    imagebutton:
        xpos 850
        ypos 300
        idle "map/trailer_fokusnik.png"
        hover "map/trailer_fokusnik-2.png"
        action Jump("fokusnik_pressed")

    imagebutton:
        xpos 1010
        ypos 230
        idle "map/trailer_clown.png"
        hover "map/trailer_clown-2.png"
        action Jump("clown_pressed")

    imagebutton:
        xpos 1150
        ypos 270
        idle "map/trailer_hoz.png"
        hover "map/trailer_hoz-2.png"
        action Jump("hoz_pressed")


        
## Stats UI
screen character_screen():
    tag character_screen_tag
    add "UI/bg peach.png"
    hbox:
        ## LEFT FRAME
        frame:
            #Remove hashtag in the next lineto remove the black and blue background
            # background None
            style_prefix "character"
            ysize 1080
            xsize 640
            vbox:
                xalign 0.5
                yalign 0.5
                textbutton _(itan.name):
                    action SetVariable("selectedCharacter", itan)
                    xsize 640
                textbutton _(dress.name):
                    action SetVariable("selectedCharacter", dress)
                    xsize 640
                textbutton _(fokusnik.name):
                    action SetVariable("selectedCharacter", fokusnik)
                    xsize 640
                textbutton _(clown.name):
                    action SetVariable("selectedCharacter", clown)
                    xsize 640
                textbutton _(psina.name):
                    action SetVariable("selectedCharacter", psina)
                    xsize 640
                textbutton _(gymnastka.name):
                    action SetVariable("selectedCharacter", gymnastka)
                    xsize 640
                textbutton _(adam.name):
                    action SetVariable("selectedCharacter", adam)
                    xsize 640
                textbutton _(letizia.name):
                    action SetVariable("selectedCharacter", letizia)
                    xsize 640
            
            textbutton _("Return"):
                yalign 0.5
                yoffset 90
                xoffset 20
                action Return()
        ## RIGHT FRAME
        frame:
            background None
            ysize 1080
            xsize 1280
            vbox:
                xalign 0.5
                xsize 600
                xoffset -300
                yoffset 100
                spacing 20
                if selectedCharacter == itan:
                    text "Имя: [selectedCharacter.name]"
                    hbox:
                        spacing 20
                        text "Милосердие"
                        bar value StaticValue(selectedCharacter.mercifulness, 50) xsize 300 
                    hbox:
                        spacing 20
                        text "Расчетливость"
                        bar value StaticValue(selectedCharacter.guile, 50) xsize 300 
                    add selectedCharacter.imageName xalign 1.0 yalign 0.5
                else:
                    text "Имя: [selectedCharacter.name]"
                    text "Нравится: [selectedCharacter.favoriteItems]"
                    text "Любимая песня: [selectedCharacter.song]"

                    hbox:
                        spacing 20
                        text "Affection"
                        bar value StaticValue(selectedCharacter.affection, 50) xsize 300 
                    add selectedCharacter.imageName xalign 1.0 yalign 0.5


style character_button_text:
    xalign 0.5



## Gift a present
default page = 0 

label call_invscreen:
    call screen inventory_screen  
    return

screen inventory_screen:
    # Get only the items for the current page
    add "shop/stock.png"
    $ start_index = page * 4
    $ end_index = min(start_index + 4, len(items))
    $ current_items = items[start_index:end_index]

    for i, item in enumerate(current_items):
        imagebutton:
            xpos 150 + (i * 490)
            ypos 700
            idle "shop/"+item+".png"
            hover "shop/"+item+"-2.png"
            action [SetVariable("selected_item", item), Hide("inventory_screen"), Jump("gift_product")]

    # Pagination Controls
    if page > 0:
        textbutton "{b}Previous{/b}" action [SetVariable("page", page - 1)] xpos 390 ypos 600
    if end_index < len(items):
        textbutton "{b}Next{/b}" action [SetVariable("page", page + 1)] xpos 1380 ypos 600
    
    imagebutton:
        xpos 1700 
        ypos 50
        idle Transform("shop/back_button.png", zoom=0.3)  
        hover Transform("shop/back_button.png", zoom=0.3)

        action Jump("gg_pressed")   


label gift_product:
    if selected_item in items:
        $ items.remove(selected_item)  # Remove the selected item
        "Ты подарил [selected_item]!"
    else:
        "Ошибка: товар не найден."
    jump fokusnik_thanks


