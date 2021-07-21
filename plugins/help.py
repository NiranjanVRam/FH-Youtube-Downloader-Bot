from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Singles(No playlist)\n\nNow send the youtube url of video to be downloaded...\n\n© @fileshomeofficial"
    await message.reply_text(helptxt)
