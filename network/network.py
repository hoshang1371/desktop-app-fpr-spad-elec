import requests
import os
import sys

from extention.massegeBox import addProductSuccesMessege

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from extention.base64 import image_to_data_url

uriImportant = "http://192.168.1.52:8000";
Tok = {}

# statusOfLogin=""
class Network:
    url_email_login = f"{uriImportant}/api/api_token_auth/";
    url_add_product = f"{uriImportant}/api/addProduct/";

    myToken = "Token 0703e9e4e6a24cfce15b26a7fa0544de3c8101ea"   
    head = {'Authorization': f"{myToken}" }


    def post_login(email,password):
        print(email)
        print(password)
        r = requests.post(Network.url_email_login, json={
        "email": email,
        "password": password
        # "email": "hoshang.1371@yahoo.com",
        # "password": "Ho741jj555at963"
        })
        # print(f"Status Code: {r.status_code}, Response: {r.json()}")
        # statusOfLogin =r.status_code
        # print(statusOfLogin)
        # print(r.text)
        if r.status_code == 200:
            Tok = r.json()
            print("ok")
            print(Tok['token'])
        return(r.status_code)


    def post_product_data(title,code,place,number,
                          brand,description,smallDescription,price,
                          priceOff,picDir,active,vige):
    # def post_product_data(self):
        # print(title)
        # print(code)
        # print(place)
        # print(description)
        # print(brand)
        # o = int(price)
        # print(o)
        # print(picDir)
        picName = picDir.split('.')[-2]
        picName = picName.split('/')[-1]
        print('+++++++++++++++++++++++++++++++++')
        print(picName)
        img = image_to_data_url(picDir)
        # print(dir)
        print('+++++++++++++++++++++++++++++++++')
        if priceOff == "":
           r = requests.post(
                Network.url_add_product, 
                headers =Network.head,
                json={
                    "title": title,
                    "code": code,
                    "place": place,
                    "number": number,
                    "brand":brand,
                    "description": description,
                    "smallDescription":  smallDescription,
                    "price": int(price),
                    "active": active,
                    "vige": vige,
                    "image":{
                        "filename": "picName",
                        "contents": img
                }        
            }
            ) 
        else:
            r = requests.post(
                Network.url_add_product, 
                headers =Network.head,
                json={
                    "title": title,
                    "code": code,
                    "place": place,
                    "number": number,
                    "brand":brand,
                    "description": description,
                    "smallDescription":  smallDescription,
                    "price": int(price),
                    "priceOff": int(priceOff),
                    "active": active,
                    "vige": vige,
                    "image":{
                        "filename": "picName",
                        "contents": img
                }        
            }
            )

        print(r.status_code) 
        
        
        # print(r.headers) 
        # print(r.content) 
        print(r.text) 
        print(r.reason) 
        if r.status_code == 200:
            addProductSuccesMessege()



	
# if __name__ == '__main__': 
#    window()
