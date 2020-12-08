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
def update_title(products):
   for item in products:
    if 'part_number' in item.keys():
       item['title'] = item['brand'] + " " +item['title'] + " " + item['part_number']
    else:
        item['title'] = item['brand'] + " " + item['title']
   item['bw_uid'] = item["article_id"]

def extract_promotion(products):
    for item in products:
        if "+Microsoft Office" in item['title']:
            item['bw_promotion'] = "bundle"
        elif "Cashback" in item['title']:
           item['bw_promotion'] = "cashback"
        elif item['old_price'] != "":
            item['bw_promotion'] = "price"
        else:
            item['bw_promotion'] = "false"
    pass

def add_scheme_to_url(products):
    for item in products:
        if 'images' in item.keys():
            for idp, url in enumerate(item['images']):
                if item['images'][idp][0] ==item['images'][idp][1] == "/":
                    item['images'][idp] = "https:" + item['images'][idp]
                elif item['images'][idp] == "/" and item['images'][idp][0] != item['images'][idp][1]:
                   item['images'][idp] = "https:/" + item['images'][idp]
                elif "https://" in url:
                    item['images'][idp]=item['images'][idp]
                else:
                   item['images'][idp] = "https://" + item['images'][idp]      


def update_bw_uid(products):
     for item in products:
        if item['article_id'] != "":
            item['bw_id'] =item['article_id']

def browswave_products(products):
    for item in products:
        print(item)
    
update_title(products)
extract_promotion(products)
add_scheme_to_url(products)
update_bw_uid(products)
browswave_products(products)
