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

    default met_characters = [False, False, False, False, True, False]
    default kitchen_first_visit = True

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
    jump kitchen_adam_meeting

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

    
        "Я подошел к арене и остановился у самого входа."
        "Запах сырой соломы ударил в ноздри, мгновенно вернув забытые образы."
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
        show gg smile 1
        gg "Прости. Я просто осматриваюсь. Я новенький. Только вчера прибыл."
        hide gg smile 1
        "Она скривилась, словно я сказал нечто запретное."
        show dress normal
        Mary "Тот самый прибывший, значит?"
        hide dress normal
        "Она отвернулась и что-то пробормотала себе под нос. Я не расслышал, но это звучало резко."
        show dress normal
        Mary "Наша Мадам, как обычно, без предупреждения..."
        hide dress normal
        "Она махнула рукой, словно отгоняя мысль, и резко сменила тон."
        show dress normal
        Mary "Ладно. Раз ты уже здесь, не стой как столб."
        Mary "Кто ты такой вообще? Откуда взялся?"
        hide dress normal
        "Я повторил свою легенду — ту, что рассказывал Мадам Дюморье, затем поинтересовался в ответ."
        jump mary_questions

    label mary_questions:
        menu:
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
                show dress happy
                Mary "Ага! Вот мои лохматые артисты."
                hide dress happy
                "Её голос сразу стал теплее, и в глазах мелькнул огонёк гордости."
                show dress happy
                Mary "Полосатые, усатые, зубастые."
                Mary "Ты не бойся, они на людей не бросаются. Как правило."
                hide dress happy
                "Она усмехнулась, явно наслаждаясь моей реакцией."
                jump mary_questions

            "Давно ты здесь?" if not asked_mary_secret:
                $ asked_mary_secret = True
                show dress normal
                Mary "Ха! Достаточно, чтоб не ходить всюду с открытым ртом, как ты сейчас."
                Mary "А остальное — не твоё собачье дело, понял?"
                hide dress normal
                jump mary_questions

            "Продолжить..." if asked_mary_name and asked_mary_job and asked_mary_secret:
                jump mary_questions_continue
        
        label mary_questions_continue:
            "Со стороны раздался рык. Я не видел, но чувствовал, как за мной кто-то хищно наблюдает."
            show dress normal
            Mary "Ладно, новенький. Меня тут уже заждались."
            Mary "Не мешай, если не хочешь попасть под горячую руку."
            hide dress normal
            "Она кивнула в сторону клетки, где из темноты на меня уставились жёлтые глаза."
            show dress happy
            Mary "Если будет нечем заняться, загляни позже. Может, покажу тебе, как тут всё устроено."
            hide dress happy
            "Я молча кивнул и радостно подвинулся к выходу."
            jump mary_continue

        label mary_continue:   
            menu:
                "Уйти":
                    jump meeting_gg_pressed


