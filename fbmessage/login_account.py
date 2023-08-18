import requests
from bs4 import BeautifulSoup

class Generete_cookie(requests.Session):

    def __init__(self, username: str, password: str) -> None:
        super().__init__()
        self.username = username
        self.password = password
        self.endpoint = 'https://mbasic.facebook.com'

    def generete_data(self) -> dict:
        html = BeautifulSoup(
            self.get(self.endpoint, headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Accept-Language": "en-US,en;q=0.9", "Dpr": "1", "Sec-Ch-Prefers-Color-Scheme": "light", "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"", "Sec-Ch-Ua-Full-Version-List": "\"Not/A)Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"115.0.5790.170\", \"Chromium\";v=\"115.0.5790.170\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Model": "\"\"", "Sec-Ch-Ua-Platform": "\"macOS\"", "Sec-Ch-Ua-Platform-Version": "\"10.13.0\"", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}).text, "html.parser"
        )
        data = {"lsd": html.find("input", attrs={"name": "lsd"})["value"], "jazoest": html.find("input", attrs={"name": "jazoest"})["value"], "m_ts": html.find("input", attrs={"name": "m_ts"})["value"], "li": html.find("input", attrs={"name": "li"})["value"], "try_number": "0", "unrecognized_tries": "0", "email": self.username, "pass": self.password, "login": "Log In", "bi_xrwh": "0"}
        return data
    
    def login(self):
        data = self.generete_data()
        response = self.post(
            self.endpoint + '/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8', headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Cache-Control": "max-age=0", "Content-Length": "152", "Content-Type": "application/x-www-form-urlencoded", "Dpr": "1", "Origin": "https://mbasic.facebook.com", "Referer": "https://mbasic.facebook.com/", "Sec-Ch-Prefers-Color-Scheme": "light", "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"", "Sec-Ch-Ua-Full-Version-List": "\"Not/A)Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"115.0.5790.170\", \"Chromium\";v=\"115.0.5790.170\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Model": "\"\"", "Sec-Ch-Ua-Platform": "\"macOS\"", "Sec-Ch-Ua-Platform-Version": "\"10.13.0\"", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36", "Viewport-Width": "701"}, data=data
        )
        if 'c_user' in str(self.cookies.get_dict()):
            cookie = ';'.join([f'{key}={value}' for key, value in self.cookies.get_dict().items()])
            print('Login: succes!')
            return cookie
        if 'checkpoint' in str(self.cookies.get_dict()):
            raise Exception(
                'account checkpoint!'
            )
        else:
            raise Exception(
                'username/password wrong!'
            )
