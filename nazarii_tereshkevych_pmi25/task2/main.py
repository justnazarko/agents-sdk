from linked_list import LinkedList


def main():
    while True:
        my_list = LinkedList()
        my_list.insert_from_keyboard()
        print(my_list)
        try:
            if my_list.is_sorted():
                print("Добуток різниць сусідніх елементів: ", my_list.calc_neighbor_differ_product())
            else:
                print("Сума додатніх елементів: ", my_list.sum_of_positive())
        except ValueError as err:
            print(err)

        choice = input("Якщо ви хочете ввести новий список, натисніть 1, у іншому випадку натисніть будь-який символ\n").strip()
        if choice != "1":
            break


main()
