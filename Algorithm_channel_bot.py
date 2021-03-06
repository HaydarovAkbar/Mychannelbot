from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup,InlineKeyboardButton

jamoaB = InlineKeyboardMarkup([
    [InlineKeyboardButton("π’ Python", callback_data="akbar")],
    [InlineKeyboardButton("π΅ Javascript", callback_data="jamshid")],
    [InlineKeyboardButton("π‘ Java", callback_data="java")]
    ])
ID = 7 # admins ID
Id = 9 # admins ID

startBatton = ReplyKeyboardMarkup([
    ["π€ Masala jo'natish βοΈ"],
    ["π¬ Yechimini jo'natish π", "π¬ Fikr qoldirish π"],
    ["π¨βπ« TeamFriendly jamoasi π¨βπ»"]
], resize_keyboard=True)

batton_start = ReplyKeyboardMarkup([
    ["π Orqaga qaytish π"]
],resize_keyboard=True)

def call_back(update,context):
    query = update.callback_query
    if query.data == "akbar":
        query.message.delete()
        context.bot.send_message(chat_id = update.effective_chat.id, text = "π Python bo'yicha dasturchi:\n \n"
                                                                            "π¨βπ» Haydarov Akbar \n \nπΊπΏTelegram @Akbar_TUIT")
    elif query.data == "jamshid":
        query.message.delete()
        context.bot.send_message(chat_id = update.effective_chat.id, text = "π¨βπ»Javascript bo'yicha dasturchi:\n"
                                                                            "\nπ¨βπ» Js developer \n"
                                                                            "\nπΊπΏTelegram @@TeamFriendly")
    else:
        query.message.delete()
        context.bot.send_message(chat_id = update.effective_chat.id, text = "π¨βπ»Java bo'yicha dasturchi: \n"
                                                                            "\nπ¨βπ» Temurmalik developer\n \n @TUITsecurity")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=""
                                  "π€ Bot orqali siz π\n \nπ§<b>Masala</b> yuborishingiz β\n \n π<b>Masala yechimi</b>ni yuborishgiz β\n \n"
                                  "π¬<b>Kanal haqida fikr bildirishingiz</b>β\n "
                                  " \nπ¨βπ»<b>dasturchilar</b> bilan bog'lanishingiz mumkin β",
                             parse_mode="HTML",
                             reply_markup=startBatton)

def masala(update,context):
    user = update.message.from_user.first_name
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"<b>{user}</b> Masalalarni jo'natish tartibi:\n"
                                                                        f"\n1οΈβ£<b>Rasm</b> ko'rinishida jo'natish imkoniyati bor β\n"
                                                                        f"\n2οΈβ£<b>Dokument</b> ko'rinishida(Word,JPG...)jo'natish imkoniyati bor β\n"
                                                                        f"\n3οΈβ£<b>Audio</b> ko'rinishida qoldirishingiz mumkin β\n"
                                                                        f"\n4οΈβ£Masalalarni <b>yozib</b> qoldirishingiz ham mumkin β\n"
                                                                        f"\n     β <b>Iltimos etiiborli bo'ling masala shartiga</b> β\n"
                                                                        f"\n#οΈβ£<b>text</b> ko'rinishida yuborish tartibi π kalit so'z(#YUBORISH) masala sharti β\n"
                                                                        f"\nπββοΈ<b>Masalan</b> π #YUBORISH shu yerga masala sharti! β",
                             parse_mode="HTML",
                             reply_markup = batton_start)
def startGAqaytish(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "π Quyidagilardan birini tanlang β",reply_markup = startBatton)

def yuborish(update,context):
    masala = update.message.text
    user = update.message.from_user
    context.bot.send_message(chat_id = ID, text = masala +f"\n \nπββοΈ Masala {user.first_name} tomonidan yo'llandi\nπΊπΏTelegram @{user.username}")
    context.bot.send_message(chat_id = Id, text = masala +f"\n \nπββοΈ Masala {user.first_name} tomonidan yo'llandi\nπΊπΏTelegram @{user.username}")
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"β Masala muvafaqiyatli jo'natildi βββ\n \n<b>TeamFriendly</b> "
                                                                        f"jamoasi nomidan tashakkur sizga π <b>{user.first_name}</b>\n"
                                                                        f"\nπ£ <b>Yechimini tez orada kanalga joylashtiramiz!</b> π",
                             parse_mode = "HTML",
                             reply_markup = batton_start)
def yechim(update,context):
    user = update.message.from_user.first_name
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"<b>{user}</b> Masalalani yechimini jo'natish tartibi:\n"
                                                                        f"\n1οΈβ£<b>Rasm</b> ko'rinishida jo'natish imkoniyati bor β\n"
                                                                        f"\n2οΈβ£<b>Dokument</b> ko'rinishida(Word,JPG...)jo'natish imkoniyati bor β\n"
                                                                        f"\n3οΈβ£<b>Audio</b> ko'rinishida qoldirishingiz mumkin β\n"
                                                                        f"\n4οΈβ£Masalalarni yechimini <b>yozib</b> qoldirishingiz ham mumkin β\n"
                                                                        f"\n     β <b>Iltimos etiiborli bo'ling masalani yechimiga </b> β\n"
                                                                        f"\n#οΈβ£<b>Yechimni yozib qoldirish</b> tartibi π kalit so'z(#YECHIM) masala yechimi β\n"
                                                                        f"\nπββοΈ<b>Masalan</b> π #YECHIM shu yerga masalani yechimi bo'lishi mumkin! β",
                             parse_mode="HTML",
                             reply_markup = batton_start)
