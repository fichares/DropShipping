menu = [{'title': "Men", 'url_name': 'men'},
            {'title': "Women", 'url_name': 'women'},
            {'title': "Kids", 'url_name': 'kids'}
            ]

t = menu[0]



for e in menu:
    print(e)
    w = 0
    for  url_name, name in e.items():
        if w == 0:
         print(name)
        w = 1