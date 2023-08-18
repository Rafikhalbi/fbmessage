import requests
from bs4 import BeautifulSoup

class Check(requests.Session):
    def __init__(self, cookie) -> None:
        super().__init__()
        self.cookie = cookie
        self.endpoint = 'https://mbasic.facebook.com'
        self.language = 'https://mbasic.facebook.com/language.php'

    def change_language(self):
        html = BeautifulSoup(
            self.get(self.language, headers={'cookie': self.cookie}).text, 'html.parser'
        )
        for lang_en in html.find_all('form', attrs={'method': 'post'}):
            if 'English (US)' in str(lang_en):
                action = self.endpoint + lang_en['action']
                data = {
                    'fb_dtsg': lang_en.find('input', attrs={'name': 'fb_dtsg'})['value'],
                    'jazoest': lang_en.find('input', attrs={'name': 'jazoest'})['value']
                }
        return self.post(action, data=data, headers={'cookie': self.cookie})

    def check_login(self):
        html = BeautifulSoup(
            self.get(self.endpoint, headers={'cookie': self.cookie}).text, 'html.parser'
        )
        if 'mbasic_logout_button' in str(html):
            self.change_language()
            print('ok, cookie valid')
            return True
        else:
            raise Exception(
                'cookie invalid!'
            )
    
