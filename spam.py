from telethon.tl import types
import os,time
from colorama import Fore
from telethon.tl.functions.messages import GetHistoryRequest 
from telethon import TelegramClient, events, sync


if os.path.isfile('session_name.session-journal'):
  os.remove('session_name.session-journal')
  os.remove('session_name.session')
file=open('x', 'w')
file.write('1')
file.close()
file=open(".api_id", "r")
api_id= (file.read())
file.close
file=open(".api_hash", "r")
api_hash= (file.read())
file.close
if api_id==(""):
  api_id=input("введіть api_id: ")
  file=open(".api_id", "w")
  file.write(api_id)
  file.close()
if api_hash==(""):
  api_hash=input("введіть api_hash: ")
  file=open(".api_hash", "w")
  file.write(api_hash)
  file.close()
def cls():
    os.system("clear")

client = TelegramClient("session_name", api_id, api_hash)

client.start()
cls()

z = "1"


@client.on(events.NewMessage)
async def handle_message(event):
    if event.message.out:
        if hasattr(event.message.peer_id, 'user_id'):
          id=event.message.peer_id.user_id
        if event.text[:5] in ('.spam','.спам'):
          mes=event.text[6:]
          d = mes.rfind(' ')
          g = mes[d+1:]
          await client.delete_messages(event.message.peer_id, event.message.id)
          i=1
          if g != '':
            while i <=(int(g)):
              await event.respond(f'{mes[:d]}')
              i = i + 1
        elif event.text[:7] == ('.реверс'):
          mes=event.text[8:]
          await client.delete_messages(event.message.peer_id, event.message.id)
          mess=mes[::-1]
          await event.respond(f'{mess}')
        elif event.text[:5] in ('.маг1','.mag1'):
          mes=event.text[6:]
          mess = len(mes)
          mess==mess-1
          i=1
          await event.edit("░")
          time.sleep(0.2)
          while i<mess:
            gg=mes[0:i]
            await event.edit(f"{gg}░")
            i=i+1
            time.sleep(0.2)
          await event.edit(mes)
        elif event.text[:5] in ('.маг2','.mag2'):
          mes=event.text[6:]
          mess = len(mes)
          mess==mess-1
          await event.edit("️❤️‍")
          time.sleep(0.2)
          i=1
          while i<=mess:
            gg=mes[0:i]
            await event.edit(f"{gg}️❤️‍")
            i=i+1
            time.sleep(0.2)
        elif event.text[:4] in ('.маг','.mag'):
          mes=event.text[5:]
          mess = len(mes)
          mess==mess-1
          i=1
          await event.edit("#")
          await event.edit("$")
          await event.edit("@")
          await event.edit("₴")
          g=mes[0]
          await event.edit(f"{g}₴")
          while i<mess:
            gg=mes[0:i]
            await event.edit(f"{gg}#")
            await event.edit(f"{gg}$")
            await event.edit(f"{gg}@")
            await event.edit(f"{gg}₴")
            i=i+1
          await event.edit(mes)
        elif event.text[:5] == ".code":
          codes = event.text[6:]
          file=open('proga.py', 'w')
          file.write(codes)
          file.close()
          os.system("python proga.py > result.txt")
          file=open("result.txt", "r")
          result= (file.read())
          file.close()
          await event.respond(f"Вывод:\n{result}")
        elif event.text in ('.clear','Clear','clear'):
          os.system("clear")
          await event.edit("clear✅")
        elif event.text[:5] in ('magic','Magic'):
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍️❤️‍️❤️‍🤍️‍️❤️‍️️❤️‍🤍️‍🤍️‍
🤍️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️🤍️‍
🤍️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍🤍️‍
🤍️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍🤍️‍
🤍️‍🤍️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍️❤️‍️❤️‍️❤️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍️❤️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🧡️‍🧡️‍🤍️‍🧡️‍🧡️‍🤍️‍🤍️‍
🤍️‍🧡️‍🧡️‍🧡️‍🧡️‍🧡🧡️‍🧡️‍🤍️‍
🤍️‍🧡️‍🧡️‍🧡️‍🧡️‍🧡️‍🧡️‍🧡️‍🤍️‍
🤍️‍🧡️‍🧡️‍🧡️‍🧡️‍🧡️‍🧡️‍🧡️‍🤍️‍
🤍️‍🤍️‍🧡️‍🧡️‍🧡️‍🧡️‍🧡️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🧡️‍🧡️‍🧡️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🧡️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍💛💛️‍🤍️‍💛️‍💛️‍🤍️‍🤍️‍
🤍️‍💛️‍💛️‍💛️‍💛️‍💛️‍💛️‍💛️‍🤍️‍
🤍️‍💛️‍💛️‍💛️‍💛️‍💛️‍💛️‍💛️‍🤍️‍
🤍️‍💛️‍💛️‍💛️‍💛️‍💛️‍💛️‍💛️‍🤍️‍
🤍️‍🤍️‍💛️‍💛️‍💛️‍💛️‍💛️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍💛️‍💛️‍💛️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍💛️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍💚️‍💚️‍🤍️‍💚️‍💚️‍🤍️‍🤍️‍
🤍️‍💚️‍💚️‍💚️‍💚️‍💚️‍💚️‍💚️‍🤍️‍
🤍️‍💚️‍💚️‍💚️‍💚️‍💚️‍💚️‍💚️‍🤍️‍
🤍️‍💚️‍💚️‍💚️‍💚️‍💚️‍💚️‍💚️‍🤍️‍
🤍️‍🤍️‍💚️‍💚️‍💚️‍💚️‍💚️‍🤍️‍🤍️‍
🤍🤍️‍🤍️‍💚️‍💚️‍💚️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍💚️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍💙️‍💙️‍🤍️‍💙️‍💙️‍🤍️‍🤍️‍
🤍️‍💙️‍💙️‍💙️‍💙️‍💙️‍💙️‍💙️‍🤍️‍
🤍️‍💙️‍💙️‍💙️‍💙️‍💙️‍💙️‍💙️‍🤍️‍
🤍️‍💙️‍💙️‍💙️‍💙️‍💙️‍💙️‍💙️‍🤍️‍
🤍️‍🤍️‍💙️‍💙️‍💙️‍💙️‍💙️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍💙️‍💙️‍💙️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍💙️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍💜️‍💜️‍🤍️‍💜️‍💜️‍🤍️‍🤍️‍
🤍️‍💜️‍💜️‍💜️‍💜️‍💜️‍💜️‍💜️‍🤍️‍
🤍️‍💜️‍💜️‍💜️‍💜️‍💜️‍💜️‍💜️‍🤍️‍
🤍️‍💜️‍💜️‍💜️‍💜️‍💜️‍💜️‍💜️‍🤍️‍
🤍️‍🤍️‍💜️‍💜️‍💜️‍💜️‍💜️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍💜️‍💜️‍💜️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍🤍️‍💜️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🖤️‍🖤️‍🤍️‍🖤️‍🖤️‍🤍️‍🤍️‍
🤍️‍🖤️‍🖤️‍🖤️‍🖤️‍🖤️‍🖤️‍🖤️‍🤍️‍
🤍️‍🖤️‍🖤️‍🖤️‍🖤️‍🖤️‍🖤️‍🖤️‍🤍️‍
🤍️‍🖤️‍🖤️‍🖤️‍🖤️‍🖤️‍🖤️‍🖤️‍🤍️‍
🤍️‍🤍️‍🖤️‍🖤️‍🖤️‍🖤️‍🖤️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🖤️‍🖤️‍🖤️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🖤️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍💙️‍💛️‍🤍️‍💛️‍💙️‍🤍️‍🤍️‍
🤍️‍💙️‍💛️‍💙️‍💛️‍💙️‍💛️‍💙️‍🤍️‍
🤍️‍💛️‍💙️‍💛️‍💙️‍💛️‍💙️‍💛️‍🤍️‍
🤍️‍💙️‍💛️‍💙️‍💛️‍💙️‍💛️‍💙️‍🤍️‍
🤍️‍🤍️‍💙️‍💛️‍💙️‍💛️‍💙️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍💙️‍💛️‍💙️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍💙️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍💜️‍🧡️‍🤍️‍🧡️‍💜️‍🤍️‍🤍️‍
🤍️‍💜️‍🧡️‍💜️‍🧡️‍💜️‍🧡️‍💜️‍🤍️‍
🤍️‍🧡️‍💜️‍🧡️‍💜️‍🧡️‍💜️‍🧡️‍🤍️‍
🤍️‍💜️‍🧡️‍💜️‍🧡️‍💜️‍🧡️‍💜️‍🤍️‍
🤍️‍🤍️‍💜️‍🧡️‍💜️‍🧡️‍💜️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍💜️‍🧡️‍💜️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍💜️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍️❤️‍🧡️‍🤍️‍🧡️‍️❤️‍🤍️‍🤍️‍
🤍️‍️❤️‍🧡️‍️❤️‍🧡️‍️❤️‍🧡️‍️❤️‍🤍️‍
🤍️‍🧡️‍️❤️‍🧡️‍️❤️‍🧡️‍️❤️‍🧡️‍🤍️‍
🤍️‍️❤️‍🧡️‍️❤️‍🧡️‍️❤️‍🧡️‍️❤️‍🤍️‍
🤍️‍🤍️‍️❤️‍🧡️‍️❤️‍🧡️‍️❤️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍️❤️‍🧡️‍️❤️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍️❤️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🩵️‍🩵️‍🤍️‍💛️‍💛️‍🤍️‍🤍️‍
🤍️‍🩵️‍🩵️‍🩵️‍💛️‍💛️‍💛️‍🩷️‍🤍️‍
🤍️‍🩵️‍🩵️‍💛️‍💛️‍💛️‍🩷️‍🩷️‍🤍️‍
🤍️‍🩵️‍💛️‍💛️‍💛️‍🩷🩷️‍💛️‍🤍️‍
🤍️‍🤍️‍💛️‍💛️‍🩷️‍🩷️‍💛️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🩷️‍🩷️‍💛️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍💛️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🩵🩵️‍🤍️‍💛️‍💛️‍🤍️‍🤍️‍
🤍️‍🩵️‍🩵️‍🩵️‍💛️‍💛️‍💛️‍🩷️‍🤍️‍
🤍️‍🩵️‍🩵️‍💛️‍💛️‍💛️‍🩷️‍🩷️‍🤍️‍
🤍️‍🩵️‍💛️‍💛️‍💛🩷️‍🩷️‍💛️‍🤍️‍
🤍️‍🤍️‍🧡️‍🧡️‍️❤️‍️❤️‍💛️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍️❤️‍️❤️‍💛️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍💛️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🩵️‍🩵️‍🤍️‍💛️‍💛️‍🤍️‍🤍️‍
🤍️‍🩵️‍🩵️‍🩵️‍💛️‍💛️‍💛️‍🩷️‍🤍️‍
🤍️‍💙️‍💙️‍🧡️‍🧡️‍🧡️‍️❤️‍️❤️‍🤍️‍
🤍️‍💙️‍🧡️‍🧡️‍🧡️‍️❤️‍️❤️‍💛️‍🤍️‍
🤍️‍🤍️‍🧡️‍🧡️‍️❤️‍️❤️‍💛️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍️❤️‍️❤️‍💛️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍💛️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍💙️‍💙🤍️‍🧡️‍🧡️‍🤍️‍🤍️‍
🤍️‍💙️‍💙️‍💙️‍🧡️‍🧡️‍🧡️‍️❤️‍🤍️‍
🤍️‍💙️‍💙️‍🧡️‍🧡️‍🧡️‍️❤️‍️❤️‍🤍️‍
🤍️‍💙️‍🧡️‍🧡️‍🧡️‍️❤️‍️❤️‍💛️‍🤍️‍
🤍️‍🤍🧡️‍🧡️‍️❤️‍️❤️‍💛️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍️❤️‍️❤️‍💛️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍💛️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍️❤️‍️❤️‍🤍️‍️❤️‍️️❤️‍🤍️‍🤍️‍
🤍️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️🤍️‍
🤍️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍🤍️‍
🤍️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍🤍️‍
🤍️‍🤍️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍️❤️‍️❤️‍️❤️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍️❤️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""️️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️
🤍️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍🤍️‍
🤍️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍🤍️‍
🤍️‍🤍️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍️❤️‍️❤️‍️❤️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍🤍️‍🤍️‍️❤️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""️❤️‍️❤️‍️❤️‍️️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
🤍️‍🤍️‍🤍️‍️❤️‍️❤️‍️❤️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍️❤️‍🤍️‍🤍️‍🤍️‍🤍️‍
🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍🤍️‍""")
          time.sleep(0.2)
          await event.edit("""️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️""")
          time.sleep(0.2)
          await event.edit("""️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️️
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍""")
          time.sleep(0.2)
          await event.edit("""️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍""")
          time.sleep(0.2)
          await event.edit("""️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍""")
          time.sleep(0.2)
          await event.edit("""️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍️❤️‍""")
          time.sleep(0.2)
          await event.edit("""️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍️❤️‍""")
          time.sleep(0.2)
          await event.edit("""️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍
️❤️‍️❤️‍️❤️‍""")
          time.sleep(0.2)
          await event.edit("""️❤️‍️❤️‍
️❤️‍️❤️‍""")
          time.sleep(0.2)
          await event.edit("❤️")
        elif event.text[:5] == '.fake':
          if hasattr(event.message.peer_id, 'user_id'):
            chat=event.message.peer_id.user_id
          elif hasattr(event.message.peer_id, 'channel_id'):
            chat=event.message.peer_id.channel_id
          phone=event.text[6:19]
          name=event.text[19:]
          await client.send_file(chat, types.InputMediaContact(
    phone_number=phone,
    first_name=name,
    last_name='',
    vcard=''
))
        elif event.text[:5] == '.hole':
          os.system(f"holehe {event.text[6:]} > result2.txt")
          file=open("result2.txt", "r")
          result= (file.read())
          file.close
          R=result.find('@gmail.com')+10
          F=result.find('[+] Email used')
          results=result[R:F]
          while results.find("[+]") != -1:
            xy=results.find('[+]')
            results=results[:xy]+"🟢"+results[xy+3:]
          while results.find("[-]") != -1:
            xy=results.find('[-]')
            results=results[:xy]+"🟣"+results[xy+3:]
          while results.find("[x]") != -1:
            xy=results.find('[x]')
            results=results[:xy]+"🔴"+results[xy+3:]

          results= (f"{results}\n[🟢] Зарегистрирован,\n[🟣] Не Зарегистрирован,\n[🔴] Не получилось проверить")
          await event.respond(results)
        elif event.text[:4] == ".cal":
          codes = event.text[5:]
          file=open('proga.py', 'w')
          file.write(f"print({codes})")
          file.close()
          os.system("python proga.py > result.txt")
          file=open("result.txt", "r")
          result= (file.read())
          await event.edit(f"{event.text[5:]}={result}")
          file.close()
        elif event.text[:4] in (".ver",".вер"):
          i = 1
          x=event.text[5:]
          while x.find(" ") != -1:
            xy=x.find(' ')
            x=x[:xy]+"_"+x[xy+1:]
          await client.delete_messages(event.message.peer_id, event.message.id)
          while i <= len(x):
            await event.respond(x[i-1])
            i+=1
        elif event.text[:1] == ".":
          os.system(f"{event.text[1:]} > result2.txt")
          file=open("result2.txt", "r")
          result= (file.read())
          file.close
          await event.respond(result)
        elif event.text.find(')') != -1:
          print(event)
        elif event.text in ('exit', 'Exit'):
          await event.edit('Exit ✅')
          file=open('x', 'w')
          file.write("11")
          file.close()
    else:
      if hasattr(event.message.peer_id, 'user_id'):
        id=event.message.peer_id.user_id
      if event.text[:5] == ".code":
        codes = event.text[6:]
        file=open('proga.py', 'w')
        file.write(codes)
        file.close()
        os.system("python proga.py > result.txt")
        file=open("result.txt", "r")
        result= (file.read())
        file.close()
        await event.respond(f"Вывод:\n{result}")
while z=="1":
  file=open('x', 'r')
  z=(file.read())
  file.close()
  for m in client.iter_messages('me', 1):
    if m.message in ("exit","Exit"):
      client.send_message('me', "ok")
      z=z+"1"
  