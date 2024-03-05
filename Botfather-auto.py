from telethon import TelegramClient, events, sync
from time import sleep

api_id = 10953300
api_hash ='9c24426e5d6fa1d441913e3906627f87'

with TelegramClient('session_name', api_id, api_hash) as client:
        result = client.send_message('BotFather', '/newbot')
        sleep(1)
        result.click(0)
        result = client.send_message('BotFather', 'satomoru')
        sleep(1)
        result = client.send_message('BotFather', f'satomoroufgornak{i}bot')
        sleep(1)
        result = client.get_messages('BotFather', limit=1)[0]
        sleep(1)
