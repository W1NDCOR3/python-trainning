from pydantic import BaseModel
import requests


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

    def __str__(self) -> str:
        return f'Post(userId={self.userId}, id={self.id}, title={self.title}, body={self.body})'

def get_url(url: str) -> None:
    """
    Make a GET request to a URL and print the response content.

    Args:
        url (str): The URL to make the request to.
    """
    response = requests.get(url)
    print(response.text)

get_url('https://www.google.com')

def post_url(url: str, payload: dict) -> None:
    """
    Make a POST request to a URL with a payload and print the response content.

    Args:
        url (str): The URL to make the request to.
        payload (dict): The payload to send in the request.
    """
    response = requests.post(url, data=payload)
    print(response.text)

post_url('https://httpbin.org/post', {'key': 'value'})

def get_json(url: str) -> dict:
    """
    Make a GET request to a URL and return the response JSON content.

    Args:
        url (str): The URL to make the request to.

    Returns:
        dict: The JSON content of the response.
    """
    response = requests.get(url)
    return response.json()

print(get_json('https://jsonplaceholder.typicode.com/posts/1'))