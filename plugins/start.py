from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/fileshomeofficial")],
        [InlineKeyboardButton(
            "Source Code 😊", url="https://t.me/kurachkanjiedukkatte")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n\nI Am A Youtube Downloader Bot developed By @fileshomeofficial \n\n❤Join Our Channel For More...\n\nClick /help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
