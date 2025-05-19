import discord
import os

from random import randint
import random
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timedelta
import json
import asyncio
import requests


import threading
import flask

# Luo Flask-palvelu pitämään Railway-prosessi hengissä
app = flask.Flask(__name__)

@app.route('/')
def home():
    return "Botti toimii!"

def run():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# Käynnistä Flask erillisessä säikeessä
t = threading.Thread(target=run)
t.daemon = True
t.start()


DISCORD_TOKEN = "MTMzMDg2NDE2MDUyNzA5Mzg5Mw.G1I7M5.vkf_UU21pwQ7YkDYGXe5hIoWpqiuksYg0xnRNE"

krisu = 312961264286695424
jani = 277091775812861952
ape = 241562953592078336
jokke = 443809016133582849
samppa = 344499563991793674
cape = 422427713052082177

lista = [krisu, jani, ape, jokke, samppa, cape]



quotet = ['“Know thyself.” — Socrates', '“Happiness depends upon ourselves.” — Aristotle', '“Man is disturbed not by things, but by the views he takes of them.” — Epictetus',
          '“He who has a why to live can bear almost any how.” — Friedrich Nietzsche', '“We are what we repeatedly do. Excellence, then, is not an act, but a habit.” — Aristotle',
          '“The unexamined life is not worth living.” — Socrates', '“Act only according to that maxim whereby you can, at the same time, will that it should become a universal law.” — Immanuel Kant',
          '“Do not spoil what you have by desiring what you have not.” — Epicurus', '“It is not length of life, but depth of life.” — Ralph Waldo Emerson', '“The only thing I know is that I know nothing.” — Socrates',
          '“To live is the rarest thing in the world. Most people exist, that is all.” — Oscar Wilde', '“You must become who you are.” — Friedrich Nietzsche', '“The mind is everything. What you think you become.” — Buddha',
          '“Be kind, for everyone you meet is fighting a hard battle.” — Attributed to Plato (though debated)', '“Time is a created thing. To say ‘I don’t have time’ is like saying ‘I don’t want to.’” — Laozi',
         '“Waste no more time arguing what a good man should be. Be one.” — Marcus Aurelius', '“He who opens a school door, closes a prison.” — Victor Hugo', '“The greater the difficulty, the more glory in surmounting it.” — Epicurus',
         '“No man ever steps in the same river twice, for it’s not the same river and he’s not the same man.” — Heraclitus', '“What we achieve inwardly will change outer reality.” — Plutarch',
         '“Even while they teach, men learn.” — Seneca', '“The only journey is the one within.” — Rainer Maria Rilke', '“The meaning of life is to find your gift. The purpose of life is to give it away.” — Pablo Picasso',
         '“To be is to be perceived.” — George Berkeley', '“Every man takes the limits of his own field of vision for the limits of the world.” — Arthur Schopenhauer', 
         '“Live as if you were to die tomorrow. Learn as if you were to live forever.” — Mahatma Gandhi', '“Freedom is the freedom to say that two plus two make four.” — George Orwell', 
         '“Silence is a source of great strength.” — Laozi', '“You can discover more about a person in an hour of play than in a year of conversation.” — Plato', 
         '“To dare is to lose one’s footing momentarily. Not to dare is to lose oneself.” — Søren Kierkegaard', '“Nature does not hurry, yet everything is accomplished.” — Laozi']
          

intents = discord.Intents.default()
intents.message_content = True
 


