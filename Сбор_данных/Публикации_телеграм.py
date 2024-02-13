
from telethon.sync import TelegramClient
from asyncio import run
import pandas as pd

df = pd.DataFrame(columns = ['date', 'views', 'count_reaction','top_reaction', 'forward', 'media','scheduled', 'edit_date',  'edit_hide', 'text', 'comments'])

api_id = API_ID
api_hash = str(API_HASH)
phone = PHONE
name = AC_NAME
chat = CHAT
path = DATA_PATH
f_name = F_NAME
path = rf'{path}\{f_name}.csv'

com = []

async def messages_func(name, api_id, api_hash):
  async with TelegramClient(name, api_id, api_hash) as client:
    print("Extracting messages")
    messages = client.iter_messages(chat)
    async for message in messages:
      id_1 = message.id
      text = message.message
      views = message.views
      date = message.date
      from_scheduled = message.from_scheduled
      edit_date = message.edit_date
      edit_hide = message.edit_hide
      reac = message.reactions
      med = message.media
      com = []

      forward = message.forwards
      df.at[id_1, 'text'] = text
      df.at[id_1, 'forward'] = forward
      df.at[id_1, 'views'] = views
      df.at[id_1, 'date'] = date
      df.at[id_1, 'media'] = med
      df.at[id_1, 'top_reaction'] = reac
      df.at[id_1, 'scheduled'] = from_scheduled
      df.at[id_1, 'edit_date'] = edit_date
      df.at[id_1, 'edit_hide'] = edit_hide

run(messages_func(name, api_id, api_hash))

df = df.reset_index(names='index')
df.to_csv(path)