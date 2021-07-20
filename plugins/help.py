from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single (No playlist)\n\nJust Send Youtube Url Now..\n\n© @fileshomeofficial"
    await message.reply_text(helptxt)
