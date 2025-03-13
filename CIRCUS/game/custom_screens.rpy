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

## Screen with character screen button
screen presentUI:
    modal True
    add "shop/stock.png"
    imagebutton:
        xoffset 200
        yoffset 750
        idle "shop/meal.png"
        hover "shop/meal-2.png"
        action [Hide("presentUI"), Jump("gift_product")]


# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.
label call_mapUI:
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
        idle "map/trailer_kris.png"
        hover "map/trailer_kris-2.png"
        action Jump("kris_pressed")

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
                textbutton _(boy1.name):
                    action SetVariable("selectedCharacter", boy1)
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
                ## Notice that we're using selectedCharacter to show the variables here.
                text "Имя: [selectedCharacter.name]"
                text "Группа Крови: [selectedCharacter.bloodType]"
                text "Любимая песня: [selectedCharacter.song]"

                hbox:
                    spacing 20
                    text "Affection"
                    ## We're creating a bar with the max affection of 10
                    ## You can change the max affection to 100 or whatever value you want.
                    bar value StaticValue(selectedCharacter.affection, 20) xsize 300 
                add selectedCharacter.imageName xalign 1.0 yalign 0.5


style character_button_text:
    xalign 0.5


label gift_product:
    jump fokusnik_thanks