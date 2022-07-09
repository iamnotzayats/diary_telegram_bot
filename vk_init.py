import requests
import os

vk_token = os.getenv('vk_token')

def get_wall_posts():
    wallpost_request = f"https://api.vk.com/method/wall.get?domain=computer.center&access_token={vk_token}&count=2&v=5.131"

    result = requests.get(wallpost_request)
    data = result.json()

    #print(data)
    for item in data['response']['items']:
        text_item = item['text']
        print(text_item)
        if "attachments" in item:
            item = item["attachments"]

            if item[0]['type'] == "doc":
                if len(item) == 1:
                    post_doc = item[0]["doc"]["url"]
                    print(post_doc)
                    list_data = [text_item,post_doc]
                    return list_data





if __name__ == '__main__':
    get_wall_posts()