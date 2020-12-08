product = {
    "title": "IdeaPad L340 Gaming Laptop, 15.6-Inch FHD (1920 X 1080) IPS Display, Intel Core i7-9750H Processor + Microsoft Office 365 Home with Auto-Renew",
    "brand": "Lenovo",
    "part_number": "KJT-00004",
    "article_id": "B07MRFM1CJ",
    "bw_uid": "B07MRFM1CJ",
    "ean": "0889842369540",
    "price": 949,
    "bw_promotion": "false",
    "old_price": "1399.00",
    "entry_page_product": "laptop"
}
price_difference = None
if "Microsoft Office" in product['title']:
    product['bw_promotion'] = "bundle"
product['title'] = product['brand'] + " " + product['title'] + " " +product['part_number']
price_difference = float(product['old_price']) - product['price'] 
print(f"The {product['entry_page_product']} {product['title']} that has a promotion of type {product['bw_promotion']} used to cost {product['old_price']} but now is {price_difference} cheaper.")

