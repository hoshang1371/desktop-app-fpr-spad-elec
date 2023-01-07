import requests

uriImportant = "http://192.168.1.51:8000";
Tok = {}
class Network:

    url_email_login = f"{uriImportant}/api/api_token_auth/";
    print(url_email_login)
    

    # def post_login():
    #     print(Network.url_email_login)

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
        if r.status_code == 200:
            Tok = r.json()
            # print("ok")
            # print(Tok['token'])