label meeting_warehouse:
    if met_characters[1]:
        show adam normal
        Adam "Привет еще раз!"
        jump adam_continue
    else:
        default asked_adam_glavny = False
        default asked_adam_job = False
        $ met_characters[1] = True
        $ adam.imageName = "characters/ava/adam ava.png"

        "Я открыл дверь кладовки. Внутри пахло пылью, старым деревом и разлитым маслом"
        "Среди хлама кто-то копался, склонившись над разбросанными ящиками."
        show adam normal
        Adam "Ох! Напугал... Редко сюда кто-то заглядывает."
        Adam "Снова здравствуй! [name], верно?"
        Adam "Ты меня прости, вчера наше знакомство не задалось. С сегодняшнего дня буду стараться лучше. Я Адам."
        hide adam normal
        #----------------
        $ adam.name = "Адам"
        $ Adam.name = "Адам"
        #----------------
        "Он протянул руку и очень крепко пожал мою, расплываясь в улыбке. Его ладонь была грубая и мозолистая, как у человека, привыкшего к труду."
        show adam normal
        Adam "Как ты устроился? Печь греет исправно? Я пару раз заглядывал проверить, пока вагончик пустовал."
        hide adam normal
        show gg smile 1
        gg "Спасибо, жаловаться не на что."  
        hide gg smile 1

        label adam_questions:
        menu:
            "Ты здесь вроде как за главного?" if not asked_adam_glavny:
                $ asked_adam_glavny = True
                show gg smile 1
                gg "По всеми вопросами, как я понял, всегда к тебе?"  
                hide gg smile 1
                show adam normal
                Adam "У нас тут нет главных. Каждый делает своё дело. Я всего лишь помогаю по хозяйству, не более."            
                Adam "Я всегда любил чинить вещи, а здесь моё маленькое увлечение еще и упрощает людям жизнь."
                hide adam normal

                jump adam_questions

            "Тебе не нужен помощник?" if not asked_adam_job:
                $ asked_adam_job = True
                show gg smile 1
                gg "{i}Не очень понял, что он за персонаж, но устраиваться нужно.{/i}"  
                hide gg smile 1
                show adam normal
                Adam "Не пойми неправильно, но у меня довольно специфичная профессия."
                Adam "Я, скажем так, таскаю тяжести на сцене."
                Adam "Не думаю, что ты мог бы чем-то подсобить. Это не в обиду, конечно."
                hide adam normal
                show gg confused 1
                gg "..."  
                gg "{i}Силач, значит?{/i}"  
                hide gg confused 1
                show gg confused 2
                "Я невольно перевёл взгляд на его фигуру. Да, мой новый знакомый был, несомненно, в хорошей форме, но явно не тот человек, которого я представлял на эту роль." 
                "Ни гигантских бицепсов, ни устрашающей ширины плеч, он был самым обычным мужчиной."
                hide gg confused 2
                show gg shy 1
                gg "{i}Чёрт, мы слишком долго молчим, а я пялюсь не туда.{/i}"
                hide gg shy 1
                jump adam_questions

            "Продолжить..." if asked_adam_glavny and asked_adam_job:
                show adam normal
                Adam "У меня есть небольшая просьба. Всё утро тут роюсь, а все никак не могу найти запасные винты для колеса. Без них мы отсюда никуда не уедем."
                hide adam normal
                "Он раскрыл ладонь и показал мне большой металлический винт." 
                show adam normal
                Adam "Если вдруг где-то увидишь такие, дай знать."
                hide adam normal
                show gg smile 1
                gg "Обязательно. И не буду дальше отвлекать."  
                hide gg smile 1
                jump adam_continue
            
        label adam_continue:
            if not kitchen_first_visit:
                show gg smile 1
                gg "Кстати, ты случайно не знаешь, где ключ от кухни?"  
                hide gg smile 1
                show adam normal
                Adam "Он у меня, но сейчас не с собой. Если ты не против, я тут кое-что доделаю и скоро присоединюсь к тебе за обедом."
                hide adam normal
                show gg smile 1
                gg "{i}Ладно, пока похожу по округе и осмотрюсь.{/i}"  
                hide gg smile 1

            Adam "До встречи!"
            hide adam normal
            menu:
                "Уйти":
                    jump meeting_gg_pressed

label meeting_food:
    
    if kitchen_first_visit: 
        "Я добрел до столовой, однако дверь оказалась заперта."  
        "За мутным стеклом не было видно ни души."  
        show gg tired 1
        gg "Закрыто..."  
        hide gg tired 1
        "Похоже, без ключа внутрь не попасть. Придётся разузнать, у кого он."  
        window hide 
        $ renpy.pause(0.5)  
        show text "Найди ключ от столовой." at truecenter
        $ renpy.pause(4) 
        hide text
        $ kitchen_first_visit = False
    else:
        "Дверь по‑прежнему закрыта."  
        show gg tired 1
        gg "А я все еще не нашел ключ."  
        hide gg tired 1

    menu:
        "Уйти":
            jump meeting_gg_pressed

