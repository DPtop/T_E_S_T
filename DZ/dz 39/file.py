def finil_price(price:int, weight:int, measure:str):
    if measure == "г":
        return weight / 1000 * price
    elif measure == "кг":
        return weight * price


price = int(input("укажите стоимость: "))
weight = int(input("укажите вес: "))
measure = input("укажите меру веса(г/кг): ")
print("итоговая цена:", finil_price(price, weight, measure))
