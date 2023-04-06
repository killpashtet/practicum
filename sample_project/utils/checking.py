import json


class Checking:
    @staticmethod
    def check_status_code(response, status_code):
        assert status_code == response.status_code, f"Status code {response.status_code} received, {status_code} " \
                                                    f"is expected."

    @staticmethod
    def check_json_parameters(response, expected_value):
        parameters = json.loads(response.text)
        assert list(parameters) == expected_value

    @staticmethod
    def check_json_value(response, field_name, expected_result):
        check = response.json()
        check_info = check.get(field_name)
        assert expected_result == check_info, f"Значение поля {field_name} равно {check_info}, должно быть " \
                                              f"{expected_result}"

    @staticmethod
    def check_json_search_word_in_value(response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        assert search_word in check_info, f"Значение поля {field_name} не содержит {search_word}"
