label meeting_gg_pressed:
    $ meeting_time = True
    scene bg gg
    show screen mapUI
    show screen characterUI


    if all(met_characters):
        jump story_begins
    else:
        while True:
            "Исследуй окрестности и познакомься со всеми артистами."

label explanation_begin:
    scene bg gg
    
    window hide 
    $ renpy.pause(0.5)  

    show text "В свободное время в верхней части экрана доступны два слота." at truecenter
    $ renpy.pause(7) 
    hide text

    show text "Один отображает уровень отношений с персонажами и характеристики главного героя." at truecenter
    $ renpy.pause(7)
    hide text

    show text "Второй — это карта для навигации по территории цирка." at truecenter
    $ renpy.pause(7)
    hide text

    window show 
    jump meeting_gg_pressed

label story_begins:
    $ meeting_time = False
    jump gg_pressed

label meeting_arena:
    if met_characters[0]:
        show dress normal
        Mary "Ты что-то забыл?"
        jump mary_continue
    else:
        default asked_mary_name = False
        default asked_mary_job = False
        default asked_mary_secret = False
        $ met_characters[0] = True

    
        "Я вышел на арену и остановился у самого входа."
        "Запах сырой соломы и железа ударил в ноздри, мгновенно вернув забытые образы."
        "Хриплый голос конферансье, гром аплодисментов..."
        "Цирк. Я был здесь последний раз еще ребенком."
        "Я тогда впервые увидел зверей из своих книжек, фокусы казались настоящим волшебством, а артисты - кем-то вроде богов."
        "Сейчас же всё было другим."
        "И арена оказалась гораздо меньше, чем я запомнил."
        "Где-то сбоку хлопнула клетка. Я вздрогнул."
        "На песке в центре стояла женщина с хлыстом. Она заметила меня."

        show dress normal
        Mary "Эй! Кто тебя сюда пустил?"
        hide dress normal
        "Я поднял руки, показывая, что безобиден."
        show gg tired
        gg "Прости. Я просто осматриваюсь. Только приехал"
        hide gg tired
        "Она нахмурилась, будто услышала не то слово. Несколько секунд смотрела, не отвечая."
        show dress normal
        Mary "Приехал?"
        hide dress normal
        "Она отвернулась и что-то пробормотала себе под нос. Я не расслышал, но это звучало резко."
        show dress normal
        Mary "Значит, опять без предупреждения..."
        hide dress normal
        "Она махнула рукой, словно отгоняя мысль, и резко сменила тон."
        show dress normal
        Mary "Ладно. Раз ты уже здесь, не стой как столб."
        Mary "Кто ты? Откуда взялся?"
        hide dress normal
        "Я повторил свою легенду, затем поинтересовался в ответ."
        jump mary_questions

    label mary_questions:
        menu:
            "Что ты хочешь спросить?"

            "Как тебя зовут?" if not asked_mary_name:
                $ dress.name = "Мэри"
                $ Mary.name = "Мэри"
                $ asked_mary_name = True
                $ dress.imageName = "characters/ava/dress ava.png"

                show dress normal
                Mary "Мэри!"
                hide dress normal
                jump mary_questions

            "Ты работаешь с животными?" if not asked_mary_job:
                $ asked_mary_job = True
                show dress normal
                Mary "Ага! Вот мои лохматые артисты."
                hide dress normal
                "Её голос сразу стал теплее, и в глазах мелькнул огонёк гордости."
                show dress normal
                Mary "Полосатые, усатые, зубастые."
                Mary "Ты не бойся, они на людей не бросаются. Обычно."
                hide dress normal
                "Она усмехнулась, явно наслаждаясь моей реакцией."
                jump mary_questions

            "Ты давно здесь?" if not asked_mary_secret:
                $ asked_mary_secret = True
                show dress normal
                Mary "Ха! Достаточно, чтоб не бегать тут кругами с открытым ртом, как ты сейчас."
                Mary "А остальное — не твоё собачье дело, понял?"
                hide dress normal
                jump mary_questions

            "Продолжить..." if asked_mary_name and asked_mary_job and asked_mary_secret:
                jump mary_questions_continue
        
        label mary_questions_continue:
            show dress normal
            Mary "Ладно, новенький. У меня дела."
            Mary "Не мешай, если не хочешь попасть под горячую руку."
            "Она кивнула в сторону клетки, где из темноты на меня уставились чьи-то жёлтые глаза."
            hide dress normal
            "Я отошёл, чувствуя, что разговор окончен."
        label mary_continue:   
            menu:
                "Уйти":
                    jump call_mapUI


