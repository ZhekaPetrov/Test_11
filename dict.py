# Словари в Python
books = {          
    'Мертвые души' : 'Н. В. Гоголь', 
    '1984' : 'Джордж Оруэл'
}                    #В словаре находятся "Ключ - значение"

print(books)
print()

books = {
    'Мертвые души',
    '1984'
}                    #Если мы не указываем значение, автоматически создается множество, где будут только ключи
print(books)
print()

#Операции по словарям
dict = {       #dictionary - словарь
    'Мертвые души' : 'Н. В. Гоголь', 
    '1984' : 'Джордж Оруэл'
}
a = dict['Мертвые души']
print(a)              #С помощью ключа извлекаем из словаря его значение
print()

#Чтобы в словарь добавить новый элемент мы указываем в квадратных скобках ключ и через = добавляем значение
dict['Скотный двор'] = 'Джордж Оруэл'
print(dict)
print()

#Чтобы удалить элемент из словаря, используем del
del dict['1984']
print(dict)
print()

#Чтобы изменить значение в словаре в квадратных скобках пишем уже существующий ключ, и через = новое значение
dict['Скотный двор'] = 'Дж. Оруэл'
print(dict)
print()

#!!!ЕСЛИ УКАЗАТЬ НЕПРАВИЛЬНЫЙ КЛЮЧ, ТО ВМЕСТО ОБРАЩЕНИЯ К УЖЕ СУЩЕСТВУЮЩЕЙ ПАРЕ МЫ СОЗДАДИМ НОВУЮ!!!

