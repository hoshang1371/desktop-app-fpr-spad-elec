import requests
import os
import sys

from extention.massegeBox import addProductSuccesMessege

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from extention.base64 import image_to_data_url
from extention.storeData import storeData ,loadData
from cryptography.fernet import Fernet

# from product.importerProduct import keyToken
keyToken = b'chz4UshV2y2R3oCf_nWpX_PsqArGPy0WRrqE72krxbI='

uriImportant = "http://192.168.1.52:8000";

Tok = {}
head = {}
class Network:
    url_email_login = f"{uriImportant}/api/api_token_auth/";
    url_add_product = f"{uriImportant}/api/addProduct/";
    url_list_product = f"{uriImportant}/api/";

    # global head  
    # myToken = "Token 0703e9e4e6a24cfce15b26a7fa0544de3c8101ea" 
    # head = {}
    # def __init__(self):
    #     self.myToken = "Token 0703e9e4e6a24cfce15b26a7fa0544de3c8101ea" 
    #     self.head ={}
    #     self.head = {'Authorization': f"{self.myToken}" }
    def post_login(email,password):
        # global j
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
            # global head
            head = {'Authorization': f"Token {Tok['token']}" }
            # self.head = {'Authorization': f"Token {Tok['token']}" }
            print("Network.head")
            print(head)
            print(Tok['token'])
            
            # tokenEnc = Fernet(keyToken).encrypt(Tok['token'].encode('utf-8'))
            # storeData(tokenEnc,keyToken)
            Network.saveLocalStorageToken(Tok['token'])

        return(r.status_code)

    def saveLocalStorageToken(TokenSave):
            tokenEnc = Fernet(keyToken).encrypt(TokenSave.encode('utf-8'))
            storeData(tokenEnc,keyToken)


    def LoadLocalStoregToken():
        db = loadData()
        print(db)
        token = Fernet(db['key']).decrypt(db['token'])
        print(token)
        head = {'Authorization': f"Token {token.decode('utf-8')}" }
        return head

    def post_product_data(title,code,place,number,
                          brand,description,smallDescription,price,
                          priceOff,picDir,active,vige):
        picName = picDir.split('.')[-2]
        picName = picName.split('/')[-1]
        print('+++++++++++++++++++++++++++++++++')
        # db = loadData()
        # print(db)
        # token = Fernet(db['key']).decrypt(db['token'])
        # print(token)
        # head = {'Authorization': f"Token {token.decode('utf-8')}" }
        head = Network.LoadLocalStoregToken()

        print('+++++++++++++++++++++++++++++++++')

        img = image_to_data_url(picDir)

        if priceOff == "":
           r = requests.post(
                Network.url_add_product, 
                headers =head,
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
                headers =head,
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

    def getProductList():

        head = Network.LoadLocalStoregToken()
        
        r = requests.get(
            Network.url_list_product,
            headers =head,
            )
        if r.status_code == 200:
            return r.text
        else:
            return "Error"

	
# if __name__ == '__main__': 
#    window()
