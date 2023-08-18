# install module
```
pip install git+https://github.com/Rafikhalbi/fbmessage
```

# example how to use

```PYTHON

import fbmessage
import random

# account facebook
username = 'username/email'
password = 'password'

# generete facebook cookie
login = fbmessage.Generete_cookie(username, password).login()

# or
login = 'datrxxxxxxxxxxxxxxxx' # youre facebook cookie

# check valid cookie, if valid return True
check = fbmessage.Check(login).check_login()

def send_message_text(login, text, url):
    send = fbmessage.Send_message(
        cookie=login, text=text, url=url
    )
    return send.send_text()

def send_message_sticker(login, url):
    sticker_list = [
        '529233727538989', # smile :)
        '529233744205654', # cry
        '529233764205652', # angry
        '529233777538984', # love
        '529233810872314', # funny
        '529233834205645', # shock
        '529233847538977', # sleep
    ]
    send = fbmessage.Send_message(
        cookie=login, url=url, sticker_id= random.choice(sticker_list)
    )
    return send.send_sticker()

while check:
    data = fbmessage.Runner(login).message()
    try:
        for event_data in data['event']:
            if event_data['message'] == 'hai':
                url, time = event_data['url'], event_data['time']
                send_message_text(login=login, text='juga', url=url)

            if event_data['message'] == 'sticker':
                url, time = event_data['url'], event_data['time']
                send_message_sticker(login=login, url=url)
            else:
                continue
    except:
        continue
```
