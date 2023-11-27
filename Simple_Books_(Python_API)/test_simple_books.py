import random
import requests

from base_page import Simple_books


class Test_cases:

    def test_authorization(self):
        obj = Simple_books()
        obj.authorization()

    def test_create_order(self):
        obj = Simple_books()
        obj.create_order()

    def test_get_order(self):
        obj = Simple_books()
        obj.get_order()

    def test_update_order(self):
        obj = Simple_books()
        obj.update_order()

    def test_get_updated(self):
        obj = Simple_books()
        obj.get_updated()

    def test_delete(self):
        obj = Simple_books()
        obj.delete()



###Get Order##
    # def get_order(self):
    #     global endpoint
    #     endpoint = '/orders/'+res['orderId']
    #
    #     response_get_order = requests.get(base_url+endpoint, headers=headers_order)
    #     print(response_get_order.status_code)
    #     print(response_get_order.json())

###Update Order###

    # def update_order(self):
    #
    #     payload_update = {
    #         "customerName": "Raghav123"
    #     }
    #
    #     response_updated_order = requests.patch(base_url+endpoint, json=payload_update, headers=headers_order)
    #     print(response_updated_order.status_code)

##Get Updated Order###
    # def get_updated(self):
    #
    #     response_updated_order = requests.get(base_url+endpoint, headers=headers_order)
    #     print(response_updated_order.status_code)
    #     print(response_updated_order.json())


###Delet Order###
    # def delete(self):
    #     response_delete_order = requests.delete(base_url+endpoint, headers=headers_order)
    #     print(response_delete_order.status_code)


# obj = Test_cases()
# obj.authorization()
# obj.create_order()
# obj.get_order()
# obj.update_order()
# obj.get_updated()
# obj.delete()