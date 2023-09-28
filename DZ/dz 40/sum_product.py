def goods_price(*dct, sum=0):
    for i in dct:
        dct2 = i
        for k, v in dct2.items():
            sum += v
    print(sum)


goods_price({'Кружка': 300, 'Стакан': 400, 'кофе 500 гр': 800})