# main

from Computer import Computer as comp
import random


# создаём список
type_list = ['ноутбук ', 'пк      ', 'моноблок']
RAM_list = [8, 12, 16, 24, 32]
processor_list = ['проц-1', 'проц-2']
comps = []
for i in range(10):
    comp_s = comp(type_list[random.randint(0,2)],       # comp_type
                 RAM_list[random.randint(0,4)],         # RAM
                 processor_list[random.randint(0,1)],   # processor
                 random.randint(100,111))               # price
    comps.append(comp_s)
# выводим список
for c in comps:
    c.show_all()


# price of selected
select_list_prices = [0, 9]     # первый и последний
price_selected = 0
print(f'\nобщая цена выбранных {select_list_prices}:')
for i in select_list_prices:
    price_selected += comps[i].get_price

print(price_selected)


# RAM 0-1
print(f'\nRAM по убыванию:')
for j in range(10):
    for i in range(len(comps)-1):
        if comps[i].get_RAM < comps[i+1].get_RAM:
            comps[i], comps[i+1] = comps[i+1], comps[i]

for c in comps:
    c.show_all()


# RAM 1-0
print(f'\nRAM по возрастанию:')
for j in range(10):
    for i in range(len(comps)-1):
        if comps[i].get_RAM > comps[i+1].get_RAM:
            comps[i], comps[i+1] = comps[i+1], comps[i]

for c in comps:
    c.show_all()


# one type
one_type = 'ноутбук '
print(f'\nодного типа "{one_type}":')
for i in comps:
    if i.get_comp_type == one_type:
        i.show_all()

