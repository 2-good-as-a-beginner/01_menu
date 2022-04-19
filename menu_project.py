# intro
# menu project is creating to allow any restaurant manager to set menu, edit it (dishes/products and price$), etc.
# how many functionalities will this programme have? who knows!? it can be improved any time and i hope, it will :)


# 1st step - importing csv library allowing .csv files import/export
import csv


# 2nd step - creating 4 variables - lists - empty at the beginning
dishes_number = []
dishes_list = []
dishes_currency = []
dishes_prices = []


# 3rd step - creating function reading data from .csv file
def import_dishes_list():
    with open('menu.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        j = 0
        for row in csv_reader:
            if j == 0:
                j += 1
            else:
                dish_nr = row[0]
                dish_name = row[1]
                dish_cur = row[2]
                dish_price = row[3]
                dish_nr.lower()
                dish_name.lower()
                dish_cur.lower()
                dish_price.lower()
                dishes_number.append(dish_nr)
                dishes_list.append(dish_name)
                dishes_currency.append(dish_cur)
                dishes_prices.append(dish_price)
                j += 1


# 4th step - creating function printing data from .csv file
def view_dishes_list():
    print()
    for i in range(len(dishes_list)):
        print(f'{dishes_number[i]}. {dishes_list[i].upper()}   {dishes_currency[i]}{dishes_prices[i]}')
        i += 1


# 5th step - creating function allowing adding values to menu and appending data to .csv file
def add_dishes():
    dish_name = input(f'\nType the name of the dish you want to add to your menu: >>> ')
    if dish_name.lower() not in dishes_list:
        if dish_name.lower() == '':
            print('You have typed nothing :(')
        elif dish_name.lower() != '':
            dish_price = input(f'And now type its price in [$]: >>> ')

            def check_float():
                try:
                    float(dish_price)
                    return True
                except ValueError:
                    return False

            if check_float() is False and dish_price != '':
                print('The price must be a number (not text).')
            elif check_float() is False and dish_price == '':
                print('You have typed nothing :(')
            elif check_float() is True and float(dish_price) <= 0:
                print('The price must be bigger than 0.')
            elif check_float() is True and float(dish_price) > 0:
                last_dish_nr_so_far = int(dishes_number[-1])
                next_dish_nr = str(last_dish_nr_so_far + 1)
                dishes_number.append(next_dish_nr)
                dishes_list.append(dish_name.lower())
                dishes_currency.append('$')
                dishes_prices.append(dish_price)
                print(f'{dish_name.upper()} has just been added to your menu.')
                with open('menu.csv', 'a', newline='') as file:
                    csv_appender = csv.writer(file, delimiter=';')
                    csv_appender.writerow([next_dish_nr, dish_name.lower(), '$', dish_price])
    elif dish_name.lower() in dishes_list:
        print(f'{dish_name.upper()} has already been added to your menu.')


# 6th step - creating function allowing modifying values in menu and writing data to .csv file
def edit_dishes_price():
    dish_name = input(f'\nType the name of the dish which price you want to change: >>> ')
    if dish_name.lower() not in dishes_list and dish_name.lower() != '':
        print(f'{dish_name.upper()} has not already been added to your menu.')
    elif dish_name.lower() not in dishes_list and dish_name.lower() == '':
        print('You have typed nothing :(')
    elif dish_name.lower() in dishes_list:
        dish_price_new = input(f'Type the new price of {dish_name.upper()}: >>> ')

        def check_float():
            try:
                float(dish_price_new)
                return True
            except ValueError:
                return False

        if check_float() is False and dish_price_new == '':
            print('You have typed nothing :(')
        elif check_float() is False and dish_price_new != '':
            print('The price must be a number (not text).')
        elif check_float() is True and float(dish_price_new) <= 0:
            print('The price must be bigger than 0.')
        elif check_float() is True and float(dish_price_new) > 0:
            for i in range(len(dishes_list)):
                if dishes_list[i] == dish_name.lower() and dishes_prices[i] == dish_price_new:
                    print(f'You have not changed the price of {dish_name.upper()}.')
                elif dishes_list[i] == dish_name.lower() and dishes_prices[i] != dish_price_new:
                    dishes_prices[i] = dish_price_new
                    print(f'The new price of {dishes_list[i].upper()} is ${dish_price_new}.')
                else:
                    i += 1
            with open('menu.csv', 'w', newline='') as file:
                csv_overwriter = csv.writer(file, delimiter=';')
                csv_overwriter.writerow(['number', 'dishes list', 'currency', 'dishes prices'])
                for k in range(len(dishes_list)):
                    csv_overwriter.writerow(
                        [dishes_number[k], dishes_list[k], dishes_currency[k], dishes_prices[k]])
                    k += 1


# 7th step - creating function allowing removing values in menu and writing data to .csv file
def remove_dishes():
    dish_name = input(f'\nType the name of the dish you want to remove from your menu: >>> ')
    if dish_name.lower() in dishes_list:
        remove_dish_index = dishes_list.index(dish_name.lower())
        dishes_number.remove(dishes_number[remove_dish_index])
        dishes_list.remove(dishes_list[remove_dish_index])
        dishes_currency.remove(dishes_currency[remove_dish_index])
        dishes_prices.remove(dishes_prices[remove_dish_index])
        for x in range(remove_dish_index,len(dishes_number)):
            dishes_number[x] = int(dishes_number[x])-1
            x -= 1
        with open('menu.csv', 'w', newline='') as file:
            csv_overwriter = csv.writer(file, delimiter=';')
            csv_overwriter.writerow(['number', 'dishes list', 'currency', 'dishes prices'])
            for k in range(len(dishes_list)):
                csv_overwriter.writerow(
                    [dishes_number[k], dishes_list[k], dishes_currency[k], dishes_prices[k]])
                k += 1
        print(f'{dish_name.upper()} has already been removed from your menu.')
    elif dish_name.lower() not in dishes_list and dish_name.lower() == '':
        print('You have typed nothing :(')
    elif dish_name.lower() not in dishes_list and dish_name.lower() != '':
        print(f'{dish_name.upper()} has not already been added to your menu.')


# 8th step - calling functions: firstly, importing data from .csv once user running the programme;
#            afterwards - infinite loop allowing calling other functions
import_dishes_list()
while True:
    print('\nWelcome to the menu!')
    print('Type 1 to see the whole menu.')
    print('Type 2 to add a dish to your menu.')
    print('Type 3 to change a price of a dish in your menu.')
    print('Type 4 to remove a dish from your menu.')
    print('Type 5 to exit.')
    user_choice = input('>>> ')
    if user_choice == '1':
        view_dishes_list()
    elif user_choice == '2':
        add_dishes()
    elif user_choice == '3':
        edit_dishes_price()
    elif user_choice == '4':
        remove_dishes()
    elif user_choice == '5':
        print('Process finished with exit code 0')
        break
    elif user_choice == '':
        print('You have typed nothing :(')
    else:
        print('You have typed incorrect answer. Try again :)')
