## Screen with character screen button
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/stats_%s.png"
        action ShowMenu("character_screen")
        
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
                textbutton _(girl1.name):
                    action SetVariable("selectedCharacter", girl1)
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
                text "Name: [selectedCharacter.name]"
                text "Blood Type: [selectedCharacter.bloodType]"
                text "Major: [selectedCharacter.major]"

                hbox:
                    spacing 20
                    text "Affection"
                    ## We're creating a bar with the max affection of 10
                    ## You can change the max affection to 100 or whatever value you want.
                    bar value StaticValue(selectedCharacter.affection, 10) xsize 300 
            add selectedCharacter.imageName xalign 1.0 yalign 0.5

style character_button_text:
    xalign 0.5