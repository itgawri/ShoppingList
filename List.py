shopping_list = ["potato", "apple", "oil", "milk", "toilet paper"]
shopping_list.append("batteries")
shopping_list.insert(0, "chocolate")
shopping_list[0] = "dark chocolate"
shopping_list.pop()
print(shopping_list)

purchased_list = ["dark chocolate", "potato", "apple", "oil", "toilet paper", "fish fingers"]

unavailable_items = []
for item in shopping_list:
    if item not in purchased_list:
        unavailable_items.append(item)

if len(unavailable_items) > 0:
    print(f"Here's a list of items on your shopping list that you did not purchase: {unavailable_items}")
else:
    print(f"Good job! You bought everything on your shopping list!")

special_items = []
for item in purchased_list:
    if item not in shopping_list:
        special_items.append(item)

if len(special_items) > 0:
    print(f"Here's a list of items you purchased but were not on your shopping list: {special_items}")

# PL--------------------------------------------------------------------------------

lista_zakupow = ["ziemniak", "jablko", "olej", "mleko", "papier toaletowy"]
lista_zakupow.append("baterie")
lista_zakupow.insert(0, "czekolada")
lista_zakupow[0] = "gorzka czekolada"
lista_zakupow.pop()
print(lista_zakupow)

lista_zakupow_zakupione = ["gorzka czekolada", "ziemniak", "jablko", "olej", "papier toaletowy", "paluszki rybne"]

niedostepne_produkty = []
for produkt in lista_zakupow:
    if produkt not in lista_zakupow_zakupione:
        niedostepne_produkty.append(produkt)

if len(niedostepne_produkty) > 0:
    print(f"Oto lista produktów z Twojej listy zakupów, których nie zakupiłeś: {', '.join(niedostepne_produkty)}")
else:
    print(f"Dobra robota! Kupileś wszystko, co było na Twojej liście zakupóów!")

specjalne_produkty = []
for produkt in lista_zakupow_zakupione:
    if produkt not in lista_zakupow:
        specjalne_produkty.append(produkt)

if len(specjalne_produkty) > 0:
    print(f"Oto lista produktów, ktorę zakupiłeś, ale nie były na Twojej liście zakupów: {', '.join(specjalne_produkty)}")
