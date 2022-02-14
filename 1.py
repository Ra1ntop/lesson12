#
names = ['Саша', 'Максим', 'Леша']
print(names[0])
print(names[1])
print(names[2])

#
names = ['Саша', 'Максим', 'Леша']
message = f"Верни сотку {names[0].title()}"
print(message)
message = f"Верни сотку {names[1].title()}"
print(message)
message = f"Верни сотку {names[2].title()}"
print(message)


#
car = ['audi', 'bmw', 'lamba']
message = f"Я хотел бы купить машину {car[0].title()}"
print(message)
message = f"Я хотел бы купить машину {car[1].title()}"
print(message)
message = f"Я хотел бы купить машину {car[2].title()}"
print(message)


#
guest = ['брат', 'сестра', 'папа', 'мама']
message = f"{guest[0].title()} приходи сегодня"
print(message)
message = f"{guest[1].title()} приходи сегодня"
print(message)
message = f"{guest[2].title()} приходи сегодня"
print(message)
message = f"{guest[3].title()} приходи сегодня"
print(message)

#
guest = ['брат', 'сестра', 'папа', 'мама']
print(guest[3], "прийти не сможет")
guest[3]="дедушка"
message = f"{guest[0].title()} приходи сегодня вечером на обед"
print(message)
message = f"{guest[1].title()} приходи сегодня вечером на обед"
print(message)
message = f"{guest[2].title()} приходи сегодня вечером на обед"
print(message)
message = f"{guest[3].title()} приходи сегодня вечером на обед"
print(message)

#
guest = ['брат', 'сестра', 'папа', 'мама']
print ("Стол стал больше")
guest.insert(0, "тетя")
guest.insert(3, "дядя")
guest.insert(6, "бабушка")
message = f"{guest[0].title()} приходи сегодня"
print(message)
message = f"{guest[1].title()} приходи сегодня"
print(message)
message = f"{guest[2].title()} приходи сегодня"
print(message)
message = f"{guest[3].title()} приходи сегодня"
print(message)
message = f"{guest[4].title()} приходи сегодня"
print(message)
message = f"{guest[5].title()} приходи сегодня"
print(message)
message = f"{guest[6].title()} приходи сегодня"
print(message)

#
guest = ['брат', 'сестра', 'папа', 'мама']
print ("Стол стал больше")
guest.insert(0, "тетя")
guest.insert(3, "дядя")
guest.insert(6, "бабушка")
message = f"{guest[0].title()} приходи сегодня"
print(message)
message = f"{guest[1].title()} приходи сегодня"
print(message)
message = f"{guest[2].title()} приходи сегодня"
print(message)
message = f"{guest[3].title()} приходи сегодня"
print(message)
message = f"{guest[4].title()} приходи сегодня"
print(message)
message = f"{guest[5].title()} приходи сегодня"
print(message)
message = f"{guest[6].title()} приходи сегодня"
print(message)
print('простите не выйдет прийдут только двое')
dlina=len(guest)
while dlina>3:
    dlina=len(guest)
    del_guest=guest.pop(0)
    message = f"{del_guest} извини в этот раз не получится"
    print(message)
message = f"{guest[0].title()} для вас еще в силе"
print(message)
message = f"{guest[1].title()} для вас еще в силе"
print(message)