class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')


        try:
            guild = discord.Object(id=548149996462145546)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')

        except Exception as e:
            print(f'Failed to sync commands: {e}')



    async def on_message(self, message):
        if message.author == self.user:
            return

        print(f"Vastaan viestiin: {message.content}")
        
        if message.content == 'moi botti':
            await message.channel.send(f'Heipparallaa {message.author}')

        if message.content == 'hyvä botti':
            await message.channel.send(f'Kiitos {message.author}!')
            await message.add_reaction('🏆')

        if message.content == 'paska botti':
            await message.channel.send(f'Okei mut aatelkaa kui noloo ois olla tää äijä ---> {message.author}')

        if "tuhma botti" in message.content:
            await message.channel.send(f'Mmmh miten tuhma? 🤤')
            await message.add_reaction('🤭')


        if message.content == 'homo':
            await message.channel.send(f'En oo homo ku oli sukat jalas')

        if message.author.id == 1366534715485589514:
            await message.reply('😐bro got the whole squad laughing')

        if message.author.id == 277091775812861952:
            await message.reply('nadal atm')


        if 'neeker' in message.content:
            await message.channel.send(f'{message.author} <--- tämä henkilö on rasisti')

        if 'nigg' in message.content:
            await message.channel.send(f'{message.author} <--- tämä henkilö on rasisti')

        if 'fortnite' in message.content.lower():
            viesti = "☝️😃Number One#️⃣1️⃣Victory Royale🏆🥇Yeah, Fortnite🏕️we bout to👇get down (get down)⬇️Ten🔟kills☠️on🔛the board🎯right now⏱️Just wiped out💥Tomato🍅Town🏡My friend👯‍♂️just got🙇🏻‍♂️downed😱I revived💉him😇now we’re heading🏃🏃‍♂️south🧭bound⬇️Now we’re in👉the Pleasent😊Park🏞️streets🏘️Look👀at the map🗺️go to the mark✅sheet📝Take me🤝to your Xbox🎮📺to play🕹️Fortnite🏕️today📅You can take🤝me🏃‍♂️to Moist💦Mire🐊but not🙅🏻‍♂️Loot💰Lake🌊🤢I'd really love❤️🥰to chug jug🍻with you😳👉👈We can be pro😎Fortnite🏕️gamers👾🎮🕹️"
            await message.channel.send(viesti)

        if 'samppa' in message.content.lower():
            viesti1 = f"If <@{samppa}> has a million fans, then I am one of them. If <@{samppa}> has ten fans, then I am one of them. If <@{samppa}> has only one fan then that is me. If <@{samppa}> has no fans, then that means I am no longer on earth. If the world is against <@{samppa}>, then I am against the world."
            await message.channel.send(viesti1)

        if 'paavi' in message.content.lower():
            v2 = f"🪦 RIP 💀 to FREAKY 🫦 POPE ✝️ FRANCIS 👴 who partied 💃 too hard 🍆 👀 this 4️⃣ /2️⃣ 0️⃣ 🌬️ 🌿 and got too LIT 🚬 on EASTER 🐰 and has sadly pASSed 🍑 on 🪦 from this life 🌎 at 8️⃣ 8️⃣ years old 👴 Now ‼️ he can sanctify ✝️ some SLUTS 👧 up ⬆️ in heaven 👼 with his 👀 side 👀 piece ❤️ JESUS 🙇‍♂️ CHRIST ✝️ He 🧑 will be fondlingly 🥵 remembered 🤔 as the FREAKIEST 😈 pope 😫 who NEVER 🚫 touched 👐 little boys 🧒 AND ‼️ made sure 💡 to show 🔍 LOVE ❤️ to everyone 🏳️‍🌈 around 🍑 the world 🌎 So get 👐 your bread 🍞 and eat 🤤 the BUSSY 🍑 of Christ ✝️ and drink 🤤 some cummy 💦 wine 🍷 for CUMMUNION 💦 💦 to ensure 🙏 your pASSage 🍑 to heaven 👼 with good 🤗 ole' FRANCIS 👴 Send 💌 this to ➡️ your 🔟 most ✝️ CHRISTLY 👼 CUNTS 👭 and if you 🫵 get 0️⃣ back 🍑 you're 🫵 a 👹 HEAVENLESS 👿 WHORE 🍆 👅 if you 🫵 get 5️⃣ back ⬅️ you're 🫵 a NAUGHTY 🥵 LITTLE 🤏 ALTER 🕺 BOY 😳 and if you 🫵 get 🔟 back you're 😜 a REAL 🔥 SPIRITUAL ✝️ SLUT 💦"
            await message.channel.send(v2)

        if 'treffi' in message.content.lower():
            v3 = f"Not gonna be active on Discord tonight. I'm meeting a girl (a real one) in half an hour (wouldn't expect a lot of you to understand anyway) so please don't DM me asking me where I am (im with the girl, ok) you'll most likely get aired because i'll be with the girl (again I don't expect you to understand) shes actually really interested in me and its not a situation i can pass up for some meaningless Discord degenerates (because i'll be meeting a girl, not that you really are going to understand) this is my life now. Meeting women and not wasting my precious time online, I have to move on from such simple things and branch out (you wouldnt understand)"
            await message.channel.send(v3)

        if 'tyttö' in message.content.lower():
            v4 = f"No way 🤯 girl on discord? 🧐 Howdy I didn't expect to see no girl round dees parts 🤠 allow me to introduce myself to you mlady 😤 you can call me Jamal and I'll call you my kitten 🤓 I moderate multiple discord servers y'know I'm a man of high status 😁 I've been looking for some female companionship lately 🤗 and since my mother has thrown me out of the basement I'm not an independent person 😎 some may even refer to me as a big boy ☺️ I live in a homeless shelter tho 🤧 and I have no job 😄 I have hobbies such as reddit and discord and anime so I'm quirky like that 😵‍💫I live of disability benefits which I spend on funko pops and anime figurines 🤑 the homeless shelter however does not allow me more than 5 hours of reddit time so it's literally 1984 😓 but please give me a chance mlady cuz I just need you to cook me food and let me live in your house and give me money and change my diapers and pay for my Nitro 🤩 Other than that I am a nice guy 😍"
            await message.channel.send(v4)

        if 'kitten' in message.content.lower():
            v5 = f"❤️ Rules for discord Kitten: ❤️ 1. Bedtime on school nights is 11:00 pm. 2. Bedtime on weekends is 2 am. 3. Eat at least TWO meals a day. 4. Eat one healthy snack each day. 5. No self-harm. Come talk to Daddy if you need support! 6. No lying to Daddy. 7. Respect Daddy 8. ALWAYS ask for permission before taking pills. 9. You must compliment yourself at least once per day. 10. Do not let other boys (or girls) lust after you — You BELONG to Daddy!!! 11. No drinking without permission. 12. No drugs. 13. No eating after 8 pm. 14. You may not please yourself out side of playtime with daddy. Daddy may make exceptions to the aforementioned rules, Kitten may not. Disobeying Daddys rules will result in punishment."
            await message.channel.send(v5)
            
        await self.process_commands(message)


