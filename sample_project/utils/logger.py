import datetime
import os


class Logger:
    file_name = f"logs/log_{datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as log_file:
            log_file.write(data)

    @classmethod
    def add_request(cls, url, method):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = "\n-----------\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Date: {datetime.datetime.now()}\n"
        data_to_add += f"Request: {method} {url}\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, result):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_to_add = f"\nResponse code: {result.status_code}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response Cookies: {cookies_as_dict}\n"
        data_to_add += f"Response body: {result.text}"
        data_to_add += "\n-----------\n"

        cls.write_log_to_file(data_to_add)