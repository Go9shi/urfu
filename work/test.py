from datetime import datetime, date

lst  = [{'amount' : '10',
        'date_expiration' : 'Здесь будет дата',
}]
goods = {'Яйца' : lst
}
title = {'Яйца' : '4',
}
def add(eats):
    lst = []

    eat = input('Добавьте продукт в холодильник: ')
    for item in title:
        if eat == item:
            goods[item].append({'amount' : int(input('Введите количество: ')),
                               'expiration_date' : datetime.strptime(input('Введите дату изготовления (мм.дд.гггг): '), "%m.%d.%Y").date(),
            })
            return goods
        else:
            amount = int(input('Введите количество/объем: '))
            date_str = input('Введите дату изготовления (мм.дд.гггг): ')
            date = datetime.strptime(date_str, "%m.%d.%Y").date()
            goods_dict = {'amount' : amount,
                  'date_expiration' : date,
    }
    lst.append(goods_dict)
    goods[eat] = lst
    return goods

print(add(goods))