def get_questions():
    url = f"https://the-trivia-api.com/v2/questions/"
    response = requests.get(url, headers={})
    data = response.json()

    randomnro = randint(0, len(data)-1)

    kysymys = data[randomnro]

    kys = kysymys['question']['text']

    vast = kysymys['incorrectAnswers']
    oikvast = kysymys['correctAnswer']

    vastaukset = [vast[0], vast[1], vast[2], oikvast]
    random.shuffle(vastaukset)

    tarkistus = {}

    tarkistus[kys] = oikvast

    return vastaukset, tarkistus


def get_daily_quote():
    today = datetime.today().date()
    random.seed(today.toordinal())
    return random.choice(quotet)



intents = discord.Intents.default()
intents.message_content = True

client = Client(command_prefix='!', intents=intents)


GUILD_ID = discord.Object(id=548149996462145546)

def kryptaa_lause(lause):
    lause = lause.lower()
    kirjaimet = sorted(set([c for c in lause if c.isalpha()]))
    arvotut_numerot = random.sample(range(1, 100), len(kirjaimet))  # numerot 1–99
    kirjain_numero = dict(zip(kirjaimet, arvotut_numerot))

    kryptattu = []
    for merkki in lause:
        if merkki.isalpha():
            kryptattu.append(str(kirjain_numero[merkki]))
        else:
            kryptattu.append(merkki)  # säilytetään välilyönnit, pilkut yms.

    return ' '.join(kryptattu), kirjain_numero
    
    
    


@client.tree.command(name='skibidi', description='Paljastaa kuka on tällä hetkellä skibidi sammakko!', guild=GUILD_ID)
async def skibidi(interaction: discord.Interaction):
    ukko = lista[randint(0,5)]
    await interaction.response.send_message(f'Skibidi sammakko on tällä hetkellä: <@{ukko}>')

@client.tree.command(name='sigma', description='Paljastaa kuka on tällä hetkellä sigma male!', guild=GUILD_ID)
async def sigma(interaction: discord.Interaction):
    ukko = lista[randint(0,5)]
    await interaction.response.send_message(f'Sigma male on tällä hetkellä: <@{ukko}>')

