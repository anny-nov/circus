define y = Character(name = "stranger", color = "#3B87C4")
label start:
    scene bg classroom
    ## show the stats button from screen gameUI (custom_screens.rpy)
    show screen gameUI
    jump show_choices


label show_choices:
    y "What do you want to know?"
    menu:
        "Learn [boy1.name]'s name":
            ## This will update the name in the character screen       
            $ boy1.name = "Yuki"

            ## This will update the sayer's name
            $ y.name = "Yuki"
            
            # Notice that the first, "What do you want to know" shows the sayer's name as "stranger".s
            # After choosing this option, the sayer is changed to "Yuki" because of the code above.
            
            y "I'm Yuki. Nice to meet you."

        "Learn [boy1.name]'s blood type":
            $ boy1.bloodType = "O"
            "The bloodType  learned"
        "Learn [boy1.name]'s major":
            $ boy1.major = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            "The major is learned."
        "Increase [boy1.name]'s affection by 5":
            $ boy1.affection += 5
            "The affection increased by 5."
        "Decrease [boy1.name]'s affection by 3":
            $ boy1.affection -= 3
            "The affection is decreased by 3."
        "End game":
            return
    
    jump show_choices