from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup,InlineKeyboardButton

jamoaB = InlineKeyboardMarkup([
    [InlineKeyboardButton("🟢 Python", callback_data="akbar")],
    [InlineKeyboardButton("🔵 Javascript", callback_data="jamshid")],
    [InlineKeyboardButton("🟡 Java", callback_data="java")]
    ])
ID = 7 # admins ID
Id = 9 # admins ID

startBatton = ReplyKeyboardMarkup([
    ["📤 Masala jo'natish ✉️"],
    ["📬 Yechimini jo'natish 🖌", "💬 Fikr qoldirish 📝"],
    ["👨‍🏫 TeamFriendly jamoasi 👨‍💻"]
], resize_keyboard=True)

batton_start = ReplyKeyboardMarkup([
    ["🔙 Orqaga qaytish 🔙"]
],resize_keyboard=True)

def call_back(update,context):
    query = update.callback_query
    if query.data == "akbar":
        query.message.delete()
        context.bot.send_message(chat_id = update.effective_chat.id, text = "🐍 Python bo'yicha dasturchi:\n \n"
                                                                            "👨‍💻 Haydarov Akbar \n \n🇺🇿Telegram @Akbar_TUIT")
    elif query.data == "jamshid":
        query.message.delete()
        context.bot.send_message(chat_id = update.effective_chat.id, text = "👨‍💻Javascript bo'yicha dasturchi:\n"
                                                                            "\n👨‍💻 Js developer \n"
                                                                            "\n🇺🇿Telegram @@TeamFriendly")
    else:
        query.message.delete()
        context.bot.send_message(chat_id = update.effective_chat.id, text = "👨‍💻Java bo'yicha dasturchi: \n"
                                                                            "\n👨‍💻 Temurmalik developer\n \n @TUITsecurity")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=""
                                  "🤖 Bot orqali siz 👇\n \n📧<b>Masala</b> yuborishingiz ✅\n \n 📝<b>Masala yechimi</b>ni yuborishgiz ✅\n \n"
                                  "💬<b>Kanal haqida fikr bildirishingiz</b>✅\n "
                                  " \n👨‍💻<b>dasturchilar</b> bilan bog'lanishingiz mumkin ✅",
                             parse_mode="HTML",
                             reply_markup=startBatton)

def masala(update,context):
    user = update.message.from_user.first_name
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"<b>{user}</b> Masalalarni jo'natish tartibi:\n"
                                                                        f"\n1️⃣<b>Rasm</b> ko'rinishida jo'natish imkoniyati bor ✅\n"
                                                                        f"\n2️⃣<b>Dokument</b> ko'rinishida(Word,JPG...)jo'natish imkoniyati bor ✅\n"
                                                                        f"\n3️⃣<b>Audio</b> ko'rinishida qoldirishingiz mumkin ✅\n"
                                                                        f"\n4️⃣Masalalarni <b>yozib</b> qoldirishingiz ham mumkin ✅\n"
                                                                        f"\n     ✅ <b>Iltimos etiiborli bo'ling masala shartiga</b> ✅\n"
                                                                        f"\n#️⃣<b>text</b> ko'rinishida yuborish tartibi 👉 kalit so'z(#YUBORISH) masala sharti ✅\n"
                                                                        f"\n💁‍♂️<b>Masalan</b> 👉 #YUBORISH shu yerga masala sharti! ✅",
                             parse_mode="HTML",
                             reply_markup = batton_start)
def startGAqaytish(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "👇 Quyidagilardan birini tanlang ✅",reply_markup = startBatton)