@client.tree.command(name='laskin', description='syötä lasku, niin suoritan sen! Muista erottaa välilyönnillä numerot ja välimerkki', guild=GUILD_ID)
async def laskin(interaction: discord.Interaction, syöte: str):

    st = syöte.split()
    luku1 = int(st[0])
    luku2 = int(st[2])
    if st[1] == "+":
        viesti = f"{luku1} + {luku2} = {luku1 + luku2}"
    elif st[1] == "-":
        viesti = f"{luku1} - {luku2} = {luku1 - luku2}"
    elif st[1] == "*":
        viesti = f"{luku1} * {luku2} = {luku1 * luku2}"
    elif st[1] == "/":
        viesti = f"{luku1} / {luku2} = {luku1 / luku2}"
    else:
        await interaction.response.send_message("Virheellinen syöte, yritä uudelleen!")
    await interaction.response.send_message(viesti)

        
    
    


@client.tree.command(name='random', description='random luku antamallasi välillä', guild=GUILD_ID)
async def randomi(interaction: discord.Interaction, number1: int, number2: int):
    await interaction.response.send_message(f'random luku väliltä {number1}-{number2} on {randint(number1, number2)}')
        

@client.tree.command(name="valitse", description="Valitsee satunnaisesti annetusta listasta! Erota vaihtoehdot pilkulla  --> , ", guild=GUILD_ID)
async def valitse(interaction: discord.Interaction, vaihtoehdot: str):
    vaihtoehdot_lista = vaihtoehdot.split(", ")
    valinta = vaihtoehdot_lista[randint(0, len(vaihtoehdot_lista)-1)]
    await interaction.response.send_message(f"Valitsen siis jonkun näistä: {vaihtoehdot}")
    await interaction.followup.send(f"Valitsen: {valinta}!")

@client.tree.command(name="ape", description="Tarkista apen parisuhdestatus!", guild=GUILD_ID)
async def ape(interaction: discord.Interaction):
    aika = datetime.now() - datetime(2021, 9, 1)
    await interaction.response.send_message(f"Ape on ollut sinkku vuodesta 2021 lähtien! Apen viimeisestä parisuhteesta on siis {aika.days} päivää. Sen aikana on ehtinyt tapahtua vaikka mitä. Tässä lista asioista, jotka ovat tapahtuneet apen sinkkuuden aikana: \n1. Ape ehti käydä armeijassa, töissä, sivarissa ja aloittaa koulun \n2. Cape ja Jani ehti muuttaa pois kotoa ja hankkia kumppaneita ja lemmikkejä \n3. Krisun penis ehti kasvaa 2 milliä \n4. Jokke ehti käydä armeijassa KOLME kertaa \n5. Jokke ehti saada syyhyn, parantua siitä ja hankkia kumppanin ja erota sen kaa jo kerran \n6. Jokerit ehti lähteä KHL:stä, vaihtaa kotihallia ja mennä Mestikseen  \n7. Man City ehti voittaa treblen ja 2 Valioliigaa  \n8. Trump ehti olla presidenttinä, hävitä vaalit ja päästä uudelleen presidentiksi \n9. Verstappen ehti voittaa 4 mestaruutta \n10. Krisu ehti käydä armeijan, olla työttömänä, hankkia kumppanin ja löytää vakkariduunin")

@client.tree.command(name="nyt", description="Kertoo nykyisen ajan", guild=GUILD_ID)
async def nyt(interaction: discord.Interaction):
    aika = datetime.now()
    suomiaika = aika + timedelta(hours=3)
    await interaction.response.send_message(f"Nyt on {suomiaika.strftime('%d.%m.%Y %H:%M:%S')}")


@client.tree.command(name="noppa", description="Heittää noppaa", guild=GUILD_ID)
async def noppa(interaction: discord.Interaction):
    await interaction.response.send_message(f"Nopan silmäluku: {randint(1, 6)}")

@client.tree.command(name="kolikko", description="Heittää kolikkoa", guild=GUILD_ID)
async def kolikko(interaction: discord.Interaction):
    tulos = "Kruuna" if randint(0, 1) == 0 else "Klaava"
    await interaction.response.send_message(f"Kolikonheiton tulos: {tulos}")


@client.tree.command(name="apesyndet", description="Kertoo kuinka kauan on apen synttäreihin!", guild=GUILD_ID)
async def synttärit(interaction: discord.Interaction):
    synttarit = datetime(2025, 7, 4) - datetime.now()
    await interaction.response.send_message(f"Apen synttärit ovat {synttarit.days} päivän päästä!")

