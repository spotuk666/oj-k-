books = {
    'Кінг': 'Воно',
    'Лондон': 'Біле ікло ',
    'Керролл': 'Аліса в країні чудес ',
    'Ліндгрен': 'Карлсон, який живе на даху '}

# Додай два найменування
books['Дефо'] = 'Пригоди Робінзона Крузо'
books['Дюма'] = ' Граф Монте-Крісто'
del books['Кінг']
# Видали одне найменування

if 'Дефо' in books and 'Дюма' in books:
     print ('База оновлена!')
if ('Кінг' in books) == False:
     print ('Переваги оновлені')








