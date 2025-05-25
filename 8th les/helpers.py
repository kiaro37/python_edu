def calc_discount(price, percent):
    if price<0 or percent<0:
        raise ValueError("Цена или процент скидки не могут быть отрицательными")
    else:
        return price-price*percent/100