@client.tree.command(name="jani", description="Kertoo Janin elämästä", guild=GUILD_ID)
async def jani(interaction: discord.Interaction):
    await interaction.response.send_message("Janilla on vakava autismi ja se on yksinäinen, mutta onneksi sillä on kuitenkin kavereita, jotka pitävät siitä huolta! Ja lisäksi se on myös aika hyvä tietokonepeleissä! Jani on joka tapauksessa aika hyvä tyyppi! Varsinkin kun se ei ole humalassa! Napsuu! Minulla on Janista paljon hyviä muistoja, mutta en muista niitä koskaan! Koska olen botti! Janilla on myös aika hyvä maku musiikissa, esimerkiksi Lassi Kuhlmanin Tiikeri! Janista tulee isona varmasti jotain hienoa! Mutta ensin Janin pitää parantua autismistaan!")

@client.tree.command(name="janinkihlajaiset", description="Onnittelee Jania ja Neaa kihlauksen johdosta!", guild=GUILD_ID)
async def kihloissa(interaction: discord.Interaction):
    kihloissa = lista[randint(0,5)]
    jani = 277091775812861952
    await interaction.response.send_message(f"Jani ja Nea menivät kihloihin 25.1.2025! Onneksi olkoon <@{jani}> ja Nea!🎉")
    await interaction.followup.send(f"Kihloissa ovat myös: Ape ja apen botti!")


@client.tree.command(name="sori", description="Antaa anteeksi! Kirjoita ensin keneltä pyydetään anteeksi ja sen jälkeen ketkä pyytävät anteeksi!", guild=GUILD_ID)
async def sori(interaction: discord.Interaction, keneltä: str):
    await interaction.response.send_message(f"Anteeksi {keneltä}😔 {interaction.user.mention} pyytää sinulta anteeksi!")


@client.tree.command(name="timer", description="Asettaa ajastimen! Kirjoita perään haluttu minuuttimäärä", guild=GUILD_ID)
async def timer(interaction: discord.Interaction, minutes: int):
    
    await interaction.response.send_message(f"Ajastin asetettu {minutes} minuutiksi!")
    
    await asyncio.sleep(minutes * 60)
    await interaction.followup.send("Aika loppui!")

@client.tree.command(name="stopwatch", description="Ottaa aikaa, kirjoita stop kun olet valmis!", guild=GUILD_ID)
async def ajanotto(interaction: discord.Interaction):
    start_time = datetime.now()
    await interaction.response.send_message("Ajanotto alkaa! Kirjoita stop kun olet valmis!")
    while True:
        response = await client.wait_for("message")
        if response.author != interaction.user:
            await interaction.followup.send("Väärä henkilö!")
            continue
        if response.content.lower() == "stop" and response.author == interaction.user:
            break
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    if elapsed_time.seconds < 60:
        await interaction.followup.send(f"Aikaa kului: {elapsed_time.seconds} sekuntia!")
    else:
        await interaction.followup.send(f"Aikaa kului: {elapsed_time.seconds//60} minuuttia ja {elapsed_time.seconds%60} sekuntia!")