label meeting_gymnastka:
    if met_characters[2]:
        show gymnastka normal
        Charlotte "Снова ко мне?"
        hide gymnastka normal
        jump charlotte_continue
    else:
        default asked_gymnastka_name = False
        default asked_gymnastka_job = False
        default asked_gymnastka_secret = False
        $ met_characters[2] = True
        $ gymnastka.imageName = "characters/ava/gymnastka ava.png"

        "Чуть вдалеке от моего трейлера затесался другой. У его крыльца, скрестив ноги на ступеньке, сидела девушка в голубом платье старомодного покроя."
        "Она казалась почти кукольной: с осиной талией, узкими плечами и огромной копной волос."
        "Тихо напевая себе под нос, она словно не замечала, что кто-то приближается. Когда я подошёл ближе, она подняла голову."
        show gymnastka normal
        Charlotte "Привет, [name]."
        hide gymnastka normal
        show gg smile 1
        gg "Здравствуй! Ты уже знаешь моё имя?"  
        hide gg smile 1
        show gymnastka normal
        Charlotte "У нас не так часто новенькие, чтобы не поинтересоваться."
        Charlotte "Я заметила тебя вчера из окна. Выглядел ты довольно потрёпанным."
        hide gymnastka normal
        "Я усмехнулся."
        show gg smile 1
        gg "Долгая дорога."  
        hide gg smile 1

        label gymnastka_questions:
        menu:
            "А как твоё имя?" if not asked_gymnastka_name:
                $ gymnastka.name = "Шарлотта"
                $ Charlotte.name = "Шарлотта"
                $ asked_gymnastka_name = True
                show gymnastka normal
                Charlotte "Шарлотта."
                hide gymnastka normal
                jump gymnastka_questions

            "Ты здесь выступаешь?" if not asked_gymnastka_job:
                $ asked_gymnastka_job = True

                show gymnastka normal
                Charlotte "Конечно, как и все вокруг."
                Charlotte "Давай, угадай, в каком жанре. У тебя одна попытка."
                hide gymnastka normal
                show gg confused 2
                gg "{i}А какие жанры я знаю?{/i}"
                hide gg confused 2

                menu:   
                    "Акробатика на лошадях?":
                        $ gymnastka.affection += 5
                        show gymnastka smile
                        Charlotte "Звучит прелестно! Всегда хотела попробовать, но Мэри запрещает."
                        Charlotte "Ты не угадал. Я - гимнастка."
                        hide gymnastka smile                    
                    "Балет?":
                        show gymnastka smile
                        Charlotte "Я люблю танцевать, но мы же в цирке!"
                        Charlotte "Ты не угадал. Я - гимнастка."
                        hide gymnastka smile
                    "Воздушная гимнастка?":
                        $ gymnastka.affection += 5
                        show gymnastka smile
                        Charlotte "Не совсем. Мой жанр - женщина-каучук."
                        hide gymnastka smile
                        show gg scared 1
                        gg "Ни разу не слышал такое название."
                        hide gg scared 1
                        show gymnastka smile
                        Charlotte "Это меня Лю Вэй научил. Раньше я тоже считала, что обычная гимнастка."
                        hide gymnastka smile
                    "Фокусы?":
                        show gymnastka smile
                        Charlotte "Иногда я залезаю в маленький куб, а Лю Вэй втыкает в меня кинжалы."
                        Charlotte "Но нет, ты не угадал. Я - гимнастка."
                        hide gymnastka smile 

                show gymnastka smile
                Charlotte "Ты ошибся, [name]. А значит, теперь ты мне что-то должен."
                hide gymnastka smile
                show gg confused 1
                gg "Вот как? И что же ты хочешь?"
                hide gg confused 1
                show gymnastka normal
                Charlotte "Загадаю желание. Но не сейчас... пусть будет сюрприз."
                Charlotte "Расслабься, я не жестокая."
                hide gymnastka normal
                jump gymnastka_questions

            "Давно ты работаешь с Мадам Дюморье?" if not asked_gymnastka_secret:
                $ asked_gymnastka_secret = True
                "Она на время задумалась, нахмурила брови. Что-то шептала, загибала пальцы и, наконец, ответила."
                show gymnastka normal
                Charlotte "Да."
                hide gymnastka normal
                jump gymnastka_questions

            "Продолжить..." if asked_gymnastka_name and asked_gymnastka_job and asked_gymnastka_secret:
                show gymnastka normal
                Charlotte "Знаю, ты ещё не определился с направлением, но могу дать тебе совет на будущее."
                Charlotte "Если ты так и продолжишь спать до обеда, то ничему не научишься. Самые лучшие тренировки начинаются до восхода солнца."
                hide gymnastka normal
                show gg confused 1
                gg "Откуда ты знаешь, во сколько я встаю?"
                hide gg confused 1
                "Она лишь мягко усмехнулась и изящно пожала плечами, будто это был глупый вопрос."
                show gymnastka normal
                Charlotte "Мне пора. Сегодня мой черёд идти на рынок."
                hide gymnastka normal
                show gg smile 1
                gg "Спасибо за совет. И за компанию."
                hide gg smile 1
                show gymnastka normal
                Charlotte "Было приятно познакомиться."
                hide gymnastka normal
                "С этими словами она легко вскочила и направилась прочь."
                jump charlotte_continue
        label charlotte_continue:
            hide gymnastka normal
            menu:
                "Уйти":
                    jump meeting_gg_pressed
    

