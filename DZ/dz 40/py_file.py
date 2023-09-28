def goods(*tpl, dct={}):
    for i in tpl:
        tpl2 = i
        dct[tpl2[0]] = tpl2[1]
    print(dct)


goods(("Кружка", 300), ("Стакан", 400), ("кофе 500 гр", 800))