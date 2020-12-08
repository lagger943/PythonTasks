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
        "article_id": "",
        "bw_uid": "",
        "ean": "08898425669540",
        "price": 1200,
        "bw_promotion": "false",
        "old_price": "",
        "entry_page_product": "laptop"
    },
    {
        "title": "Blade 15 Gaming Laptop - Intel Core i7-8750H 6 Core + Microsoft Office 365 Home with Auto-Renew",
        "brand": "Razer",
        "article_id": "B08149JV6B",
        "bw_uid": "",
        "price": 1300,
        "bw_promotion": "false",
        "old_price": "1600",
        "entry_page_product": "laptop"
    }
]
for item in products:
    if 'part_number' in item.keys():
        item['title'] = item['brand'] + " " + item['title'] + " " + item['part_number']
    else:
        item['title'] =item['brand'] + " " + item['title']
    item['bw_uid'] = item["article_id"]
    
    if "+ Microsoft Office" in item['title']: 
        item['bw_promotion'] = "bundle"
    elif item['old_price'] != "":
        item['bw_promotion'] = "price"
    else:
         item['bw_protmiton'] = "false"
for item in products:
    if item['bw_uid'] != "":
        if item['bw_promotion'] == "bundle" or item['bw_promotion'] == "price":
            price_diff = float(item['old_price']) - item['price'] 
            print(f"The {item['entry_page_product']}: {item['title']} has a promotion of type: {item['bw_promotion']} and costs {item['price']}$ which is {price_diff}$ less than before")
        else:
            print(f"The {item['entry_page_product']}: {item['title']} has no promotion of any type and costs {item['price']}$")