label meeting_fokusnik:
    if met_characters[3]:
        show fokusnik normal
        LuVay "Уже соскучился?"
        hide fokusnik normal
        jump fokusnik_continue
    else:
        default asked_fokusnik_name = False
        default asked_fokusnik_job = False
        default asked_fokusnik_help = False
        
        $ met_characters[3] = True
        $ fokusnik.imageName = "characters/ava/fokusnik ava.png"

    
        "На пороге у трейлера сидел мужична в костюме и циллиндре, будто бы готовый хоть сейчас выйти на сцену."
        "Он издалека наблюдал за тем, как я подхожу и широко улыбнулся, когда я поздоровался и наши взгляды встретились."
        show fokusnik normal
        LuVay "Рад удостовериться, что слухи не врут. Приветствую, наша новая звезда."
        hide fokusnik normal
        show gg smile 1
        gg "Какими же слухами я уже успел обзавестись?"  
        hide gg smile 1
        show fokusnik normal
        LuVay "О, я слышал только лишь о том, что вчера в наши ряды затесался симпатичный молодой человек."
        hide fokusnik normal
        show gg smile 1
        gg "Очень лестные слова. В лицо я получил лишь пару угроз вышвырнуть меня отсюда."  
        hide gg smile 1
        show fokusnik normal
        LuVay "О, Кайл со всеми такой, не принимай близко к сердцу."
        #--------------
        $ psina.name = "Кайл"
        $ Kyle.name = "Кайл"
        #--------------
        LuVay "А ты у нас..?"
        hide fokusnik normal
        show gg smile 1
        gg "Меня зовут [name]."  
        hide gg smile 1

        label fokusnik_questions:
        menu:
            "Как твоё имя?" if not asked_fokusnik_name:
                #--------------
                $ fokusnik.name = "Лю Вэй"
                $ LuVay.name = "Лю Вэй"
                #--------------
                $ asked_fokusnik_name = True
                show fokusnik normal
                LuVay "Лю Вэй."
                hide fokusnik normal
                "Он медленно поднялся и протянул мне руку для рукопожатия."
                show fokusnik normal
                LuVay "Какая удивительно гладкая кожа. Редко такую встретишь у простых работяг в наших краях."
                LuVay "Какого королевства вы наследник, юный господин?"
                hide fokusnik normal
                "Я почувствовал, как к щекам прилила кровь и поспешно отдёрнул руку."
                show gg shy 1
                gg "{i}Нужно сменить тему.{/i}"
                hide gg shy 1

                jump fokusnik_questions

            "Чем ты здесь занимаешься?" if not asked_fokusnik_job:
                $ asked_fokusnik_job = True
                "Вместо ответа мой собеседник потянулся рукой к своему циллиндру. Секунда - и..."
                show fokusnik krolik 2
                LuVay "Творю чудеса."
                hide fokusnik krolik 2
                "Он вытащил из шляпы белого пушистого кролика, который тут же зашевелил ушами и прильнул обратно к шляпе."
                "Я не смог сдержать удивленного выдоха."
                show gg scared 1
                gg "{i}Он что, всё это время держал его там?{/i}"
                gg "Ты фокусник?"
                hide gg scared 1
                show fokusnik krolik 2
                LuVay "Называй меня как хочешь: фокусником, иллюзионистом... Некоторые даже зовут магом. Хотя я считаю себя простым творцом искусства."
                hide fokusnik krolik 2
                "Он отпустил кролика на землю и тот понёсся в направлении леса."
                jump fokusnik_questions
            
            "Я сейчас в поиске, чем мог бы быть полезен." if not asked_fokusnik_help:
                $ asked_fokusnik_help = True
                show gg smile 1
                gg "Не хочу просто болтаться без дела."
                hide gg smile 1
                show fokusnik normal
                LuVay "Тогда ты удачно зашёл."
                LuVay "Я как раз ищу ассистента."
                LuVay "Мой новый трюк с распиливанием пока, скажем так, не до конца отточен, а место в ящиках с предыдущими добровольцами заканчивается."
                hide fokusnik normal
                show gg confused 1
                gg "{i}Кажется, у него своеобразное чувство юмора.{/i}"
                gg "Я ещё подумаю. Сегодня хотелось бы дожить до обеда."
                hide gg confused 1
                jump fokusnik_questions

            "Продолжить..." if asked_fokusnik_name and asked_fokusnik_job and asked_fokusnik_help:
                show fokusnik normal
                LuVay "Раз уж мы расправшиваем друг друга, позволь узнать, откуда ты, [name]?"
                hide fokusnik normal
                show gg smile 1
                gg "О, я издалека. Маленький, ничем не примечательный городок на дальнем севере."
                gg "Но я уже давно не бываю там, с тех пор, как начал путешевствовать."
                hide gg smile 1
                show fokusnik normal
                LuVay "Прекрасно, люблю народы севера и их нрав."
                LuVay "Жаль, тебе не передался их очаровательный говор."
                hide fokusnik normal
                show gg confused 1
                gg "Кхм."
                hide gg confused 1
                show fokusnik normal
                LuVay "В любом случае, рад был знакомству, [name]. Я всегда здесь, если захочется... прикоснуться к настоящей магии."
                hide fokusnik normal
                "Он плавно приподнял шляпу в вежливом жесте, подмигнул мне на прощание и вернулся в свой трейлер."
                show fokusnik normal
                LuVay "Ну, до встречи, принцесса."
                hide fokusnik normal
                show gg confused 1
                gg "..."
                gg "Прикоснуться к магии?"
                hide gg confused 1
                jump fokusnik_continue
            
        label fokusnik_continue:
            menu:
                "Уйти":
                    jump meeting_gg_pressed
    
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
                jump meeting_gg_pressed

