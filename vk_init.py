import requests

def get_wall_posts():
    wallpost_request = "https://api.vk.com/method/wall.get?domain=computer.center&v=5.131"
    result = requests.get(wallpost_request)
    print(result)

if __name__ == '__main__':
    get_wall_posts()