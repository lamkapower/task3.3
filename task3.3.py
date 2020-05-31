import requests
from urllib.parse import urlencode
from pprint import pprint

TOKEN = 'a5f2c7d3c6d52abf3540da30d5722180a695b7277a70d011b24aa7f5e41ed8ae699edfad4c21f946f88ec'


class Users:

    def __init__(self, user_id):
        self.user_id = user_id

    

    def get_params(self):
        return {
            'access_token': 'a5f2c7d3c6d52abf3540da30d5722180a695b7277a70d011b24aa7f5e41ed8ae699edfad4c21f946f88ec',
            'user_id': self.user_id,
            'v': '5.89'
        }

    def friends_list(self):
        params = self.get_params()
        response = requests.get('https://api.vk.com/method/friends.get', params=params)
        return response.json()['response']['items']

    def __and__(self, other_id):
        User1_set = set(self.friends_list())
        params = self.get_params()
        params['user_id'] = other_id.get_params()['user_id']
        response = requests.get('https://api.vk.com/method/friends.get', params=params)
        User2_set = set(response.json()['response']['items'])
        intersection_set = User1_set.intersection(User2_set)
        return intersection_set

    def __str__(self):
        return f'https://vk.com/id{self.user_id}'

if __name__ == "__main__":
    User1 = Users('28577')
    User2 = Users('11264606')
    User3 = Users('6274')
    cross_friends = (User1 & User3)
    print(cross_friends)
    print(User2)
