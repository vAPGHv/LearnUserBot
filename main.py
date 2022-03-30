# -------=imports=-------
from pyrogram import Client, filters # бот
from time import sleep

app = Client("my_account")

@app.on_message(filters.command("hack", prefixes="/") & filters.me) # комманда
def hack(_, msg):
    name = msg.text.split("/hack ", maxsplit=1)[1] # достаём слово после /hack
    input_sym = 0

    while (input_sym < 100):
        try:
            msg.edit(f"Взлом объекта '{name}' в процессе... {input_sym}%")
            input_sym += 1
            sleep(0.2)

        except:
            pass

    msg.edit(f"Взлом объекта '{name}' в процессе... {input_sym}% \nОбъект '{name}' взломан!")

@app.on_message(filters.command("inp", prefixes="/") & filters.me) # комманда
def redact(_, msg):
    realtext = msg.text.split("/inp ", maxsplit=1)[1] # достаём слово после /input

    text = list(realtext)

    num = 0

    text2 = ""

    while len(text) - 1 != num:
        try:
            text2 = text2 + text[num]
            msg.edit(f"{text2}_")
            num += 1
            sleep(0.4)
        except:
            pass

    msg.edit(realtext)

app.run()
