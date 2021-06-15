price = 40 #DOLLARS
shipping_cost = 5.5 #EUROS

price_bgn = price*1.67 #Converting to bgn
shipping_bgn = shipping_cost*1.96 #Converting to bgn
total_price=price_bgn+shipping_bgn #Total sum with shipping
print(f" Price without shippping {price_bgn} Leva\n Price with shipping {total_price} Leva")