@client.tree.command(name="trivia", description="Triviapeli. Kirjoita perään haluttujen kierrosten määrä! Max. 10", guild=GUILD_ID)
async def trivia(interaction: discord.Interaction, amount: int):
    await interaction.response.send_message("Tervetuloa triviaan! Kirjoita jotain aloittaaksesi!")
    jatkuuko = amount
    pisteet = 0
    väärä = 0
    while 11 > jatkuuko > 0:
        questions = get_questions()
        vastaukset = questions[0]
        tarkistus = questions[1]
        await interaction.followup.send(f"Kysymys: {list(tarkistus.keys())[0]} \n \nA) {vastaukset[0]} \nB) {vastaukset[1]} \nC) {vastaukset[2]} \nD) {vastaukset[3]}")

        a = vastaukset[0]
        b = vastaukset[1]
        c = vastaukset[2]
        d = vastaukset[3]

        while True:
            response = await client.wait_for("message")
            
            if response.author == interaction.user:
            
                if response.content.lower() == "a":
                    if a == list(tarkistus.values())[0]:
                        await interaction.followup.send("Oikein!✅")
                        pisteet += 1
                        break
                    else:
                        await interaction.followup.send("Väärin!❌")
                        väärä += 1
                        await interaction.followup.send(f"Oikea vastaus oli: {list(tarkistus.values())[0]}")
                        break
                if response.content.lower() == "b":
                    if b == list(tarkistus.values())[0]:
                        await interaction.followup.send("Oikein!✅")
                        pisteet += 1
                        break
                    else:
                        await interaction.followup.send("Väärin!❌")
                        väärä += 1
                        await interaction.followup.send(f"Oikea vastaus oli: {list(tarkistus.values())[0]}")
                        break
                if response.content.lower() == "c":
                    if c == list(tarkistus.values())[0]:
                        await interaction.followup.send("Oikein!✅")
                        pisteet += 1
                        break
                    else:
                        await interaction.followup.send("Väärin!❌")
                        väärä += 1
                        await interaction.followup.send(f"Oikea vastaus oli: {list(tarkistus.values())[0]}")
                        break
                if response.content.lower() == "d":
                    if d == list(tarkistus.values())[0]:
                        await interaction.followup.send("Oikein!✅")
                        pisteet += 1
                        break
                    else:
                        await interaction.followup.send("Väärin!❌")
                        väärä += 1
                        await interaction.followup.send(f"Oikea vastaus oli: {list(tarkistus.values())[0]}")
                        break

                else:
                    await interaction.followup.send("Väärä vastaus! Kirjoita A, B, C tai D!")
                    continue
            elif response.author.bot == True:
                continue
            else:
                await interaction.followup.send(f"Et voi osallistua {response.author.mention}! Tämä on käyttäjän {interaction.user.mention} peli!")
                continue

        jatkuuko -= 1
        await asyncio.sleep(2)
        if jatkuuko == 0:
            await interaction.followup.send(f"Peli päättyi! Pisteet🏅 {pisteet}")
            await interaction.followup.send(f"Oikeita vastauksia✅ {pisteet} \nVääriä vastauksia❌ {väärä}")
            await asyncio.sleep(2)
            await interaction.followup.send("Haluatko pelata lisää? Kirjoita 1 jos haluat jatkaa! Kirjoita mitä tahansa muuta jos haluat lopettaa! \nJos haluat asettaa automaattikierroksia, kirjoita haluamasi määrä! (Max. 10)")
        
            response = await client.wait_for("message")
            jatkuuko = int(response.content)


            
            
            
            


    

@client.tree.command(name="hirsi", description="Hirsipuu peli", guild=GUILD_ID)
async def hirsi(interaction: discord.Interaction, sana: str):
    await interaction.response.send_message("Tervetuloa hirsipuu peliin! Hirsipuussa pelaaja keksii sanan, ja muut pelaajat yrittävät arvata sen! Jos pelaaja arvaa väärin 6 kertaa, hän häviää!")
    sana = sana.lower()
    sana1 = sana
    sana_lista = list(sana)
    arvattu_lista = ["-"] * len(sana)
    
    vääriä = []
    yritykset = 6
    while True:
        await interaction.followup.send(f"Sana:   {'  '.join(arvattu_lista)}  \n\nYrityksiä jäljellä: {yritykset}\n Sanan pituus: {len(sana)}\nVäärät kirjaimet: " + " ".join(vääriä))
        response = await client.wait_for("message")
        if response.author == interaction.user:
            await interaction.followup.send(f"Hei {response.author.mention}! Et voi arvailla omaa hirsipuutasi!")
            continue

        else:
            
            if response.content.lower() in sana_lista:
                for i in range(len(sana)):
                    if sana_lista[i] == response.content.lower():
                        arvattu_lista[i] = response.content.lower()
                if "-" not in arvattu_lista:
                    await interaction.followup.send(f"Voitit!🎉 Sana oli: {sana}")
                    break

            elif response.content.lower() == sana1:
                await interaction.followup.send(f"Voitit!🎉 Sana oli: {sana}")
                break

            else:
                yritykset -= 1
                await interaction.followup.send(f"Väärin!❌ Yrityksiä jäljellä: {yritykset}")
                vääriä.append(response.content.lower())
                vääriä.sort()
                if yritykset == 0:
                    await interaction.followup.send(f"Hävisit!💔 Sana oli: {sana}")
                    break

