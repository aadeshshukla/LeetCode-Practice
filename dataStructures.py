#discount system
fruits={'apple':25,'banana':12,'mango':40}
vegetables={'tomato':30,'potato':25,'onion':35}
dairy={'milk':30,'cheese':90,'butter':60}

#category discount
category_discount={
    'fruits':10, #10%
    'vegetables':5, #5%
    'dairy':15  #15%
}
#CATEGORIES
categories={
     'fruits':fruits,
    'vegetables':vegetables,
    'dairy':dairy
}
def get_discounted_price(product):
    for category_name,items in categories.items():
        if product in items:
            original_price=items[product]
            discount=category_discount[category_name]
            discounted_price=original_price-(original_price*discount/100)
            return discounted_price
    return "product not found"

print(get_discounted_price('potato'))