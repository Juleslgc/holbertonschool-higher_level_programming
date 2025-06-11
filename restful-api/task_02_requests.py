#!/usr/bin/python3
"""
It contains the functions:
fetch_and_print_posts
fetch_and_save_posts
"""
import requests
import csv


url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Function that fetches all post from JSONPlaceholder.
    """
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Error during query: {}".format(e))
        return

    print("Status Code: {}".format(response.status_code))
    for post in response.json():
        print(post['title'])


def fetch_and_save_posts():
    """
    Function that fetches all post from JSONPlaceholder.
    """
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Error during query: {}".format(e))
        return

    print("Status Code: {}".format(response.status_code))
    data = response.json()
    filtered_posts = []
    for post in data:
        new_post = {
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
        }
        filtered_posts.append(new_post)
    with open("posts.csv", 'w') as file:
        write = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
        write.writeheader()
        write.writerows(filtered_posts)
