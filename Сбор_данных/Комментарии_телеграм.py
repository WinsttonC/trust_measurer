
import telethon
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
sum_list = []
dict_users = {}


senders_list = []
async def comments_func(name, api_id, api_hash):
  i = 0
  error_counter = 0
  async with TelegramClient(name, api_id, api_hash) as client:
      print("Extracting messages")
      for index in df['index']: 
        com = []
        messages_2 = client.iter_messages(chat, reply_to = index)
        # Заменяем значение ячейки в столбце 'count_reaction'
        i +=1
        try:
            async for mes in messages_2:
                senders_list.append(mes.from_id)
        
        except telethon.errors.RPCError as e:
            if "The message ID used in the peer was invalid" in str(e):
                error_counter =+ 1
                print("Произошла ошибка 'The message ID used in the peer was invalid'. Продолжение цикла...")
                continue
      
      top_senders = pd.DataFrame({'sender' : senders_list})
      top_senders = top_senders['sender'].value_counts().head(20).index.tolist()
      try:
        for elem in top_senders:
            user = await client.get_entity(elem)
            print(user.first_name)
      except AttributeError as e:
        print(e)
    
run(comments_func(name, api_id, api_hash))
df.to_csv(path)