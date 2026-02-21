import telebot
import sqlite3
from telebot import types

# Bot tokeningizni shu yerga yozing
TOKEN = "8479798538:AAGM851VKTQFdwEtl1qt9L-sTOsqnlhYFWE"
bot = telebot.TeleBot(TOKEN)

# 1. Ma'lumotlar bazasini va jadvallarni yaratish
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Foydalanuvchilar jadvali
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users 
                      (user_id INTEGER PRIMARY KEY, username TEXT, status TEXT)''')
    # ISO tasvirlar jadvali
    cursor.execute('''CREATE TABLE IF NOT EXISTS iso_images 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, reliability TEXT, video_url TEXT, download_link TEXT)''')
    conn.commit()
    conn.close()

# 2. Bazaga boshlang'ich ma'lumotlarni qo'shish
def populate_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM iso_images")
    if cursor.fetchone()[0] == 0:
        iso_list = [
    # --- OMMABOP VA ODDIY FOYDALANUVCHILAR UCHUN ---
    ('Linux Mint Cinnamon', 'Juda yuqori (Rasmiy)', 'https://youtu.be/POf5mCs5YgI', 'https://pub.linuxmint.io/stable/22.3/linuxmint-22.3-cinnamon-64bit.iso'),
    ('Linux Mint XFCE', 'Juda yuqori (Rasmiy)', 'https://youtu.be/ULrJVk4JJ20', 'https://pub.linuxmint.io/stable/22.3/linuxmint-22.3-xfce-64bit.iso'),
    ('Ubuntu Desktop 24.04', 'Juda yuqori', 'https://youtu.be/fUvXN-BngS4', 'https://releases.ubuntu.com/24.04/ubuntu-24.04.1-desktop-amd64.iso'),
    ('Zorin OS Core', 'Yuqori', 'https://youtu.be/7Vp9V9T6vWc', 'https://mirrors.edge.kernel.org/zorinos/17/Zorin-OS-17.1-Core-64-bit.iso'),
    ('Pop!_OS (NVIDIA)', 'Yuqori (Geymerlar uchun)', 'https://youtu.be/pS0POnV9KNo', 'https://iso.pop-os.org/22.04/amd64/nvidia/44/pop-os_22.04_amd64_nvidia_44.iso'),
    ('Elementary OS', 'O’rtacha', 'https://youtu.be/Xm99S-G7oU0', 'https://elementary.io/latest.iso'),
    ('Fedora Workstation', 'Yuqori', 'https://youtu.be/Yp04w_S_M_A', 'https://download.fedoraproject.org/pub/fedora/linux/releases/40/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-40-1.1.iso'),
    ('Manjaro KDE Plasma', 'Yuqori', 'https://youtu.be/5P_IAn6pS7E', 'https://download.manjaro.org/kde/24.0/manjaro-kde-24.0-240513-linux66.iso'),
    ('Deepin OS', 'O’rtacha (Dizayn)', 'https://youtu.be/1u7u8p_A9oA', 'https://cdimage.deepin.com/releases/23/deepin-desktop-community-23-x86_64.iso'),
    ('MX Linux', 'Juda yuqori (Barqaror)', 'https://youtu.be/As_FkIom_9I', 'https://mxlinux.org/latest-iso/'),

    # --- KUCHSIZ KOMPYUTERLAR UCHUN (LIGHTWEIGHT) ---
    ('Lubuntu', 'Yuqori', 'https://youtu.be/vS_M2p-u5rY', 'https://cdimage.ubuntu.com/lubuntu/releases/24.04/release/lubuntu-24.04-desktop-amd64.iso'),
    ('Linux Lite', 'Yuqori', 'https://youtu.be/V6E98Ie-E8M', 'https://osdn.net/dl/linuxlite/linux-lite-7.0-64bit.iso'),
    ('Puppy Linux', 'O’rtacha', 'https://youtu.be/L83pY6v9lKk', 'https://distro.ibiblio.org/puppylinux/puppy-fossa/fossapup64-9.5.iso'),
    ('AntiX Linux', 'Yuqori', 'https://youtu.be/96_S_98K3rU', 'https://antixlinux.com/download/'),
    ('Peppermint OS', 'O’rtacha', 'https://youtu.be/wXhK-y_oF4M', 'https://peppermintos.com/download/'),
    ('Bodhi Linux', 'O’rtacha', 'https://youtu.be/m9_3E-m5R7c', 'https://www.bodhilinux.com/download/'),
    ('Tiny Core Linux', 'Past (Faqat mutaxassislar uchun)', 'https://youtu.be/1mE-R_87qis', 'http://tinycorelinux.net/15.x/x86_64/release/CorePure64-15.0.iso'),
    ('Xubuntu', 'Yuqori', 'https://youtu.be/S_B7_P7R7vM', 'https://cdimage.ubuntu.com/xubuntu/releases/24.04/release/xubuntu-24.04-desktop-amd64.iso'),

    # --- KIBERXAVFSIZLIK VA TESTLASH UCHUN ---
    ('Kali Linux', 'Juda yuqori', 'https://youtu.be/L6mN0Xv6_O4', 'https://cdimage.kali.org/kali-2024.2/kali-linux-2024.2-installer-amd64.iso'),
    ('Parrot Security OS', 'Yuqori', 'https://youtu.be/kP7I8Y6S6M4', 'https://download.parrot.sh/parrot/iso/6.1/Parrot-security-6.1_amd64.iso'),
    ('BlackArch Linux', 'Past (Qiyin)', 'https://youtu.be/vD5K_6N-Dmg', 'https://blackarch.org/download.html'),
    ('Tails', 'Yuqori (Anonimlik)', 'https://youtu.be/CAAnmC5_PzY', 'https://tails.net/install/download/index.en.html'),
    ('Whonix', 'Yuqori', 'https://youtu.be/39uD0U_O-lE', 'https://www.whonix.org/wiki/Download'),

    # --- PROFESSIONAL VA DASTURCHILAR UCHUN ---
    ('Arch Linux', 'O’rtacha (Qiyin o’rnatish)', 'https://youtu.be/DPLnKs67P_I', 'https://mirrors.edge.kernel.org/archlinux/iso/latest/archlinux-x86_64.iso'),
    ('Debian 12 Bookworm', 'Juda yuqori', 'https://youtu.be/I7_4G7Sg6Xk', 'https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.6.0-amd64-netinst.iso'),
    ('EndeavourOS', 'Yuqori', 'https://youtu.be/mXN-iM2A028', 'https://endeavouros.com/latest-release/'),
    ('openSUSE Tumbleweed', 'Yuqori', 'https://youtu.be/X0pE7mHj850', 'https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso'),
    ('Solus OS', 'O’rtacha', 'https://youtu.be/rNndp97nCfs', 'https://getsol.us/download/'),
    ('Gentoo Linux', 'Juda past (Ekspertlar)', 'https://youtu.be/V6n0-EwE9gM', 'https://www.gentoo.org/downloads/'),
    ('Slackware', 'Past (Retro)', 'https://youtu.be/rS8S-M9QoO4', 'http://www.slackware.com/getslack/'),
    ('AlmaLinux (Server)', 'Yuqori', 'https://youtu.be/p667Ait_U_0', 'https://almalinux.org/get-almalinux/'),
    ('Rocky Linux (Server)', 'Yuqori', 'https://youtu.be/A9V0uIidA3Y', 'https://rockylinux.org/download'),

    # --- NOODATIY VA QIZIQARLI TIZIMLAR ---
    ('ChromeOS Flex', 'Yuqori', 'https://youtu.be/0p_mD2V6D9o', 'https://chromeenterprise.google/os/chromeosflex/'),
    ('Android-x86', 'O’rtacha', 'https://youtu.be/tAnp5D8UqC8', 'https://www.android-x86.org/download.html'),
    ('Garuda Linux', 'O’rtacha (Dizayn)', 'https://youtu.be/u1eT_yM79A4', 'https://garudalinux.org/downloads.html'),
    ('Nobara Project', 'Yuqori (Gaming)', 'https://youtu.be/tS9tX-OndyA', 'https://nobaraproject.org/download-nobara/'),
    ('Void Linux', 'O’rtacha', 'https://youtu.be/8I6YV_oY0B0', 'https://voidlinux.org/download/'),
    ('NixOS', 'O’rtacha (Konfiguratsiya)', 'https://youtu.be/CwfOf7y0C60', 'https://nixos.org/download.html'),
    ('Haiku OS', 'Past (Eksperimental)', 'https://youtu.be/v_E6QUnG758', 'https://www.haiku-os.org/get-haiku/'),
    ('FreeBSD', 'O’rtacha (Unix)', 'https://youtu.be/jP_V5k0W_Dk', 'https://www.freebsd.org/where/'),
    ('ReactOS', 'Past (Windows kloni)', 'https://youtu.be/I9j4_fI6_vE', 'https://reactos.org/download/'),
    ('Kubuntu', 'Yuqori', 'https://youtu.be/g_p70_m1qS0', 'https://kubuntu.org/getkubuntu/'),
    ('Ubuntu Budgie', 'Yuqori', 'https://youtu.be/8_Y990Xp_Uo', 'https://ubuntubudgie.org/downloads/'),
    ('ArcoLinux', 'Yuqori (O’rganish uchun)', 'https://youtu.be/oXn5m26V0V0', 'https://arcolinux.com/downloads/'),
    ('GhostBSD', 'O’rtacha', 'https://youtu.be/u88rT_rY1Sg', 'https://ghostbsd.org/download'),
    ('PureOS', 'Yuqori (Xavfsiz)', 'https://youtu.be/mF80vK_1uS0', 'https://pureos.net/download/'),
    ('Alpine Linux', 'Past (Juda kichik)', 'https://youtu.be/j7v_wV_U-sU', 'https://alpinelinux.org/downloads/'),
    ('Mageia', 'O’rtacha', 'https://youtu.be/v_vWv_pS-v8', 'https://www.mageia.org/en/downloads/'),
    ('OpenBSD', 'Yuqori (Xavfsizlik)', 'https://youtu.be/i_G7MhO7e8Q', 'https://www.openbsd.org/ftp.html'),
    ('Qubes OS', 'O’rtacha (Maxfiy)', 'https://youtu.be/h9T_K_X0D0Y', 'https://www.qubes-os.org/download/'),
]
        cursor.executemany('''INSERT INTO iso_images (name, reliability, video_url, download_link) 
                              VALUES (?, ?, ?, ?)''', iso_list)
        conn.commit()
    conn.close()

# --- BOT HANDLERLARI ---

@bot.message_handler(commands=['start', 'register'])
def register(message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT OR IGNORE INTO Users (user_id, username, status) VALUES (?, ?, ?)", 
                       (message.from_user.id, message.from_user.username, 'registered'))
        conn.commit()
    except Exception as e:
        print(f"Xatolik: {e}")
    finally:
        conn.close()
    
    bot.reply_to(message, "Salom! Siz muvaffaqiyatli ro'yxatdan o'tdingiz.\n\nBuyruqlar:\n/view - ISO ro'yxatini ko'rish\n/select - Video qo'llanma\n/download - Yuklab olish")

@bot.message_handler(commands=['view'])
def view_images(message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, reliability FROM iso_images")
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        bot.send_message(message.chat.id, "Hozircha bazada ma'lumot yo'q.")
        return

    response = "📂 **Mavjud ISO tasvirlar:**\n\n"
    for row in rows:
        response += f"🆔 ID: {row[0]}\n💿 Nomi: {row[1]}\n✅ Ishonchlilik: {row[2]}\n" + "-"*20 + "\n"
        if len(response) > 3500: # Telegram limitidan oshib ketmasligi uchun
            bot.send_message(message.chat.id, response, parse_mode="Markdown")
            response = ""
    
    if response:
        bot.send_message(message.chat.id, response, parse_mode="Markdown")

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
        bot.send_message(message.chat.id, f"🎬 *{res[0]}* o'rnatish qo'llanmasi:\n{res[1]}", parse_mode="Markdown")
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

if __name__ == "__main__":
    init_db()
    populate_database()
    print("Bot ishga tushdi...")
    bot.infinity_polling()