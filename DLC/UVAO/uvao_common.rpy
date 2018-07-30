﻿#DLC, активируется флагом alt_dlc_active

label alt_day1_uvao_ch1:
    if not (herc or loki):
        th "Где же мы с ней разминулись?"
        "Я попытался восстановить события:"
        th "Сначала тень, метнувшаяся от столовой, потом площадь с Гендой, потом… да и все.{w} Куда угодно могла шмыгнуть!"
        "Следопыт из меня получился не очень. Самому бы теперь выбраться…"
        $ alt_day1_chase_uvao = True
    return

label alt_day1_uvao_ch2:
    th "Я ж забыл, о чем вообще с ней собирался поговорить!"
    me "Лена, я вот еще что спросить хотел…"
    un "О чем?"
    me "Генда этот, весь день на него смотрю… Ты не знаешь кто это?{w} Чем знаменит?"
    show un surprise pioneer with dspr
    "На меня посмотрели странно. {w}Как на ребенка, спросившего «Тетя, а что это за большая светящаяся штука в небесах?»."
    "Повисла неловкая тишина."
    show un shy pioneer with dspr
    un "Я п-пойду? {w}Поздно уже…"
    hide un with dissolve
    "Не дожидаясь ответа, она поднялась со скамейки и ушла, украдкой на меня поглядывая."
    th "Вот теперь я прочно занял роль местного психа."
    play sound sfx_hiding_in_bush
    "Вдруг позади меня хрустнула ветка. Я обернулся и, кажется, успел заметить чью-то тень!"
    "Секунда - и как ничего не бывало."
    th "Наверно, малышня…"
    "Вздохнув, я поднялся и побрел в сторону домиков."
    $ alt_day1_genda_investigation = True
    stop music fadeout 4
    $ renpy.pause(3)
    window hide
    return
    
label alt_day3_uvao_ch3:
    if alt_day1_genda_investigation and (len(list_d2_date_7dl) == 0) and max(lp_us,lp_dv,lp_un,lp_mi,lp_sl) <= 5:
        menu:
            "Сбежать!":
                "Мысли тревожно заметались. {w} Танцевать не хотелось категорически, да и сосредоточиться на плане дальнейших действий танец бы только помешал, особенно вкупе со странным поведением вожатой." 
                "Решение, как всегда, нашлось своеобразное и эффективное."
                me "Ольга Дмитриевна, что-то живот у меня…"
                "Для достоверности я скрючился и взялся за якобы страдающий живот обеими руками."
                show mt normal dress with dissolve
                "Лицо моей несостоявшейся партнерши по танцам выражало сложную смесь недоверия, разочарования и беспокойства."
                mt "Беги уж, страдалец. Может, Виолу попросить потом в медпункт вернуться?"
                "Я энергично помотал головой и полетел в сторону туалета."
                hide mt with dissolve
                window hide
                play ambience ambience_camp_center_night fadein 5
                scene bg ext_dining_hall_away_night
                with dissolve
                th "Фух, оторвался."
                dreamgirl "Ну ты даешь! Такую даму бортануть!{w} Ты что, ослеп и оглох, упускать подобное? Поиметь вожатую!{w} Все, знать тебя не знаю!"
                th "Оставь меня, старушка, я в раздумьях.{w} Тебе, может быть, и по барабану, где я оказался, но мне-то явно нет. И где, и почему, и когда…"
                dreamgirl "Так точно, мон женераль, все силы на раскрытие заговора по перемещению Семенов в пространстве и времени!"
                "Под этот разговор я сел прямо на траву и неспешно озирал окрестности, собирая мысли в кучку."
                "Исчезающие на глазах тени, странности в поведении местных обитательниц…"
                show uv shade2 at right with dissolve
                $ renpy.pause(.3)
                hide uv with easeoutright
                "Додумать я эту мысль не успел, потому как мое внимание привлек темный силуэт, залезающий в окно столовой."
                window hide
                scene bg ext_dining_hall_away_night_uvao2_7dl with dissolve
                play music music_list["mystery_girl_v2"] fadein 3
                th "Алиса!"
                "Пришло в голову очевидное объяснение."
                th "И не первый раз уже!"
                dreamgirl "Может ее того… Припугнуть немного?"
                "Идея припугнуть ДваЧе была достаточно привлекательной, чтобы вынудить меня подняться с насиженного места и начать тихо подбираться к приоткрытому окну."
                window hide
                scene bg ext_dining_hall_away_night_uvao2_7dl:
                    xalign 0.5 yalign 0.5 zoom 1.0
                    linear 1.0 zoom 2.0 xalign 0.7 yalign 0.5
                "Примерно на половине пути окно опять распахнулось и тень начала выбираться."
                "Я только вознамерился окликнуть Алису, как заметил явное несоответствие по ряду пунктов."
                "Во-первых, девушка была явно пониже и пофигуристей, {w} во-вторых, одета она была не в пионерскую форму,{w} а в-третьих…"
                "Для осознания этого «в-третьих» я глубоко вдохнул и присмотрелся еще раз. Да, у нее действительно были кошачьи уши и аккуратный хвост!"
                dreamgirl "Вау, значит, такой маскарад и при совке был популярен!"
                window hide
                scene bg ext_dining_hall_away_night_uvao1_7dl with dissolve:
                    zoom 2.0 xalign 0.7 yalign 0.5
                "Силуэт дернул ухом и скрылся в тенях за углом столовой. Я остолбенел."
                window hide
                scene bg ext_dining_hall_away_night with dissolve:
                    zoom 2.0 xalign 0.7 yalign 0.5
                    linear 1.0 zoom 1.0 xalign 0.5 yalign 0.5
                th "Он сейчас что?"
                dreamgirl "Вот они, минусы юности! От гормонов уже глюки начинаются."
                th "И окно от ветра открывалось? Нет, кто-то тут явно был."
                dreamgirl "Что же ты ее на «кис-кис-кис» не подозвал?"
                th "Ха-ха, как смешно."
                dreamgirl "А если серьезно – это уже диагноз, друг ситный. {w} Надо было тебе меньше аниме смотреть и хентайной манги почитывать."
                th "Но я же полностью нормальный…"
                dreamgirl "…и справка есть, знаю.{w} А еще ты разговариваешь с голосом у себя в голове и находишься в пионерлагере самого что ни на есть советского времени. {w}С шестнадцатилетними пионерками. Нафиг-нафиг."
                "Я оторвал остановившийся взгляд от стены столовой и побрел к себе в домик. Увиденное требовало осмысления, причем осмысления по возможности свежей головой."
                $ alt_day3_uvao_spotted = True
                stop music fadeout 3
                stop ambience
                window hide
            "Остаться.":
                 pass
    return

label alt_day3_uvao_ch4:
    "Странное существо возле столовой…"
    return