@client.tree.command(name="wordle", description="Wordle peli", guild=GUILD_ID)
async def wordle(interaction: discord.Interaction):
    await interaction.response.send_message("Tervetuloa Wordle peliin! \nSäännöt: \n1. Arvaa sana 6 yrityksellä \n2. Sana on 5 kirjainta pitkä \n3. Jos kirjain on oikein ja oikeassa paikassa, se on vihreä \n4. Jos kirjain on oikein, mutta väärässä paikassa, se on keltainen \n5. Jos kirjain ei ole oikein, se on punainen")
    with open("words.txt", "r") as f:
        words = f.readlines()
        sana = words[randint(0, len(words)-1)]
        sana1 = sana.strip()
        sanalista = list(sana1)
        
    väärät = []
    yritykset = 6  
    while True:
        await interaction.followup.send(f"Arvaa sana! \nYrityksiä jäljellä: {yritykset}\nVäärät kirjaimet: " + " ".join(väärät))
        
        response = await client.wait_for("message")
        if response.author.bot == True:
            continue
        if response.author != interaction.user and response.author.bot == False:
            await interaction.followup.send(f"Et voi osallistua {response.author.mention}! Tämä on käyttäjän {interaction.user.mention} peli!")
            continue
        
        if len(response.content) != 5:
            await interaction.followup.send("Arvauksesi pitää olla 5 kirjainta pitkä!")
            continue
        wordlist = list(response.content.lower())
        
        emojilista = []
        
        for i in range(len(sanalista)):
            if wordlist[i] == sanalista[i]:
                emojilista.append(f":green_square:")
                
            elif wordlist[i] in sanalista:
                emojilista.append(f":yellow_square:")
                
            else:
                emojilista.append(f":red_square:")
                if wordlist[i] not in väärät:
                    väärät.append(wordlist[i])
                    väärät.sort()


        await interaction.followup.send(f"{' '.join(emojilista)}")
        yritykset -= 1
        if wordlist == sanalista:
            await interaction.followup.send(f"Voitit!🎉 Sana oli: {sana1}")
            break
        elif yritykset == 0:
            await interaction.followup.send(f"Hävisit!💔 Sana oli: {sana1}")
            break

@client.tree.command(name="slots", description="Hedelmäpeli. Kirjoita pyöräytysten määrä komennon perään! Max. 10", guild=GUILD_ID)
async def slots(interaction: discord.Interaction, amount: int):
    await interaction.response.send_message("Tervetuloa hedelmäpeliin! \nVoitat jos saat 3 samaa hedelmää! \nHedelmät: 🍒 🍋 🍊 🍉 🍇")
    await asyncio.sleep(2)
    hedelmät = ["🍒", "🍋", "🍊", "🍉", "🍇"]
    jatkuuko = amount
    voitot = 0
    häviöt = 0
    while 11 > jatkuuko > 0:
        rullat = [hedelmät[randint(0, 4)], hedelmät[randint(0, 4)], hedelmät[randint(0, 4)]]
        await interaction.followup.send(f"{' '.join(rullat)}")
        
        if rullat[0] == rullat[1] == rullat[2]:
            
            await interaction.followup.send("Voitit!🎉")
            await asyncio.sleep(2)
            jatkuuko -= 1
            voitot += 1

        else:
            
            await interaction.followup.send("Hävisit!💔")
            await asyncio.sleep(2)
            jatkuuko -= 1
            häviöt += 1

        if jatkuuko == 0:
            voittoprosentti = voitot/(voitot+häviöt)*100
            await interaction.followup.send(f"Voittoja: {voitot} \nHäviöitä: {häviöt} \nVoittoprosentti: {voittoprosentti:.2f}%")

        while jatkuuko == 0:
            
            await interaction.followup.send("Pyöräytä uudestaan kirjoittamalla 1! Poistu pelistä kirjoittamalla mitä tahansa muuta! \nVoit myös asettaa halutun määrän automaattipyörätyksiä kirjoittamalla haluamasi määrän! (Max. 10)")
        
            response = await client.wait_for("message")
            if response.author != interaction.user and response.author.bot == False:
                await interaction.followup.send(f"Et voi osallistua {response.author.mention}! Tämä on käyttäjän {interaction.user.mention} peli!")
                continue

            if response.author.bot == True:
                continue
                
            else:
                jatkuuko = int(response.content)




