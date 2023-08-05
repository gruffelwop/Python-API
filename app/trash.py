
my_posts = [
    {
        "title": "Title 0",
        "content": "Content 0",
        "id": 0,
    },
    {
        "title": "Title 1",
        "content": "Content 1",
        "id": 1,
    },
    {
        "title": "Title 2",
        "content": "Content 2",
        "id": 2,
    },
]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post
        
def find_post_index(id):
    for i, post in enumerate(my_posts):
        if post["id"] == id:
            return i
