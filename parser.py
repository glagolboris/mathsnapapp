import re
import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, photo_in_base64):
        self.url_for_OCR = 'https://www.mathway.com/OCR'
        self.base64_image = photo_in_base64

    def run_solve(self, equation):
        from reshatel import resh
        return resh(equation)

    def get_equation(self) -> str:
        data = {
            'imageData': f'data:image/png;base64,{self.base64_image.decode("utf-8")}',
            'culture': 'ru'
        }
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'accept-encoding': 'gzip, deflate, br',
            'referer': 'https://www.mathway.com/ru/Algebra',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
            'x-requested-with': 'XMLHttpRequest'
        }

        response = requests.post(url=self.url_for_OCR, headers=headers, data=data)
        response_json = response.json()
        if response_json['AsciiMath'].count(',') == 1:
            return response_json['AsciiMath'].replace('{', '').replace('}', '').replace(':', '').replace('[',
                                                                                                         '').replace(
                ']', '')
        else:
            return response_json['AsciiMath'].replace('{', '').replace('}', '').replace(':', '')
