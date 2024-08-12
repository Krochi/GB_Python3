#Задание1:

# NV_videocart = int(input("Ведите кол-во видеокарт:"))
#
# videocart = []
# empty_list = -1
#
# for item in range(NV_videocart):
#     cart = int(input(f"Видеокарта {item + 1}:"))
#     videocart.append(cart)
#     if cart > empty_list:
#       empty_list = cart
#
# new_videocart = []
# for cart in videocart:
#     if cart != empty_list:
#         new_videocart.append(cart)
#
# print("Старый список видеокарт", videocart)
# print("Новый список видеокарт", new_videocart)


#Задание2:

# films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов",
#          "Мементо", "Отступники", "Деревня"]
# f_films = []
# films_num = input("Введите сколько фильмов, вы хотите посмотреть")
# for _ in range(int(films_num)):
#     my_films = input("Введите фильм: ")
#     if my_films in films:
#
#         f_films.append(my_films)
#     else:
#         print("Такого фильма нет!")
#
# print(f"Новый список фильмов:  {f_films}")

#Задание3:

# lst = [1, 4, -3, 0, 10]
#
# for i in range(len(lst) - 1):
#     for j in range(len(lst) - i - 1):
#         if lst[j] > lst[j + 1]:
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]
# print(lst)

#Задание4:

# good = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678'
# }
#
# store = {
#     '12345': [{'quantity': 27, 'price': 43},],
#     '23456': [{'quantity': 22, 'price': 510},
#               {'quantity': 32, 'price': 520},],
#     '34567': [{'quantity': 2, 'price': 1200},
#               {'quantity': 1, 'price': 1150},],
#     '45678': [{'quantity': 50, 'price': 100},
#               {'quantity': 12, 'price': 95},
#               {'quantity': 43, 'price': 97},],
# }
#
# for item_name, item_code in good.items():
#     total_quantity = 0
#     total_cost = 0
#
#     if item_code in store:
#         for entry in store[item_code]:
#             quantity = entry['quantity']
#             price = entry['price']
#             total_quantity += quantity
#             total_cost += price * quantity
#
#     print(f"{item_name} - {total_quantity} штук, стоимость - {total_cost} рублей")

#Задание5:

N = int(input("ВВедите кол-во заказов:"))

orders = {}
for i in range(N):
    order = input(f"{i + 1}-й заказ: ")
    parts = order.split(',')
    buyer = parts[0].strip()
    pizza = parts[1].strip()
    quantity = int(parts[2].strip())

    if buyer not in orders:
        orders[buyer] = {}

    if pizza not in orders[buyer]:
        orders[buyer][pizza] = 0
    orders[buyer][pizza] += quantity

for buyer in sorted(orders.keys()):
    print(f"{buyer}: ")
    for pizza in sorted(orders[buyer].keys()):
        print(f"{pizza}: {orders[buyer][pizza]}")