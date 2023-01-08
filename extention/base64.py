import base64

def image_to_data_url(filename):
    ext = filename.split('.')[-1]
    # prefix = f'data:image/{ext};base64,'
    prefix = f'data:@file/{ext};base64,'
    with open(filename, 'rb') as f:
        img = f.read()
    # print(prefix)
    # print("********************")
    # print(base64.b64encode(img).decode('utf-8'))
    return prefix + base64.b64encode(img).decode('utf-8')