import json, re

posts = []
POST_PATH = 'posts.json'


def load_posts_from_json():
    global posts
    with open(POST_PATH, encoding='UTF-8') as fp:
        posts = json.load(fp)
        return posts


def upload_posts(posts):
    with open(POST_PATH, 'w', encoding='UTF-8') as file:
        json.dump(posts, file, indent=4)



