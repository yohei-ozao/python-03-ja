import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com/posts"


def list_posts():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        posts = response.json()
        for post in posts:
            print(post)
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


def create_post(title, body, user_id):
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()
        print("Post created successfully.")
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


def update_post(post_id, title=None, body=None, user_id=None):
    data = {}
    if title:
        data["title"] = title
    if body:
        data["body"] = body
    if user_id:
        data["userId"] = user_id
    try:
        response = requests.put(f"{API_URL}/{post_id}", json=data)
        response.raise_for_status()
        print("Post updated successfully.")
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


def delete_post(post_id):
    try:
        response = requests.delete(f"{API_URL}/{post_id}")
        response.raise_for_status()
        print("Post deleted successfully.")
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


def main():
    while True:
        print("1: List posts\n2: Create post\n3: Update post\n4: Delete post\n5: Exit")
        option = input("Choose an option: ")

        if option == "1":
            list_posts()
        elif option == "2":
            title = input("Enter title: ")
            body = input("Enter body: ")
            user_id = input("Enter user ID: ")
            create_post(title, body, user_id)
        elif option == "3":
            post_id = input("Enter post ID: ")
            title = input("Enter new title: ")
            body = input("Enter new body: ")
            user_id = input("Enter new user ID: ")
            update_post(post_id, title, body, user_id)
        elif option == "4":
            post_id = input("Enter post ID: ")
            delete_post(post_id)
        elif option == "5":
            print("Exiting program.")
            sys.exit(0)
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()