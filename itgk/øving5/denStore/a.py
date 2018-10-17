

#def yn(var, text, tellVar, neste):
#    var = input(text)
#    if var == "y":
#        global tellVar
#        tellVar +=1
#        neste
#    elif var == "n":
#        neste
#    else:
#        yn(var, text, tellVar, neste)

def tarFag(age):
    fag = input("Tar du noen fag? y/n\n")
    if fag == "y":
        global antall_fag
        antall_fag +=1
        tarITGK(age)
    elif fag == "n":
        tarITGK(age)
    else:
        tarFag(age)


def tarITGK(age):
    if age>=22:
        medlem_ITGK = input("Tar du virkelig ITGK? y/n\n")
    else:
        medlem_ITGK = input("Tar du ITGK? y/n\n")
    if medlem_ITGK == "y":
        global antall_ITGK
        antall_ITGK += 1
    elif medlem_ITGK == "n":
        pass
    else:
        tarITGK(age)


def tidLekser():
    timer_lekser = int(input("Hvor mange timer bruker du på lekser i snitt per dag?\n"))
    global antall_timer_lekser
    antall_timer_lekser += timer_lekser

def questionnaire():
    x=0
    while x<1:
        print("Velkommen til spørreundersøkelsen!")
        gender = input("Hvilket kjønn er du? m/f\n")
        if gender == "m":
            global antall_menn
            antall_menn += 1
        elif gender == "f":
            global antall_kvinner
            antall_kvinner +=1
        age = int(input("Hvor gammel er du?\n"))
        if age<=15 or age>=25:
            print("Du er er utenfor aldersgruppen")
            questionnaire()
        else:
            tarFag(age)
            #yn("fag", "Tar du noen fag? y/n\n", "antall_fag",tarITGK(age))
        tidLekser()
        x+=1
    global antall_timer_lekser
    antall_timer_lekser = antall_timer_lekser/( antall_kvinner+ antall_menn)
    print(antall_fag, antall_ITGK, antall_kvinner, antall_menn, antall_timer_lekser)
antall_menn = 0
antall_kvinner = 0
antall_fag = 0
antall_ITGK = 0
antall_timer_lekser = 0
x=0
questionnaire()
