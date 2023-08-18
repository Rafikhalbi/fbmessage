import requests
from bs4 import BeautifulSoup
import re

class Send_message(requests.Session):
    def __init__(self, cookie, text = None, url = None, sticker_id = None) -> None:
        super().__init__()
        self.cookie = cookie
        self.text = text
        self.url = 'https://mbasic.facebook.com'+url
        self.headers.update({'cookie': self.cookie})
        self.sticker = sticker_id

    def get_html(self):
        return BeautifulSoup(
            self.get(self.url).text, 'html.parser'
        )

    def send_text(self):
        html = self.get_html()
        try:
            ids = html.find('input', attrs={'name': re.compile(r'ids\[\d+\]')})['value']
        except:
            ids = None
        action = html.find('form', attrs={'method': 'post', 'id': 'composer_form'})['action']
        data = {
            'fb_dtsg': html.find('input', attrs={'name': 'fb_dtsg'})['value'],
            'jazoest': html.find('input', attrs={'name': 'jazoest'})['value'],
            'body': self.text,
            'send': 'Send',
            'tids': html.find('input', attrs={'name': 'tids'})['value'],
            'wwwupp': 'C3',
            f'ids[{ids}]': ids,
            'platform_xmd': '',
            'referrer': '',
            'ctype': '',
            'cver': 'legacy',
            'csid': html.find('input', attrs={'name': 'csid'})['value']
            }
        return self.post(f'https://mbasic.facebook.com{action}', data=data)

    def send_sticker(self):
        html = self.get_html()
        sticker_url = html.find('a', string='Send Stickers')['href']
        get_sticker_html = BeautifulSoup(
            self.get(f'https://mbasic.facebook.com{sticker_url}').text, 'html.parser'
        )
        url_post = get_sticker_html.find('form', attrs={'method': 'post'})['action']
        data = {
            'fb_dtsg': get_sticker_html.find('input', attrs={'name': 'fb_dtsg'})['value'],
            'jazoest': get_sticker_html.find('input', attrs={'name': 'jazoest'})['value'],
            'body': '',
            'tids': get_sticker_html.find('input', attrs={'name': 'tids'})['value'],
            'sticker_id': self.sticker
        }
        return self.post(f'https://mbasic.facebook.com{url_post}', data=data)
