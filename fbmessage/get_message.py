import requests
from bs4 import BeautifulSoup
import re

class Runner(requests.Session):
    def __init__(self, cookie) -> None:
        super().__init__()
        self.cookie = cookie
        self.headers.update({'cookie': self.cookie})
        self.endpoint = 'https://mbasic.facebook.com/messages/'

    def message(self, result={'event': []}, existing_data = None):
        result.clear()
        
        if existing_data is None:
            result = {'event': []}
        else:
            result = existing_data

        html = BeautifulSoup(
            self.get(self.endpoint).text, 'html.parser'
        )
        
        table = html.find_all('table')
        data = re.findall(
            r'<a href="(.*?)">.*?<span class=".*?">(.*?)</span>.*?<abbr>(.*?)</abbr>', str(table)
        )

        for get_message in data:
            url, message, time = get_message[0], get_message[1], get_message[2]
            message = BeautifulSoup(message, 'html.parser').get_text()
            result['event'].append({'message': message, 'url': url, 'time': time})
        return result