label meeting_warehouse:
    if met_characters[1]:
        show adam normal
        Adam "Привет еще раз!"
        jump adam_continue
    else:
        default asked_adam_name = False
        default asked_adam_job = False
        default asked_adam_secret = False
        $ met_characters[1] = True

        show adam normal
        
        Adam "Привет!"

        label adam_questions:
        menu:
            "Что ты хочешь спросить?"

            "Как тебя зовут?" if not asked_adam_name:
                $ adam.name = "Адам"
                $ Adam.name = "Адам"
                $ asked_adam_name = True
                Adam "Адам!"
                jump adam_questions

            "Чем ты здесь занимаешься?" if not asked_adam_job:
                $ asked_adam_job = True
                Adam "Я гей."
                jump adam_questions

            "Ты что-то скрываешь?" if not asked_adam_secret:
                $ asked_adam_secret = True
                Adam "Все мы что-то скрываем..."
                jump adam_questions

            "Продолжить..." if asked_adam_name and asked_adam_job and asked_adam_secret:
                jump adam_continue
            
        label adam_continue:
            Adam "Приятно познакомиться!"
            hide adam normal
            menu:
                "Уйти":
                    jump call_mapUI

label meeting_food:
    show gg tired 1
    "Закрыто..."
    "А я все еще не нашел ключ."
    hide gg tired 1
    menu:
        "Уйти":
            jump call_mapUI

label meeting_gymnastka:
    if met_characters[2]:
        show gymnastka normal
        Charlotte "Ну привет."
        hide gymnastka normal
        jump charlotte_continue
    else:
        default asked_gymnastka_name = False
        default asked_gymnastka_job = False
        default asked_gymnastka_secret = False
        $ met_characters[2] = True

        show gymnastka normal
        
        Charlotte "Привет!"

        label gymnastka_questions:
        menu:
            "Что ты хочешь спросить?"

            "Как тебя зовут?" if not asked_gymnastka_name:
                $ gymnastka.name = "Шарлотта"
                $ Charlotte.name = "Шарлотта"
                $ asked_gymnastka_name = True
                Charlotte "Шарлотта!"
                jump gymnastka_questions

            "Чем ты здесь занимаешься?" if not asked_gymnastka_job:
                $ asked_gymnastka_job = True
                Charlotte "Я гей."
                jump gymnastka_questions

            "Ты что-то скрываешь?" if not asked_gymnastka_secret:
                $ asked_gymnastka_secret = True
                Charlotte "Все мы что-то скрываем..."
                jump gymnastka_questions

            "Продолжить..." if asked_gymnastka_name and asked_gymnastka_job and asked_gymnastka_secret:
                jump charlotte_continue
            
        label charlotte_continue:
            Charlotte "Приятно познакомиться!"
            hide gymnastka normal
            menu:
                "Уйти":
                    jump call_mapUI
    

label meeting_fokusnik:
    if met_characters[3]:
        show fokusnik normal
        LuVay "Ну привет."
        hide fokusnik normal
        jump fokusnik_continue
    else:
        default asked_fokusnik_name = False
        default asked_fokusnik_job = False
        default asked_fokusnik_secret = False
        $ met_characters[3] = True

        show fokusnik normal
        
        LuVay "Привет!"

        label fokusnik_questions:
        menu:
            "Что ты хочешь спросить?"

            "Как тебя зовут?" if not asked_fokusnik_name:
                $ fokusnik.name = "Лю Вэй"
                $ LuVay.name = "Лю Вэй"
                $ asked_fokusnik_name = True
                LuVay "Лю Вэй."
                jump fokusnik_questions

            "Чем ты здесь занимаешься?" if not asked_fokusnik_job:
                $ asked_fokusnik_job = True
                LuVay "Я гей."
                jump fokusnik_questions

            "Ты что-то скрываешь?" if not asked_fokusnik_secret:
                $ asked_fokusnik_secret = True
                LuVay "Все мы что-то скрываем..."
                jump fokusnik_questions

            "Продолжить..." if asked_fokusnik_name and asked_fokusnik_job and asked_fokusnik_secret:
                jump fokusnik_continue
            
        label fokusnik_continue:
            LuVay "Приятно познакомиться!"
            hide fokusnik normal
            menu:
                "Уйти":
                    jump call_mapUI
    
