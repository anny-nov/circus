label meeting_gg_pressed:
    scene bg gg
    show screen mapUI
    show screen characterUI
    while True:
        "Исследуй окрестности и познакомься со всеми артистами."

label meeting_arena_pressed:
    hide screen mapUI
    scene bg arena
    jump after_house_choice

label meeting_warehouse_pressed:
    hide screen mapUI
    scene bg warehouse
    jump after_house_choice

label meeting_food_pressed:
    hide screen mapUI
    scene bg food
    jump after_house_choice

label meeting_gymnastka_pressed:
    hide screen mapUI
    scene bg gymnastka
    jump gymnastka_house

label meeting_fokusnik_pressed:
    hide screen mapUI
    scene bg fokusnik
    jump fokusnik_house

label meeting_clown_pressed:
    hide screen mapUI
    scene bg clown
    jump clown_house

label meeting_adam_pressed:
    hide screen mapUI
    scene bg adam
    jump adam_house

label meeting_hoz_pressed:
    hide screen mapUI
    scene bg hoz
    jump hoz_house

label meeting_psina_pressed:
    hide screen mapUI
    scene bg psina
    jump psina_house

label meeting_dress_pressed:
    hide screen mapUI
    scene bg dress
    jump dress_house

label meeting_fire_pressed:
    hide screen mapUI
    scene bg fire
    jump after_house_choice