def yuborish(update,context):
    masala = update.message.text
    user = update.message.from_user
    context.bot.send_message(chat_id = ID, text = masala +f"\n \n💁‍♂️ Masala {user.first_name} tomonidan yo'llandi\n🇺🇿Telegram @{user.username}")
    context.bot.send_message(chat_id = Id, text = masala +f"\n \n💁‍♂️ Masala {user.first_name} tomonidan yo'llandi\n🇺🇿Telegram @{user.username}")
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"✅ Masala muvafaqiyatli jo'natildi ✅✅✅\n \n<b>TeamFriendly</b> "
                                                                        f"jamoasi nomidan tashakkur sizga 😊 <b>{user.first_name}</b>\n"
                                                                        f"\n📣 <b>Yechimini tez orada kanalga joylashtiramiz!</b> 🔊",
                             parse_mode = "HTML",
                             reply_markup = batton_start)
def yechim(update,context):
    user = update.message.from_user.first_name
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"<b>{user}</b> Masalalani yechimini jo'natish tartibi:\n"
                                                                        f"\n1️⃣<b>Rasm</b> ko'rinishida jo'natish imkoniyati bor ✅\n"
                                                                        f"\n2️⃣<b>Dokument</b> ko'rinishida(Word,JPG...)jo'natish imkoniyati bor ✅\n"
                                                                        f"\n3️⃣<b>Audio</b> ko'rinishida qoldirishingiz mumkin ✅\n"
                                                                        f"\n4️⃣Masalalarni yechimini <b>yozib</b> qoldirishingiz ham mumkin ✅\n"
                                                                        f"\n     ✅ <b>Iltimos etiiborli bo'ling masalani yechimiga </b> ✅\n"
                                                                        f"\n#️⃣<b>Yechimni yozib qoldirish</b> tartibi 👉 kalit so'z(#YECHIM) masala yechimi ✅\n"
                                                                        f"\n💁‍♂️<b>Masalan</b> 👉 #YECHIM shu yerga masalani yechimi bo'lishi mumkin! ✅",
                             parse_mode="HTML",
                             reply_markup = batton_start)
def masala_yechimi(update,context):
        masala = update.message.text
        user = update.message.from_user
        context.bot.send_message(chat_id = ID, text = masala +f"\n \n💁‍♂️ Masala yechimi {user.first_name} tomonidan yo'llandi\n🇺🇿Telegram @{user.username}")
        context.bot.send_message(chat_id = Id, text = masala +f"\n \n💁‍♂️ Masala yechimi {user.first_name} tomonidan yo'llandi\n🇺🇿Telegram @{user.username}")
        context.bot.send_message(chat_id = update.effective_chat.id, text = f"✅ Masalani yechimi muvafaqiyatli jo'natildi ✅✅✅\n \n<b>TeamFriendly</b> "
                                                                            f"jamoasi nomidan tashakkur sizga 😊 <b>{user.first_name}</b>\n"
                                                                            f"\n📣 <b>Yechimini tez orada ko'rib chiqib kanalga joylashtiramiz!</b> 🔊",
                                 parse_mode = "HTML",
                                 reply_markup = batton_start)
def rahmat(update,context):
    user = update.message.from_user
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"\n👨‍💻 <b>TeamFriendly</b> "
                                                                        f"jamoasi nomidan tashakkur sizga 😊 🤝 <b>{user.first_name}</b>\n",
                             parse_mode = "HTML",
                             reply_markup = batton_start)
def fikr(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"👨‍💻 <b>TeamFriendly</b> jamoasiga fikr qoldirish 🧐💭!\n"
                                                                        f"\n📝 Fikr qoldirish tartibi: kalit so'z(#FIKR) fikrlar...✅\n"
                                                                        f"\n👉 Masalan #FIKR kanal manga juda yoqdi!!!‍ 👨‍💻 👍",
                             parse_mode = "HTML",
                             reply_markup = batton_start)
