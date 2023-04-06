from utils.api import Google_maps_api
from utils.checking import Checking

"""Создание, изменение и удаление новой локации"""


class Test_create_place():
    def test_create_new_place(self):
        print("\nPOST method:")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_value(result_post, 'status', 'OK')

        print("GET method:")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print("PUT method:")
        result_put = Google_maps_api.put_new_place(place_id)

        print("GET method:")
        result_get = Google_maps_api.get_new_place(place_id)

        print("DELETE method:")
        result_delete = Google_maps_api.delete_place(place_id)

        print("GET method should return 404...")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
