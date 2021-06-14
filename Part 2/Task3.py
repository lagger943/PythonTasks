products = [
    {
        "title": "IdeaPad L340 Gaming Laptop, 15.6-Inch FHD (1920 X 1080) IPS Display, Intel Core i7-9750H Processor + Microsoft Office 365 Home with Auto-Renew",
        "brand": "Lenovo",
        "part_number": "KJT-00004",
        "article_id": "B07MRFM1CJ",
        "bw_uid": "",
        "ean": "0889842369540",
        "price": 949,
        "bw_promotion": "false",
        "old_price": "1399.00",
        "entry_page_product": "laptop"
    },
    {
        "title": "Inspiron 13 5000 2-in-1 - 13.3\" FHD Touch and Samsung 860 Evo 500GB 2.5 inch SATA III Internal SSD",
        "brand": "Dell",
        "part_number": "KJT-00016",
        "article_id": "B08170JV6B",
        "bw_uid": "",
        "ean": "08898425669540",
        "price": 1200,
        "bw_promotion": "false",
        "old_price": "",
        "entry_page_product": "laptop",
        "images": [
            "//images-na.ssl-images-amazon.com/images/I/51nUJKG2VGL._SL1000_.jpg",
            "https://images-na.ssl-images-amazon.com/images/I/61A1tGq5q3L._SL1000_.jpg",
            "/images-na.ssl-images-amazon.com/images/I/51RXnBkn6hL._SL1000_.jpg",
            "https://images-na.ssl-images-amazon.com/images/I/61Y6Q2qCHOL._SL1500_.jpg",
            "images-na.ssl-images-amazon.com/images/I/61qKz%2BI7mhL._SL1500_.jpg"
        ],
    },
    {
        "title": "Blade 15 Gaming Laptop - Intel Core i7-8750H 6 Core + Microsoft Office 365 Home with Auto-Renew",
        "brand": "Razer",
        "article_id": "",
        "bw_uid": "",
        "price": 1300,
        "bw_promotion": "false",
        "old_price": "1600",
        "entry_page_product": "laptop"
    },
    {
        "title": "Blade 17 Gaming Laptop - Intel Core i7-8750H 6 Core 40$ Cashback",
        "brand": "Razer",
        "article_id": "B08170JO4B",
        "bw_uid": "",
        "price": 1300,
        "bw_promotion": "false",
        "old_price": "",
        "entry_page_product": "laptop"
    }
]
def update_title(product):
    if 'part_number' in product.keys():
            product['title'] = product['brand'] + " " + product['title'] + " " + product['part_number']
    else:
            product['title'] = product['brand'] + " " + product['title']
    product['bw_uid'] = product["article_id"]


def extract_promotion(product):
    if "+Microsoft Office" in product['title']:
        product['bw_promotion'] = "bundle"
    elif "Cashback" in product['title']:
        product['bw_promotion'] = "cashback"
    elif product['old_price'] != "":
        product['bw_promotion'] = "price"
    else:
        product['bw_promotion'] = "false"

def add_scheme_to_url(product):
    if 'images' in product.keys():
        for idp, url in enumerate(item['images']):
            if product['images'][idp][0] == product['images'][idp][1] == "/":
                    product['images'][idp] = "https:" + product['images'][idp]
            elif product['images'][idp] == "/" and product['images'][idp][0] != product['images'][idp][1]:
                    product['images'][idp] = "https:/" + product['images'][idp]
            elif "https://" in url:
                    product['images'][idp] = product['images'][idp]
            else:
                product['images'][idp] = "https://" + product['images'][idp]


def update_bw_uid(product):
    if product['article_id'] != "":
        product['bw_id'] = product['article_id']


def browswave_products(products):
    for item in products:
        print(item)

for item in products:
    update_title(item)
    extract_promotion(item)
    add_scheme_to_url(item)
    update_bw_uid(item)
browswave_products(products)