def fikr_tashakkur(update,context):
    user = update.message.from_user
    fikr = update.message.text
    context.bot.send_message(chat_id = ID, text = fikr + f"\n \n💁‍♂️ Fikr {user.first_name} tomonidan yo'llandi\n🇺🇿Telegram @{user.username}",)
    context.bot.send_message(chat_id = Id, text = fikr + f"\n \n💁‍♂️ Fikr {user.first_name} tomonidan yo'llandi\n🇺🇿Telegram @{user.username}",)
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"\n👨‍💻 <b>TeamFriendly</b> "
                                                                        f"jamoasi nomidan <b>Fikringiz uchun tashakkur</b> sizga 😊 🤝 <b>{user.first_name}</b>\n",
                             parse_mode = "HTML",
                             reply_markup = batton_start)
def jamoa(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "^_^",
                             reply_markup = batton_start)
    context.bot.send_message(chat_id = update.effective_chat.id, text = "👨‍💻 <b>TeamFriendly</b> jamosi 👨‍💻 \n \n👇 Quyidagilardan birini tanlang 🟡🟢🔵",
                             parse_mode = "HTML",
                             reply_markup = jamoaB)

def main(update, context):
    text = update.message.text
    if text == "📤 Masala jo'natish ✉️":
        return masala(update,context)
    if text == "🔙 Orqaga qaytish 🔙":
        return startGAqaytish(update,context)
    if "#YUBORISH" in text:
        return yuborish(update,context)
    if text == "📬 Yechimini jo'natish 🖌":
        return yechim(update,context)
    if "#YECHIM" in text:
        return masala_yechimi(update,context)
    if text == "💬 Fikr qoldirish 📝":
        return fikr(update,context)
    if "#FIKR" in text:
        return fikr_tashakkur(update,context)
    if text == "👨‍🏫 TeamFriendly jamoasi 👨‍💻":
        return jamoa(update,context)

def document(update, context):
    user = update.message.from_user

    context.bot.send_document(chat_id=ID, document=update.message.document)

    context.bot.send_message(chat_id=ID,
                             text=f"📬 Dokument 💁‍♂️ <b>{user.first_name}</b> dan 👉👉👉 @{user.username} ",
                             parse_mode="HTML")
    context.bot.send_document(chat_id=Id, document=update.message.document)

    context.bot.send_message(chat_id=Id,
                             text=f"📬 Dokument 💁‍♂️ <b>{user.first_name}</b> dan 👉👉👉 @{user.username} ",
                             parse_mode="HTML")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"✅ <b>{user.first_name}</b> Dokument muvofaqiyatli jo'natildi ✅",
                             parse_mode="HTML")
    return rahmat(update,context)


def photo(update, context):
    user = update.message.from_user

    context.bot.send_photo(chat_id=ID, photo=update.message.photo[0])

    context.bot.send_message(chat_id=ID, text=f"🌆 Rasm 💁‍♂️ <b>{user.first_name}</b> dan 👉👉👉 @{user.username}",
                             parse_mode="HTML")
    context.bot.send_photo(chat_id=Id, photo=update.message.photo[0])

    context.bot.send_message(chat_id=Id, text=f"🌆 Rasm 💁‍♂️ <b>{user.first_name}</b> dan 👉👉👉 @{user.username}",
                             parse_mode="HTML")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"✅ <b>{user.first_name}</b> Rasm muvofaqiyatli jo'natildi ✅", parse_mode="HTML")
    return rahmat(update,context)


def voice(update, context):
    user = update.message.from_user

    context.bot.send_voice(chat_id=ID, voice=update.message.voice)

    context.bot.send_message(chat_id=ID,
                             text=f"🌆 Ovozli xabar 💁‍♂️ <b>{user.first_name}</b> dan 👉👉👉 @{user.username}",
                             parse_mode="HTML")
    context.bot.send_voice(chat_id=Id, voice=update.message.voice)

    context.bot.send_message(chat_id=Id,
                             text=f"🌆 Ovozli xabar 💁‍♂️ <b>{user.first_name}</b> dan 👉👉👉 @{user.username}",
                             parse_mode="HTML")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"✅ <b>{user.first_name}</b> Ovozli xabar muvofaqiyatli jo'natildi ✅",
                             parse_mode="HTML")
    return rahmat(update,context)