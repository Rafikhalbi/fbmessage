import requests, re, json, random

class CreatePage(requests.Session):
    def __init__(self, cookie, name) -> None:
        self.name = name
        self.pageUrl = 'https://web.facebook.com/pages/creation?ref_type=launch_point'
        self.graph = 'https://web.facebook.com/api/graphql/'
        super().__init__()
        self.cookies.update({'cookie': cookie})

    def getDataPayload(self):
        self.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Dpr': '1',
            'Referer': 'https://web.facebook.com/',
            'Sec-Ch-Prefers-Color-Scheme': 'dark',
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'Sec-Ch-Ua-Full-Version-List': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.71", "Google Chrome";v="120.0.6099.71"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Model': '""',
            'Sec-Ch-Ua-Platform': '"Linux"',
            'Sec-Ch-Ua-Platform-Version': '"5.15.0"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Viewport-Width': '661'
        })
        html = self.get(self.pageUrl).text
        try:
            data = {
                'av': re.search('__user=(.*?)&', str(html)).group(1),
                '__user': re.search('__user=(.*?)&', str(html)).group(1),
                '__a': '1',
                '__req': '15',
                '__hs': re.search('"haste_session":"(.*?)",', str(html)).group(1),
                'dpr': '1',
                '__ccg': 'EXCELLENT',
                '__rev': re.search('{"rev":(.*?)}', str(html)).group(1),
                '__s': 'jckwe1:g4nova:2fctec',
                '__hsi': re.search('"hsi":"(.*?)",', str(html)).group(1),
                '__dyn': '7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwnUW3q2ibwNwnof8boG0IE6u3y4o2Gwfi0LVEtwMw65xO2OU7m221FwgolzUO0-E7m4oaEnxO0Bo7O2l2Utwwwi831wiE567Udo5qfK0zEkxe2GewyDwkUtxGm2SUbElxm1Wxfxmu3W3y261eBx_wHwdG7FoarCwLyESE6C14wkQ0z8c86-3u364UrwFg662S269wqQ1FwgU4q3G1eKufw',
                '__csr': 'gz6MH8RZWkiKyindsj8x4B8ya-B_8COiOnbEyczTfvBmZWSGqimBWlOEyQRKF3nFyqCWlGHWqpkqKihrGCGjyoBiaazbhWnK9DCUoiAyuaXGjRxaiazE94FF5BGfyodAui68W2h1q49AEbE9aw_xifxW6GwIx622h3U88lwjo4e9xq2u1wxmubxbwExS0B84m0_8bU563O484i1mwMwvU2hw0KHxG00w_o03lqPw3UFU5-0Ao0lHw1ie0cpy8O0he5E0caU0nSzU1RE0yPw1hm01d3w1xy',
                '__comet_req': '15',
                'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', str(html)).group(1),
                'jazoest': re.search('&jazoest=(.*?)",', str(html)).group(1),
                'lsd': re.search('"LSD",\[\],{"token":"(.*?)"', str(html)).group(1),
                '__aaid': '0',
                '__spin_r': re.search('"__spin_r":(.*?),', str(html)).group(1),
                '__spin_b': 'trunk',
                '__spin_t': re.search('"__spin_t":(.*?),', str(html)).group(1),
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
                'variables': '{"input":{"bio":"hello, welcome to my fanspage","categories":["1105"],"creation_source":"comet","name": "%s","page_referrer":"launch_point","actor_id":"%s","client_mutation_id":"1"}}'%(self.name, re.search('__user=(.*?)&', str(html)).group(1)),
                'server_timestamps': 'true',
                'doc_id': '5296879960418435'
            }
            return data
        except:
            raise Exception("data not found!")
        
    def create(self):
        data = self.getDataPayload()
        self.headers.update({
            'Accept': '*/*',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Length': '1404',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Dpr': '1',
            'Origin': 'https://web.facebook.com',
            'Referer': 'https://web.facebook.com/pages/creation?ref_type=launch_point',
            'Sec-Ch-Prefers-Color-Scheme': 'dark',
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'Sec-Ch-Ua-Full-Version-List': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.71", "Google Chrome";v="120.0.6099.71"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Model': '""',
            'Sec-Ch-Ua-Platform': '"Linux"',
            'Sec-Ch-Ua-Platform-Version': '"5.15.0"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Viewport-Width': '661',
            'X-Asbd-Id': '129477',
            'X-Fb-Friendly-Name': 'AdditionalProfilePlusCreationMutation',
            'X-Fb-Lsd': 'agV5-prqvb1NPxlKBuSemS',
        })

        response_data = json.loads(self.post(self.graph, data=data).text)
        error_message = response_data['data']['additional_profile_plus_create']['error_message']
        if error_message is None:
            additional_profile_id = response_data['data']['additional_profile_plus_create']['additional_profile']['id']
            print(f"Akun berhasil dibuat! ID Akun: {additional_profile_id}")
        else:
            print(f"Terjadi kesalahan: {error_message}")

def createName():
    number = random.randint(0, 10000)
    random_text = random.choice(['AB', 'AC', 'AD', 'AF', 'AG', 'AF', 'AH', 'AJ', 'CC', 'HY', 'GS'])
    return 'VOD %s %s'%(random_text, number)

if __name__ == '__main__':
    cookies = open('account.txt', 'r').read().splitlines()
    for cookie in cookies:
        name = createName()
        try:
            page = CreatePage(cookie=cookie, name=name)
            page.create()
        except:
            continue
    print('=============================\n  PROGRAM FINISH\n=============================')