label meeting_adam:
    show gg tired 1
    "Кажется, никого..."
    hide gg tired 1
    menu:
        "Уйти":
            jump meeting_gg_pressed

label meeting_hoz:
    show gg tired 1
    "Я бы не стал туда пока заходить..."
    hide gg tired 1
    menu:
        "Уйти":
            jump meeting_gg_pressed

label meeting_psina:
    show gg tired 1
    "Кажется, никого..."
    hide gg tired 1
    menu:
        "Уйти":
            jump meeting_gg_pressed


label meeting_dress:
    show gg tired 1
    "Кажется, никого..."
    hide gg tired 1
    menu:
        "Уйти":
            jump meeting_gg_pressed

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

        show psina attack
        Kyle "Снова ты, черт побери!"
        hide psina attack
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
                show gg tired 1
                gg "{i}Видимо, ожидал, что я убегу, крича о помощи.{/i}"
                hide gg tired 1
                show psina normal
                Kyle "Не дрогнул... Ну-ну."
                Kyle "Видимо совсем парню страх отшибло."
                Kyle "Ну ничего, я тебе покажу, почему стоило слушать с самого начала."
                hide psina normal
                "Мужчина медленно встал, разминая кулаки."
        
        show gg tired 1
        gg "Уж не на твое ли место Мадам себе замену подыскивала?"
        hide gg tired 1
        "Мужчина остановился и прищурился."
        show psina normal
        Kyle "Что ты сказал?"
        hide psina normal
        show gg tired 1
        gg "Ты ж поэтому и взъелся, верно?"
        gg "Так знай, не я — другого проходимца найдут. Всех ведь не перепугаешь."
        hide gg tired 1
        show psina attack
        Kyle "Когда она успела тебе всё это сказать?"
        Kyle "..."
        Kyle "Ах ты сукин сын."
        hide psina attack
        "Его как-будто бы осенило."
        show psina attack
        Kyle "Мадам Дюморье, черт бы ее подрал! Прямо у меня под носом, эта хитрая змея."
        Kyle "Еще и этого сопляка!" 
        Kyle "Что, небось уже заселился в дом Шона?"
        hide psina attack
        "Он шумно выдохнул, и, не дожидаясь ответа, снова сел у костра."
        show psina normal
        Kyle "Проваливай."
        hide psina normal
        "Я не стал спорить."
        jump psina_continue
            
        label psina_continue:
            hide psina normal
            menu:
                "Уйти":
                    jump meeting_gg_pressed

