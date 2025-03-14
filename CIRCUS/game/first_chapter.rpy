label start_forest:
    window hide
    play music "rain.mp3"
    scene bg rain night with dissolve
    show bg rain night at Transform(zoom=1.8)


    "Уже несколько дней погода не была благосклонна к живым существам."
    "Все небо затянули тучи, отчего казалось, что мир погрузился в вечную тьму, а косой дождь размывал дороги и забирался под одежду своими колючими каплями."
    "Ни один уважающий себя путник не высовывал в эти дни носу из дома или постоялого двора."
    "Кроме одного сумасшедшего упрямца."
    show gg tired
    gg "Меня."
    hide gg tired
    "Я промок до нитки и очень устал, но все равно продолжал шагать вперед назло непогоде."
    "Кожаная сумка с вещами казалась неимоверно тяжелой и тянула вниз, с каждой минутой все сильнее склоняя к соблазну свалиться в слякоть и уснуть прямо на дороге"
    "А бывший еще пару дней назад белым воротник рубашки смотрелся сейчас как облезлая шерсть бездомного кота"
    show gg tired
    gg "Если бы я знал, что начнётся шторм, то остался бы в том городе!"
    hide gg tired
    "Я ругаюсь на самого себя от невозможности сделать что-то со сложившейся ситуацией, но на самом деле, вернись я в прошлое, поступил бы точно также."
    "Деньги, запасенные на рискованное путешествие кончились слишком быстро, и еще одну ночь снимать комнату я просто не мог себе позволить."
    "Продолжая шагать по раскисшей дороге, я вдруг заметил впереди едва различимую фигуру, возящуюся у телеги, которая застряла на обочине."
    "Дождь так хлестал по глазам, что я сперва подумал, будто мне показалось, но фигура снова зашевелилась, подтверждая реальность увиденного."
    show farmer
    Farmer "Эй, там! Живой, или дух нечистый?"
    hide farmer
    show gg tired
    gg "Живой, живой!"
    hide gg tired
    show farmer
    Farmer "А вот телега моя, кажись, уже к праотцам собралась!"
    hide farmer
    "Подойдя ближе, я увидел, что одно из колес телеги скособочилось и выглядело так, будто готово развалиться."
    "Лошадь, казалось, тоже была на пределе сил, храпела и едва удерживалась на ногах. Мужчина сидел на корточках, разглядывая поврежденное колесо."
    show gg tired
    gg " Н-да... Веселое местечко для привала выбрал."
    gg "И что, дальше сам собрался это корыто тянуть?"
    hide gg tired
    "Мужик лишь вздохнул."

    window hide  # Hide the normal dialogue window
    $ renpy.pause(0.5)  

    show text "Герой может выбирать между путем милосердия и путем расчетливости." at truecenter
    $ renpy.pause(7)  # Time for the message to stay
    hide text

    show text "Милосердный герой склонен бескорыстно помогать окружающим. Он эмпатичен и лучше сходится с людьми." at truecenter
    $ renpy.pause(7)
    hide text

    show text "Расчетливый герой во всем видит выгоду. Он более изворотливый, ему легче дается договариваться." at truecenter
    $ renpy.pause(7)
    hide text

    show text "Выбери сейчас!" at truecenter
    $ renpy.pause(5)
    hide text

    window show  

    menu:
        "Ничего, вдвоем точно справимся.":
            $ itan.mercifulness += 5 
            show farmer
            Farmer "Ну, коли ты такой смелый, давай-ка помогай. А то сам, как видишь, уже в отчаянье."
            hide farmer
            show gg happy
            gg "Что ж, для начала давай телегу хоть немного приподнимем, а потом посмотрим."
            gg "Держу пари, телега ещё и грузом набита под завязку."
            show gg happy
            show farmer
            Farmer "А то! Там всё моё добро: мука, соль да крохотка овса для этой бедолаги"
            hide farmer
            "Мужчина махнул на лошадь."
            show farmer
            Farmer "Если всё тут брошу, считай, пиши пропало."
            hide farmer
            show gg happy
            gg "Значит, бросать нельзя."
            hide gg happy
            "Я кивнул, устраиваясь на колени рядом с колесом."
        "Помогу я тебе это колесо починить, но с одним условием.":
            $ itan.guile += 5
            show farmer
            Farmer "Ага, ага, условия у него... "
            hide farmer
            "Мужчина вытер грязь с лица."
            show farmer
            Farmer "Ну, валяй, говори, что хочешь. Всё одно, без твоей помощи я тут и сгнию. "
            hide farmer
            show gg happy
            gg "Мне ночлег нужен."
            gg "Хоть на сеновале каком, и крышу над головой."
            gg "И миску супа, если не жалко."
            gg "А то я скоро, как твоя лошадь, ноги протяну"
            show gg happy
            show farmer
            Farmer "Да ради бога! Чего хочешь, то бери, только чтоб до дома до ночи дотащились."
            hide farmer
            show gg happy
            gg "Вот и славно. А теперь подержи-ка эту рухлядь."
            hide gg happy
            "Я уже прикидывал, как быстрее справиться с работой."
    show gg happy
    gg "Готово."  
    hide gg happy      
    "Я выпрямился, хлопая ладонями по мокрым штанам"
    show farmer
    Farmer "Рукастый! "
    hide farmer
    "Путник обошел телегу и проверил колесо."
    show farmer
    Farmer "Пошли, пущу переночевать у меня в сенях."
    Farmer "Паршивая сегодня ночка будет, а ты, гляжу, совсем продрог."
    Farmer "Тебя как звать-то?"
    hide farmer
    "Я на секунду замер."
    "Использовать свое настоящее имя я не мог, а времени подумать над новым не было."
    python:
        name = renpy.input((""))
        itan.name = name
    if name.strip() == "":  
        $ name = "Луиджи" 
        $ itan.name = "Луиджи"
            
    define gg = Character("[name]", color="#ffffff")
    show gg tired
    gg "[name]"
    hide gg tired
    "Фермер хлопнул по месту рядом с собой, забираясь в телегу."
    show farmer
    Farmer "Вон, на козлы садись, [name], а то совсем скоро опять в грязь завязнем."
    Farmer "А ты, паря, чего по таким лужам бродишь? "
    hide farmer
    show gg tired
    gg "Работу ищу."
    gg "Хотел успеть в следующий город до ночи, но дождь планы спутал."
    hide gg tired
    show farmer
    Farmer "Работу, говоришь? Ну, если ты такой же ловкий и в других делах, есть тут на селе циркачи бродячие."
    Farmer "Да-да, не смотри так!"
    Farmer "Они тут каждую осень появляются. И главный у них всегда ищет помощников."
    hide farmer
    show gg happy
    gg "Циркачи? Смешной ты."
    gg "И чем, по-твоему, я им помогу? Летать через кольца или львов дрессировать?"
    hide gg happy
    "Крестьянин громко рассмеялся, откинув голову назад."
    show farmer
    Farmer "Не, парень, там и без тебя акробатов хватает."
    Farmer "Но такие, кто может телегу починить, шатёр поставить или фонарь настроить, — ценятся! А ты вроде из тех, кто может гвоздь забить."
    hide farmer
    "Я задумался."
    "Бродячий цирк, кочующий из города в город."
    "Никто и подумать не сможет, что искать меня стоит там."
    show gg tired
    gg "Ну, а где они сейчас? "
    hide gg tired
    show farmer
    Farmer "Недалеко, у леса лагерь разбили. Я тебя утром проведу. А пока ночуй у меня, обсохнешь, силы наберёшь."
    hide farmer
    "Я лишь усмехнулся в ответ, но идея застряла в его голове, словно заноза."
    scene bg rain day with dissolve
    show bg rain day at Transform(zoom=1.5)
    "На утро дождь только усилился."
    "Воздух был пропитан сыростью, а небо нависло тёмной пеленой, не оставляя надежды на просвет. "
    if (itan.mercifulness > 0 ):
        "На прощание, жена моего нового знакомого, видимо расчувствовавшись из-за рассказанной мужем истории, протянула мне кулёк."
        "В нём были картофель, сыр и кусок вяленого мяса — простой, но ценный подарок для того, кто не знает, где окажется к вечеру."
        python:
            renpy.notify("Предмет добавлен в инвентарь.")
            items.append("meal")
        "Крестьянин натянул на плечи потрёпанный плащ и мы отправились в путь."
    else:
        "Перед уходом крестьянин всучил мне пару монет, видимо решив, что этим жестом он закрывает наш долг."
        python:
            renpy.notify("Получено 5 монет.")
            money += 5
        "Я убрал монеты в карман и мы отправились в путь."
    "Дорога оказалась не из лёгких. Грязь цеплялась к сапогам, делая каждый шаг тяжелее."
    "Однако крестьянин уверенно вел меня через лес, не обращая внимания на погоду."
    "Наконец, сквозь завесу дождя показались первые очертания шатров. Силуэты их были смутными и неясными, едва различимыми в сыром сумраке."
    "Мой спутник останавлся и тяжело вздохнул."
    show farmer
    Farmer "Я дальше не пойду"
    Farmer "Честно, не по душе мне это место. Тут... эти циркачи не совсем обычные." 
    "Ну, береги себя, парень."
    hide farmer
    "Я кивнул в ответ, чувствуя, что не буду настаивать. Место и вправду вызывало какой-то странный холод в груди."
    "Атмосфера здесь явно не располагала к цирковому веселью, хотя, вероятно, такое впечатление сложилось из-за погоды"
    "Я прошагал еще сотню-другую шагов по размытой дождём дороге, когда впереди, разрезая темноту, замаячили огни фонарей."
    show gg tired
    gg "{i}Интересно, зачем делать стоянку так далеко от цивилизации?{/i}"
    hide gg tired
    "Я ускорил шаг, чтобы поскорее оказаться под крышей. Чем ближе я подходил, тем отчетливее становились очертания большого полосатого шатра."
    
    scene bg circus rain with dissolve
    show bg circus rain at Transform(zoom=3.1)

    "Вокруг шатра виднелись старые повозки с облупившейся краской, стоящие на неровной земле. Их колёса утопали в сырой почве"
    "Я заметил отблески пламени и поспешил туда."

    scene bg fire with dissolve
    show bg fire at Transform(zoom=1.9)

    "Костер распологался под навесом. У костра сидел мужчина."
    show gg happy
    gg "Добрый день!"
    hide gg happy
    show psina normal
    Kyle "Сегодня не выступаем."
    hide psina normal
    show gg tired
    gg "{i}Даже не повернулся.{/i}"
    hide gg tired
    show gg happy
    gg "Я ищу того, кто тут за главного. Мне нужна работа."
    hide gg happy
    "Мужчина наконец повернулся в мою сторону и окинул меня быстрым взглядом."
    show psina normal
    Kyle "Проваливай отсюда."
    hide psina normal
    show gg scared
    gg "Что?"
    hide gg scared
    show psina normal
    Kyle "Катись отсюда, что непонятного?"
    Kyle "Работы нет. И если сам не понимаешь, покажу тебе дорогу назад."
    hide psina normal
    "Он сжал кулаки. Такого теплого приветствия я не ожидал."
    show gg scared
    gg "Понял, и вам хорошего вечера."
    hide gg scared
    "Я развернулся и пошел назад."
    "Драться со всеми грубиянами на пути точно не входило в мои планы."
    "Но и сдаваться так просто я не собирался."
    "Я отошел на такое расстояние, чтобы скрыться за ближайшим трейлером и пошел по кругу, скрываясь за стеной дождя. "

    "Диалог с хозяйкой блаблабла"


    jump gg_pressed


    
    return
