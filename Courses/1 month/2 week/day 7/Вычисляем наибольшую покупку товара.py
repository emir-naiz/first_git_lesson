# Вычисляем наибольшую покупку, товара
# Ogogo shop
list1 = ['Asus','Acer','HP','Lenovo','Sony','Dell','Macbook']
list2 = [20,10,11,9,20,21,3]
max_of_list2 = max(list2) # Ищем наибольшее кол-во покупок
index_list2 = list2.index(max_of_list2) # Находим позицию элемента max_of_list2
print(f"Ноутбук: {list1[index_list2]} Покупали: {max_of_list2} раз!")