@client.tree.command(name="randomlol", description="Arvotaan sinulle random League of Legends championi!", guild=GUILD_ID)
async def randomlol(interaction: discord.Interaction):
    with open("lolchamp.txt", "r") as f:
        champ = f.readlines()
        champ1 = champ[randint(0, len(champ)-1)]
        champ2 = champ1.strip()
    await interaction.response.send_message(f"Random championisi on  ➡️  {champ2}!")

        
@client.tree.command(name="randomadc", description="Arvotaan sinulle random League of Legends ADC championi!", guild=GUILD_ID)
async def randomadc(interaction: discord.Interaction):
    with open("adc.txt", "r") as f:
        adc = f.readlines()
        adc1 = adc[randint(0, len(adc)-1)]
        adc2 = adc1.strip()
    await interaction.response.send_message(f"Random ADC championisi on  ➡️  {adc2}!")


@client.tree.command(name="randomquote", description="Arvotaan sinulle viisas aforismi!", guild=GUILD_ID)
async def randomquote(interaction: discord.Interaction):
     await interaction.response.send_message(quotet[randint(0, len(quotet)-1)])

@client.tree.command(name="quote", description="Näytä päivän sitaatti", guild=GUILD_ID)
async def quote(interaction: discord.Interaction):
    today_quote = get_daily_quote()
    await interaction.response.send_message(f"📢 Quote of the Day:\n{today_quote}")

@client.tree.command(name='roast', description='Roastaan mainitsemasi henkilön!', guild=GUILD_ID)
async def vitsi(interaction: discord.Interaction, kuka: str):
    with open("roastit.txt", "r") as f:
        roast = f.readlines()
        r1 = roast[randint(0,len(roast)-1)]
        await interaction.response.send_message(f"Hei {kuka}! {r1}")


@client.tree.command(name='krypto', description='Ratkaise kryptattu lause!', guild=GUILD_ID)
async def krypto(interaction: discord.Interaction):
    with open("Sanakrypto_lauseet.txt", "r") as f:
        kryptot = f.readlines()
        k1 = kryptot[randint(0,len(kryptot)-1)]
        kryptattu, avain = kryptaa_lause(k1)


    await interaction.response.send_message(f"Tervetuloa krypto-sanapeliin {interaction.user.mention}!\n Kryptattu lause on: {kryptattu} \n Arvaa kirjain kirjoittamalla ensin kirjain ja sitten numero! esim. a 1 \n Jos haluat vihjeen, kirjoita vihje. Vihje paljastaa satunnaisen kirjaimen!")

    while True:
        response = await client.wait_for("message")
        if response.author == interaction.user:
            if response.content.lower() == "vihje":
                vihje = random.choice(list(avain.keys()))
                await interaction.followup.send(f"Vihje: {vihje} = {avain[vihje]}")
                continue
            else:
                try:
                    kirjain, numero = response.content.split()
                    numero = int(numero)
                    if avain[kirjain] == int(numero):
                        await interaction.followup.send(f"Oikein! ✅")
                        await interaction.followup.send(f"Kirjain: {kirjain} = {numero}")
                        kryptattu = kryptattu.replace(str(numero), kirjain)
                        if "-" not in kryptattu:
                            await interaction.followup.send(f"Voitit!🎉 Kryptattu lause oli: {k1}")
                            break
                        else:
                            await interaction.followup.send(f"Kryptattu lause on nyt: {kryptattu}")
                            continue
                        
                    else:
                        await interaction.followup.send("Väärin! Yritä uudelleen!")
                        continue
                except ValueError:
                    await interaction.followup.send("Virheellinen syöte! Kirjoita ensin kirjain ja sitten numero! esim. a 1")
        elif response.author.bot == True:
            continue
        else:
            await interaction.followup.send(f"Et voi osallistua {response.author.mention}! Tämä on käyttäjän {interaction.user.mention} peli!")
            continue




# Asynkroninen pääfunktio
async def main():
    print("Käynnistetään botti...")
    await client.start(os.getenv('DISCORD_TOKEN'))

# Flask + botti yhdessä
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())  # Ajetaan pääfunktio asynkronisesti


