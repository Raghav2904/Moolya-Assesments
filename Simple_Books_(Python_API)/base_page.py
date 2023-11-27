import requests
import random

class Simple_books:

    def authorization(self):
        global base_url
        global access_token

        base_url = 'https://simple-books-api.glitch.me'
        endpoint_auth = '/api-clients/'
        num = str(random.randint(0, 100))

        payload_auth = {
            "clientName": "Postman",
            "clientEmail": "Raghav"+num+"@example.com"
        }

        response_aut = requests.post(base_url+endpoint_auth, json=payload_auth)
        print(response_aut.status_code)

        access_token = (response_aut.json())
        print(access_token['accessToken'])

    def create_order(self):
        global res
        global headers_order

        endpoint_order = '/orders'
        headers_order = {'Authorization': 'Bearer ' + access_token['accessToken']}

        payload_auth = {
            "bookId": 1,
            "customerName": "Raghav"
        }

        response_order = requests.post(base_url+endpoint_order, json=payload_auth, headers=headers_order)
        print(response_order.status_code)
        print(response_order.json())

        res = response_order.json()

    def get_order(self):

        global endpoint
        endpoint = '/orders/'+res['orderId']

        response_get_order = requests.get(base_url+endpoint, headers=headers_order)
        print(response_get_order.status_code)
        print(response_get_order.json())

        response_get_order = requests.get(base_url+endpoint, headers=headers_order)
        print(response_get_order.status_code)
        print(response_get_order.json())

    def update_order(self):

        payload_update = {
            "customerName": "Raghav123"
        }

        response_updated_order = requests.patch(base_url+endpoint, json=payload_update, headers=headers_order)
        print(response_updated_order.status_code)

    def get_updated(self):

        response_updated_order = requests.get(base_url+endpoint, headers=headers_order)
        print(response_updated_order.status_code)
        print(response_updated_order.json())

    def delete(self):
        response_delete_order = requests.delete(base_url+endpoint, headers=headers_order)
        print(response_delete_order.status_code)
