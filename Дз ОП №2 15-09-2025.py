shopping_list = [4, 6, 11, 27, 15, 3, 50, 37, 16, 29,
                 "хліб", "молоко", "яйця", "сир", "цукерки",
                 "шоколадка", "помідори", "огірки", "цибуля", "ковбаса"] # список з 10 int та 10 str
ints = sorted([x for x in shopping_list if isinstance(x, int)]) # сортування int
strs = sorted([x for x in shopping_list if isinstance(x, str)]) # сортування str
sorted_shop_list = ints + strs # поєднання ints та strs
even_numbers = [x for x in ints if x % 2 == 0] # збираємо парні числа в новий список
caps_strs = [x.upper() for x in strs] # переводимо всі елементи str у верхній регістр
print("Відсортований список:", sorted_shop_list, "\nСписок праних чисел:", even_numbers, "\nСписок слів капсом:", caps_strs) # виводимо результат