label meeting_clown:
    show clown normal
    Fred "А?"
    hide clown normal
    $ met_characters[4] = True
    jump meeting_clown_continue
    
            
    label meeting_clown_continue:
        Fred "Ты что-то хотел?"
        hide clown normal
        menu:
            "Уйти":
                jump call_mapUI

label meeting_adam:
    show gg tired 1
    "Кажется, никого..."
    hide gg tired 1
    menu:
        "Уйти":
            jump call_mapUI

label meeting_hoz:
    show gg tired 1
    "Я бы не стал туда пока заходить..."
    hide gg tired 1
    menu:
        "Уйти":
            jump call_mapUI

label meeting_psina:
    show gg tired 1
    "Кажется, никого..."
    hide gg tired 1
    menu:
        "Уйти":
            jump call_mapUI


label meeting_dress:
    show gg tired 1
    "Кажется, никого..."
    hide gg tired 1
    menu:
        "Уйти":
            jump call_mapUI

label meeting_fire:
    if met_characters[5]:
        show psina normal
        Kyle "Проваливай."
        hide psina normal
        jump psina_continue
    else:
        default asked_psina_name = False
        default asked_psina_job = False
        default asked_psina_secret = False
        $ met_characters[5] = True
        $ psina.imageName = "characters/ava/psina ava.png"


        "Небольшой костёр потрескивал между трейлерами."
        "Возле огня сидел на сложенном ящике мой недавний знакомый. На этот раз в руке у него поблескивал длинный нож."
        "Он медленно водил лезвием по точильному камню."
        "Я уже думал развернуться и уйти, но сухая ветка предательски хрустнула под ногой."
        "Незнакомец поднял глаза."

        show psina normal
        Kyle "Снова ты, черт побери!"
        hide psina normal
        "Секунда — и рука его резко дёрнулась. Нож сверкнул в огне и полетел прямо в мою сторону."
        menu:
            "Отскочить в сторону.":
                $ itan.mercifulness += 5 
                "Я резко рванул вбок, и нож просвистел в воздухе, впившись в дерево позади."
                show psina normal
                Kyle "Ха. А я думал, совсем дурак."
                Kyle "Так чего же ты все еще здесь, раз за шкуру свою печешься?"
                Kyle "Второй раз не промахнусь."
                hide psina normal
                "Он медленно встал и потянулся за спину, туда, где в кобуре на поясе поблескивала еще одна рукоять."
            "Остаться на месте.":
                $ psina.affection += 5
                $ itan.guile += 5
                "Я замер, не шевельнувшись. Лезвие просвистело в каких-то сантиметрах от плеча и воткнулось рядом в землю."
                show psina normal
                Kyle "..."
                hide psina normal
                "Несколько секунд он молча сидел, пристально глядя на меня."
                show gg tired
                gg "{i}Видимо, ожидал, что я убегу, крича о помощи.{/i}"
                hide gg tired
                show psina normal
                Kyle "Не дрогнул... Ну-ну."
                Kyle "Видимо совсем парню страх отшибло."
                Kyle "Ну ничего, я тебе покажу, почему стоило слушать с самого начала."
                hide psina normal
                "Мужчина медленно встал, разминая кулаки."
        
        show gg tired
        gg "Уж не на твое ли место Мадам себе замену подыскивала?"
        hide gg tired
        "Мужчина остановился и прищурился."
        show psina normal
        Kyle "Что ты сказал?"
        hide psina normal
        show gg tired
        gg "Ты ж поэтому и взъелся, верно?"
        gg "Так знай: не я — другого проходимца найдут. Всех ведь не перепугаешь."
        hide gg tired
        show psina normal
        Kyle "Когда она успела?.."
        Kyle "Нет." 
        Kyle "Ах ты сукин сын."
        hide psina normal
        "Его как-будто бы осенило."
        show psina normal
        Kyle "Мадам Дюморье, черт бы ее подрал! Прямо у меня под носом, эта хитрая змея."
        Kyle "Еще и этого сопляка!" 
        Kyle "Что, небось уже заселился в дом Шона?"
        hide psina normal
        "Он шумно выдохнул, и снова сел у костра."
        show psina normal
        Kyle "Проваливай."
        hide psina normal
        "Я не стал спорить."
        jump psina_continue
            
        label psina_continue:
            hide psina normal
            menu:
                "Уйти":
                    jump call_mapUI

