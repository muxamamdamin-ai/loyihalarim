import telebot
import sqlite3
from telebot import types
import os
from flask import Flask
import threading
TOKEN = "8479798538:AAGM851VKTQFdwEtl1qt9L-sTOsqnlhYFWE"
bot = telebot.TeleBot(TOKEN)
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users 
                      (user_id INTEGER PRIMARY KEY, username TEXT, status TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS iso_images 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, reliability TEXT, video_url TEXT, download_link TEXT)''')
    conn.commit()
    conn.close()
def populate_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM iso_images")
    if cursor.fetchone()[0] == 0:
        iso_list = [
    ('Ubuntu Desktop', 'Juda yuqori', 'https://www.youtube.com/results?search_query=how+to+install+ubuntu+desktop', 'https://ubuntu.com/download/desktop'),
    ('Linux Mint Cinnamon', 'Juda yuqori', 'https://www.youtube.com/results?search_query=how+to+install+linux+mint', 'https://linuxmint.com/download.php'),
    ('Zorin OS', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+zorin+os', 'https://zorin.com/os/download/'),
    ('Pop!_OS', 'Yuqori (Geymerlar)', 'https://www.youtube.com/results?search_query=how+to+install+pop+os', 'https://pop.system76.com/'),
    ('Fedora Workstation', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+fedora+workstation', 'https://fedoraproject.org/workstation/download/'),
    ('Manjaro Linux', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+manjaro+linux', 'https://manjaro.org/download/'),
    ('Elementary OS', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+elementary+os', 'https://elementary.io/'),
    ('Deepin OS', 'O’rtacha (Dizayn)', 'https://www.youtube.com/results?search_query=how+to+install+deepin+os', 'https://www.deepin.org/en/download/'),
    ('MX Linux', 'Juda yuqori', 'https://www.youtube.com/results?search_query=how+to+install+mx+linux', 'https://mxlinux.org/download-links/'),
    ('EndeavourOS', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+endeavouros', 'https://endeavouros.com/latest-release/'),
    ('Garuda Linux', 'Yuqori (Geymerlar)', 'https://www.youtube.com/results?search_query=how+to+install+garuda+linux', 'https://garudalinux.org/downloads.html'),
    ('Nobara Linux', 'Yuqori (Geymerlar)', 'https://www.youtube.com/results?search_query=how+to+install+nobara+linux', 'https://nobaraproject.org/download-nobara/'),

    # --- KUCHSIZ KOMPYUTERLAR UCHUN (LIGHTWEIGHT) ---
    ('Lubuntu', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+lubuntu', 'https://lubuntu.me/downloads/'),
    ('Xubuntu', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+xubuntu', 'https://xubuntu.org/download/'),
    ('Ubuntu MATE', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+ubuntu+mate', 'https://ubuntu-mate.org/download/'),
    ('Linux Lite', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+linux+lite', 'https://www.linuxliteos.com/download.php'),
    ('Peppermint OS', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+peppermint+os', 'https://peppermintos.com/'),
    ('Bodhi Linux', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+bodhi+linux', 'https://www.bodhilinux.com/download/'),
    ('antiX Linux', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+antix+linux', 'https://antixlinux.com/download/'),
    ('Puppy Linux', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+puppy+linux', 'https://puppylinux.com/index.html#download'),
    ('Tiny Core Linux', 'Past', 'https://www.youtube.com/results?search_query=how+to+install+tiny+core+linux', 'http://tinycorelinux.net/downloads.html'),
    ('Q4OS', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+q4os', 'https://q4os.org/downloads1.html'),

    # --- KIBERXAVFSIZLIK VA PENTESTING ---
    ('Kali Linux', 'Juda yuqori', 'https://www.youtube.com/results?search_query=how+to+install+kali+linux', 'https://www.kali.org/get-kali/'),
    ('Parrot Security', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+parrot+os', 'https://parrotsec.org/download/'),
    ('BlackArch Linux', 'Past (Qiyin)', 'https://www.youtube.com/results?search_query=how+to+install+blackarch+linux', 'https://blackarch.org/downloads.html'),
    ('Tails OS', 'Yuqori (Maxfiylik)', 'https://www.youtube.com/results?search_query=how+to+install+tails+os', 'https://tails.net/install/index.en.html'),
    ('Whonix', 'Yuqori (Anonimlik)', 'https://www.youtube.com/results?search_query=how+to+install+whonix', 'https://www.whonix.org/wiki/Download'),
    ('Wifislax', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+wifislax', 'https://www.wifislax.com/'),
    ('Qubes OS', 'O’rtacha (Maxfiy)', 'https://www.youtube.com/results?search_query=how+to+install+qubes+os', 'https://www.qubes-os.org/downloads/'),

    # --- SERVER VA ENTERPRISE ---
    ('Debian', 'Juda yuqori', 'https://www.youtube.com/results?search_query=how+to+install+debian', 'https://www.debian.org/download'),
    ('Ubuntu Server', 'Juda yuqori', 'https://www.youtube.com/results?search_query=how+to+install+ubuntu+server', 'https://ubuntu.com/download/server'),
    ('AlmaLinux', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+almalinux', 'https://almalinux.org/get-almalinux/'),
    ('Rocky Linux', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+rocky+linux', 'https://rockylinux.org/download'),
    ('CentOS Stream', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+centos+stream', 'https://www.centos.org/centos-stream/'),
    ('openSUSE Leap', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+opensuse+leap', 'https://get.opensuse.org/leap/'),
    ('TrueNAS CORE', 'Yuqori (NAS)', 'https://www.youtube.com/results?search_query=how+to+install+truenas+core', 'https://www.truenas.com/download-truenas-core/'),
    ('Proxmox VE', 'Yuqori (Virtualizatsiya)', 'https://www.youtube.com/results?search_query=how+to+install+proxmox+ve', 'https://www.proxmox.com/en/downloads'),

    # --- ADVANCED / PROFESSONAL ---
    ('Arch Linux', 'Qiyin', 'https://www.youtube.com/results?search_query=how+to+install+arch+linux', 'https://archlinux.org/download/'),
    ('Gentoo Linux', 'Juda qiyin', 'https://www.youtube.com/results?search_query=how+to+install+gentoo+linux', 'https://www.gentoo.org/downloads/'),
    ('Slackware', 'Juda qiyin', 'https://www.youtube.com/results?search_query=how+to+install+slackware', 'http://www.slackware.com/getslack/'),
    ('Void Linux', 'Qiyin', 'https://www.youtube.com/results?search_query=how+to+install+void+linux', 'https://voidlinux.org/download/'),
    ('NixOS', 'Qiyin', 'https://www.youtube.com/results?search_query=how+to+install+nixos', 'https://nixos.org/download/'),
    ('Alpine Linux', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+alpine+linux', 'https://alpinelinux.org/downloads/'),
    ('Clear Linux', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+clear+linux', 'https://clearlinux.org/downloads.html'),

    # --- BSD VA UNIX ---
    ('FreeBSD', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+freebsd', 'https://www.freebsd.org/where/'),
    ('OpenBSD', 'Qiyin', 'https://www.youtube.com/results?search_query=how+to+install+openbsd', 'https://www.openbsd.org/faq/faq4.html'),
    ('NetBSD', 'Qiyin', 'https://www.youtube.com/results?search_query=how+to+install+netbsd', 'https://www.netbsd.org/mirrors/'),
    ('GhostBSD', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+ghostbsd', 'https://ghostbsd.org/download'),
    ('DragonFly BSD', 'Qiyin', 'https://www.youtube.com/results?search_query=how+to+install+dragonfly+bsd', 'https://www.dragonflybsd.org/download/'),

    # --- NOODATIY, RETRO VA BOSHQALAR ---
    ('ChromeOS Flex', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+chrome+os+flex', 'https://chromeenterprise.google/os/chromeosflex/'),
    ('Android-x86', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+android+x86+on+pc', 'https://www.android-x86.org/download.html'),
    ('Bliss OS', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+bliss+os', 'https://blissos.org/'),
    ('PrimeOS', 'O’rtacha (Android gaming)', 'https://www.youtube.com/results?search_query=how+to+install+primeos', 'https://primeos.in/download/'),
    ('ReactOS', 'Past (Windows klon)', 'https://www.youtube.com/results?search_query=how+to+install+reactos', 'https://reactos.org/download/'),
    ('Haiku OS', 'Past (BeOS davomchisi)', 'https://www.youtube.com/results?search_query=how+to+install+haiku+os', 'https://www.haiku-os.org/get-haiku/'),
    ('KDE Neon', 'Yuqori', 'https://www.youtube.com/results?search_query=how+to+install+kde+neon', 'https://neon.kde.org/download'),
    ('Solus', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+solus+linux', 'https://getsol.us/download/'),
    ('Mageia', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+mageia', 'https://www.mageia.org/en/downloads/'),
    ('PCLinuxOS', 'O’rtacha', 'https://www.youtube.com/results?search_query=how+to+install+pclinuxos', 'https://www.pclinuxos.com/?page_id=10'),
    ('Slax', 'Yuqori (USB uchun)', 'https://www.youtube.com/results?search_query=how+to+install+slax+linux', 'https://www.slax.org/'),
    ('Porteus', 'Yuqori (USB uchun)', 'https://www.youtube.com/results?search_query=how+to+install+porteus+linux', 'http://www.porteus.org/'),
]
        cursor.executemany('''INSERT INTO iso_images (name, reliability, video_url, download_link) 
                              VALUES (?, ?, ?, ?)''', iso_list)
        conn.commit()
    conn.close()

@bot.message_handler(commands=['start', 'register'])
def register_hendler(message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users (user_id, username, status) VALUES (?, ?, ?)", 
                       (message.from_user.id, message.from_user.username, 'registered'))
        conn.commit()
    except Exception as e:
        print(f"Xatolik: {e}")
    conn.close()
    
    bot.reply_to(message, "Salom! Siz muvaffaqiyatli ro'yxatdan o'tdingiz.\n\nBuyruqlar:\n/view - ISO ro'yxatini ko'rish\n/select - Video qo'llanma\n/download - Yuklab olish\n/search - Qidirish uchun")
@bot.message_handler(commands=['view'])
def view_images(message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, reliability FROM iso_images")
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        bot.send_message(message.chat.id)
        return
    response = "<b>Mavjud ISO tasvirlar:</b>\n\n"
    for row in rows:
        line = f"<b>ID:</b> {row[0]}\n <b>Nomi:</b> {row[1]}\n <b>Ishonchlilik:</b> {row[2]}\n" + "—"*15 + "\n"
        if len(response) + len(line) > 4000:
            bot.send_message(message.chat.id, response, parse_mode="HTML")
            response = ""
        response += line
    
    if response:
        bot.send_message(message.chat.id, response, parse_mode="HTML")
@bot.message_handler(commands=['select'])
def select_image(message):
    msg = bot.send_message(message.chat.id, "O'rnatish videosini ko'rish uchun ISO ID raqamini kiriting:")
    bot.register_next_step_handler(msg, process_video_step)
def process_video_step(message):
    iso_id = message.text
    if not iso_id.isdigit():
        bot.send_message(message.chat.id, "Iltimos, faqat raqam kiriting!")
        return

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, video_url FROM iso_images WHERE id = ?", (iso_id,))
    res = cursor.fetchone()
    conn.close()

    if res:
        bot.send_message(message.chat.id, f" <b>{res[0]}</b> o'rnatish qo'llanmasi:\n{res[1]}", parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, "Bunday ID dagi ISO topilmadi.")
@bot.message_handler(commands=['download'])
def ask_download_id(message):
    msg = bot.send_message(message.chat.id, "Yuklab olish uchun ISO ID raqamini yuboring:")
    bot.register_next_step_handler(msg, send_download_link)

def send_download_link(message):
    iso_id = message.text
    if not iso_id.isdigit():
        bot.send_message(message.chat.id, "Iltimos, faqat raqam kiriting!")
        return

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, download_link FROM iso_images WHERE id = ?", (iso_id,))
    res = cursor.fetchone()
    conn.close()
    
    if res:
        iso_name, iso_url = res[0], res[1]
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Yuklab olish ⬇️", url=iso_url)
        markup.add(btn)
        
        bot.send_message(message.chat.id, f"💿 *{iso_name}* yuklab olishga tayyor!", reply_markup=markup, parse_mode="Markdown")
        ask_user_os(message, iso_name)
    else:
        bot.send_message(message.chat.id, "Kechirasiz, bunday ID topilmadi.")

def ask_user_os(message, iso_name):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add("Windows", "Linux", "MacOS")
    msg = bot.send_message(message.chat.id, 
                           "USB fleshka tayyorlash bo'yicha maslahat berishim uchun, hozir qaysi OS dan foydalanyapsiz?", 
                           reply_markup=markup)
    bot.register_next_step_handler(msg, lambda m: give_usb_advice(m, iso_name))

def give_usb_advice(message, iso_name):
    user_os = message.text.lower()
    ventoy_incompatible = ["androidx86", "blissos", "fydeos", "primeos"]
    iso_name_lower = iso_name.lower().replace(" ", "")
    
    advice = f"💡 *{iso_name}* uchun USB tayyorlash bo'yicha maslahat:\n\n"
    
    is_ventoy_ok = True
    for bad_os in ventoy_incompatible:
        if bad_os in iso_name_lower:
            is_ventoy_ok = False
            break

    if is_ventoy_ok:
        advice += "✅ Bu OS uchun **Ventoy** tavsiya etiladi. Fleshkani bir marta formatlaysiz va ISO faylini shunchaki ichiga tashlaysiz.\n\n"
    else:
        advice += "⚠️ Bu OS Ventoy bilan yaxshi ishlamasligi mumkin. Shuning uchun 'Direct Write' usulidan foydalaning (Rufus yoki Etcher).\n\n"

    if user_os == "windows":
        advice += "🛠 **Windows uchun:** Rufus, BalenaEtcher yoki Ventoy."
    elif user_os == "linux":
        advice += "🛠 **Linux uchun:** BalenaEtcher, Ventoy yoki `dd` buyrug'i."
    elif user_os == "macos":
        advice += "🛠 **MacOS uchun:** BalenaEtcher yoki Raspberry Pi Imager."
    else:
        advice += "🛠 **Tavsiya:** BalenaEtcher barcha platformalarda ishlaydi."

    bot.send_message(message.chat.id, advice, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(commands=['search'])
def ask_search_query(message):
    msg = bot.send_message(message.chat.id, "🔍 Qaysi operatsion tizimni qidiryapsiz? Nomini kiriting (masalan, <i>Ubuntu</i> yoki <i>Mint</i>):", parse_mode="HTML")
    bot.register_next_step_handler(msg, process_search_step)

def process_search_step(message):
    search_term = message.text.strip()
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM iso_images WHERE name LIKE ?", (f'%{search_term}%',))
    results = cursor.fetchall()
    conn.close()

    if results:
        response = f"🔍 <b>'{search_term}'</b> bo'yicha qidiruv natijalari:\n\n"
        for row in results:
            response += f"🆔 <b>ID:</b> {row[0]} — <b>{row[1]}</b>\n"
        
        response += "\n💡 <i>O'rnatish videosi uchun /select, yuklab olish uchun /download tugmasini bosing va ID raqamni kiriting.</i>"
        bot.send_message(message.chat.id, response, parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, f"Kechirasiz, <b>'{search_term}'</b> nomli operatsion tizim topilmadi. Boshqa nom yozib ko'ring.", parse_mode="HTML")
# Render uchun kichik web server
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run_flask():
    # Render avtomatik ravishda PORT muhit o'zgaruvchisini beradi
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    init_db()
    populate_database()
    
    # Web serverni alohida oqimda (thread) ishga tushirish
    threading.Thread(target=run_flask).start()
    
    print("Bot ishga tushdi...")
    bot.infinity_polling()