def masala_yechimi(update,context):
        masala = update.message.text
        user = update.message.from_user
        context.bot.send_message(chat_id = ID, text = masala +f"\n \nπββοΈ Masala yechimi {user.first_name} tomonidan yo'llandi\nπΊπΏTelegram @{user.username}")
        context.bot.send_message(chat_id = Id, text = masala +f"\n \nπββοΈ Masala yechimi {user.first_name} tomonidan yo'llandi\nπΊπΏTelegram @{user.username}")
        context.bot.send_message(chat_id = update.effective_chat.id, text = f"β Masalani yechimi muvafaqiyatli jo'natildi βββ\n \n<b>TeamFriendly</b> "
                                                                            f"jamoasi nomidan tashakkur sizga π <b>{user.first_name}</b>\n"
                                                                            f"\nπ£ <b>Yechimini tez orada ko'rib chiqib kanalga joylashtiramiz!</b> π",
                                 parse_mode = "HTML",
                                 reply_markup = batton_start)
def rahmat(update,context):
    user = update.message.from_user
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"\nπ¨βπ» <b>TeamFriendly</b> "
                                                                        f"jamoasi nomidan tashakkur sizga π π€ <b>{user.first_name}</b>\n",
                             parse_mode = "HTML",
                             reply_markup = batton_start)
def fikr(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"π¨βπ» <b>TeamFriendly</b> jamoasiga fikr qoldirish π§π­!\n"
                                                                        f"\nπ Fikr qoldirish tartibi: kalit so'z(#FIKR) fikrlar...β\n"
                                                                        f"\nπ Masalan #FIKR kanal manga juda yoqdi!!!β π¨βπ» π",
                             parse_mode = "HTML",
                             reply_markup = batton_start)
def fikr_tashakkur(update,context):
    user = update.message.from_user
    fikr = update.message.text
    context.bot.send_message(chat_id = ID, text = fikr + f"\n \nπββοΈ Fikr {user.first_name} tomonidan yo'llandi\nπΊπΏTelegram @{user.username}",)
    context.bot.send_message(chat_id = Id, text = fikr + f"\n \nπββοΈ Fikr {user.first_name} tomonidan yo'llandi\nπΊπΏTelegram @{user.username}",)
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"\nπ¨βπ» <b>TeamFriendly</b> "
                                                                        f"jamoasi nomidan <b>Fikringiz uchun tashakkur</b> sizga π π€ <b>{user.first_name}</b>\n",
                             parse_mode = "HTML",
                             reply_markup = batton_start)
def jamoa(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "^_^",
                             reply_markup = batton_start)
    context.bot.send_message(chat_id = update.effective_chat.id, text = "π¨βπ» <b>TeamFriendly</b> jamosi π¨βπ» \n \nπ Quyidagilardan birini tanlang π‘π’π΅",
                             parse_mode = "HTML",
                             reply_markup = jamoaB)

def main(update, context):
    text = update.message.text
    if text == "π€ Masala jo'natish βοΈ":
        return masala(update,context)
    if text == "π Orqaga qaytish π":
        return startGAqaytish(update,context)
    if "#YUBORISH" in text:
        return yuborish(update,context)
    if text == "π¬ Yechimini jo'natish π":
        return yechim(update,context)
    if "#YECHIM" in text:
        return masala_yechimi(update,context)
    if text == "π¬ Fikr qoldirish π":
        return fikr(update,context)
    if "#FIKR" in text:
        return fikr_tashakkur(update,context)
    if text == "π¨βπ« TeamFriendly jamoasi π¨βπ»":
        return jamoa(update,context)

def document(update, context):
    user = update.message.from_user

    context.bot.send_document(chat_id=ID, document=update.message.document)

    context.bot.send_message(chat_id=ID,
                             text=f"π¬ Dokument πββοΈ <b>{user.first_name}</b> dan πππ @{user.username} ",
                             parse_mode="HTML")
    context.bot.send_document(chat_id=Id, document=update.message.document)

    context.bot.send_message(chat_id=Id,
                             text=f"π¬ Dokument πββοΈ <b>{user.first_name}</b> dan πππ @{user.username} ",
                             parse_mode="HTML")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"β <b>{user.first_name}</b> Dokument muvofaqiyatli jo'natildi β",
                             parse_mode="HTML")
    return rahmat(update,context)


def photo(update, context):
    user = update.message.from_user

    context.bot.send_photo(chat_id=ID, photo=update.message.photo[0])

    context.bot.send_message(chat_id=ID, text=f"π Rasm πββοΈ <b>{user.first_name}</b> dan πππ @{user.username}",
                             parse_mode="HTML")
    context.bot.send_photo(chat_id=Id, photo=update.message.photo[0])

    context.bot.send_message(chat_id=Id, text=f"π Rasm πββοΈ <b>{user.first_name}</b> dan πππ @{user.username}",
                             parse_mode="HTML")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"β <b>{user.first_name}</b> Rasm muvofaqiyatli jo'natildi β", parse_mode="HTML")
    return rahmat(update,context)


def voice(update, context):
    user = update.message.from_user

    context.bot.send_voice(chat_id=ID, voice=update.message.voice)

    context.bot.send_message(chat_id=ID,
                             text=f"π Ovozli xabar πββοΈ <b>{user.first_name}</b> dan πππ @{user.username}",
                             parse_mode="HTML")
    context.bot.send_voice(chat_id=Id, voice=update.message.voice)

    context.bot.send_message(chat_id=Id,
                             text=f"π Ovozli xabar πββοΈ <b>{user.first_name}</b> dan πππ @{user.username}",
                             parse_mode="HTML")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"β <b>{user.first_name}</b> Ovozli xabar muvofaqiyatli jo'natildi β",
                             parse_mode="HTML")
    return rahmat(update,context)