from pystyle import Center
import discum, re, requests, json, datetime, random, os
import httpx
from flask import Flask, render_template
from threading import Thread
app = Flask('')
@app.route('/')
def home():
  return "bot python is online!"
def index():
  return render_template("index.html")
def run():
  app.run(host='0.0.0.0', port=8080)
def H():
  t = Thread(target=run)
  t.start()

H()


# ตั้งค่าในไฟล์ Setting.json
token = os.environ.get('token') # โทเค่นคนที่จะใช้ดัก / ไม่ใช่บอท
phone = os.environ.get('phone') # เบอร์รับตัง
webhook = os.environ.get('webhook') # เว็ปฮุ้ก

regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
bot = discum.Client(token=token,log=False)
regexx = 'https://gift.truemoney.com/campaign/?v='

def sendwebhook(sendgift):
    description = f"```{sendgift}```"
    image_url = "https://cdn.discordapp.com/attachments/1215617138124005387/1220308645271568384/546838.jpg?ex=660e77fd&is=65fc02fd&hm=3481cb750aab9ff144fa28ab788e7b72899d5e5d10ce1af9d801761a3560cd5d&"
    webhook_name = "ดักอั่งเปา"
    webhook_title = "phishing gift"
    time = datetime.datetime.utcnow()
    title_url ="highzixdev_69"
    icon_url = "https://cdn.discordapp.com/attachments/1215617138124005387/1220308645271568384/546838.jpg?ex=660e77fd&is=65fc02fd&hm=3481cb750aab9ff144fa28ab788e7b72899d5e5d10ce1af9d801761a3560cd5d&"
    avatar_url ="https://cdn.discordapp.com/attachments/1215617138124005387/1220308645271568384/546838.jpg?ex=660e77fd&is=65fc02fd&hm=3481cb750aab9ff144fa28ab788e7b72899d5e5d10ce1af9d801761a3560cd5d&"
    footer = "blackmarket"
    randcolor = random.randint(0x000000, 0xFFFFFF)
    data = {
    "content": "@everyone",
      "embeds": [
        {
          "title": f"{webhook_title}",
          "tts": "true",
          "description": f"\n{description}",
          "url": f"{title_url}",
          "color": f"{randcolor}",
          "timestamp": f"{time}",
          "author": {
            "name": f"{webhook_name}",
            "url": f"{title_url}",
            "icon_url": f"{icon_url}"
          },
          "footer": {
            "text": f"{footer}",
            "icon_url": f"{icon_url}"
          },
          "image": {
            "url": f"{image_url}"
          }
        }
      ],
      "username": f"{webhook_name}",
      "avatar_url": f"{avatar_url}"
    }
    requests.post(webhook, json=data)

cr = '''
\33[33m╔═══╦╗──╔╦══╗╔═══╦═══╦═══╦═══╦═══╦═══╗
\33[33m║╔═╗║╚╗╔╝║╔╗║║╔══╣╔═╗║╔═╗║╔═╗║╔══╣╔══╝
\33[33m║║─╚╩╗╚╝╔╣╚╝╚╣╚══╣╚═╝║╚══╣║─║║╚══╣╚══╗         \33[35mFACEBOOK \33[30m:\33[31m Highzixdev_69#0000
\33[33m║║─╔╗╚╗╔╝║╔═╗║╔══╣╔╗╔╩══╗║╚═╝║╔══╣╔══╝         \33[35mDISCORD \33[30m:\33[31m https://discord.com/invite/sPZ2XnpMB2
\33[33m║╚═╝║─║║─║╚═╝║╚══╣║║╚╣╚═╝║╔═╗║║──║╚══╗         \33[35mWEB \33[30m:\33[31m https://highzy.ovdc.xyz/?page=shop
\33[33m╚═══╝─╚╝─╚═══╩═══╩╝╚═╩═══╩╝─╚╩╝──╚═══╝         
══╦═════════════════════════════════╦══
'''

@bot.gateway.command
def somefunctionname(resp):
    if resp.event.ready_supplemental:
      user = bot.gateway.session.user
      os.system('cls' if os.name == 'nt' else 'clear')
      os.system("title PSISHING GIFT DISCORD ^| BY HIGHZY")
      print(Center.XCenter(cr))
      print(f"\n\33[35mLogged in as \33[33m{user['username']}#{user['discriminator']}")
    if resp.event.ready_supplemental:
        pass
    if resp.event.message:
            url = re.findall(regex,resp.parsed.auto()["content"])
            URL = list(map(lambda x:list(x)[0],url))
            if len(URL) > 0:
                for i in range(len(URL)):
                    URL = URL[0]
                    linkgift = str(URL.split("https://gift.truemoney.com/campaign/?v=")[1])
                    responseapi = httpx.post(f"https://gift.truemoney.com/campaign/vouchers/{linkgift}/redeem",json={"mobile":f"{phone}","voucher_hash":f"{linkgift}"},headers={"Accept": "application/json","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36","Content-Type": "application/json","Origin": "https://gift.truemoney.com","Accept-Language": "en-US,en;q=0.9","Connection": "keep-alive"})
        
                    if responseapi.status_code == 200:
                        # print(responseapi.json())
                        ownergift = responseapi.json()["data"]["owner_profile"]["full_name"]
                        amountbaht = responseapi.json()["data"]["voucher"]["amount_baht"]
                        # return(f"รับเงินจาก {ownergift} จํานวน {amountbaht}")
                        e = f'link {resp.parsed.auto()["content"]}\nformguild {resp.parsed.auto()["guild_id"]}\ninchannlid {resp.parsed.auto()["channel_id"]}'
                        sendwebhook(e)
                    else:
                        print("รับเงินไม่สําเร็จ")
            
                    
                    # if requests.get(api).json()["status"] == "SUCCESS":
                    #     e = f'link {resp.parsed.auto()["content"]}\nformguild {resp.parsed.auto()["guild_id"]}\ninchannlid {resp.parsed.auto()["channel_id"]}'
                    #     sendwebhook(e)
                    # else:
                    #     pass
                    # print(URL[i])
            else:
                pass
            # print(resp.parsed.auto())
            # sendwebhook(e)
            # print(resp.parsed.auto())
            
bot.gateway.run()
