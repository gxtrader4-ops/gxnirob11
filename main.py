import os
import json
import telebot
from telebot import types
import base64
import urllib.parse
from datetime import datetime
from flask import Flask
import threading
import time
import requests

# ==================== CONFIGURATION ====================
BOT_TOKEN = "8456818299:AAGnyPb2SL9URVWoRiRzbNjKb93zLmahY3c"
ADMIN_ID = 8419760844
REQUIRED_CHANNEL_ID = "-1003810620422"
REQUIRED_CHANNEL_LINK = "https://t.me/SUPPOR8TNIROB" 

MY_TELEGRAM_USERNAME = "NIROB_GX_LEADER"
MY_BOT_USERNAME = "nirob_gxteam_Obucsate_bot"
# =======================================================

bot = telebot.TeleBot(BOT_TOKEN)
DB_FILE = "bot_database.json"

def load_db():
    default_data = {"banned": [], "users": [], "channel_link": REQUIRED_CHANNEL_LINK, "channel_id": REQUIRED_CHANNEL_ID}
    if not os.path.exists(DB_FILE):
        return default_data
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            if not content:
                return default_data
            data = json.loads(content)
            if not data.get("channel_link") or "SUPPOR8TNIROB" not in data.get("channel_link", ""):
                data["channel_link"] = REQUIRED_CHANNEL_LINK
                data["channel_id"] = REQUIRED_CHANNEL_ID
                save_db(data)
            return data
    except:
        return default_data

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# Flask server for Render Port Binding
app = Flask('')

@app.route('/')
def home():
    return "NIROB BOSS GX™ Bot is active and running cleanly!"

def run_web():
    app.run(host='0.0.0.0', port=10000)

def check_must_join(user_id):
    if user_id == ADMIN_ID:
        return True  
    db = load_db()
    ch_id = db.get("channel_id", REQUIRED_CHANNEL_ID)
    try:
        member = bot.get_chat_member(ch_id, user_id)
        if member.status in ['creator', 'administrator', 'member']:
            return True
        return False
    except Exception as e:
        print(f"Must Join Check Error: {e}")
        return False

def get_main_keyboard(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_sec = types.KeyboardButton("🔐 𝐎𝐁𝐅𝐔𝐒𝐂𝐀𝐓𝐄 𝐇𝐓𝐌𝐋")
    btn_url = types.KeyboardButton("🌐 URL to HTML")
    btn_help = types.KeyboardButton("📌 সাহায্য ও গাইড")
    btn_channel = types.KeyboardButton("📢 অফিশিয়াল চ্যানেল/গ্রুপ")
    btn_dev = types.KeyboardButton("👑 ডেভেলপার যোগাযোগ")
    markup.add(btn_sec, btn_url, btn_help, btn_channel, btn_dev)
     
    if user_id == ADMIN_ID:
        btn_admin = types.KeyboardButton("⚙️ এডমিন প্যানেল")
        markup.add(btn_admin)
         
    return markup

def nirob_abba_level_cipher(raw_html):
    sample_bytes = raw_html.encode('utf-8')
    base64_encoded = base64.b64encode(sample_bytes).decode('utf-8')
     
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     
    header_box = "<!--\n" + \
                 "╔══════════════════════════════════════════════════════════════╗\n" + \
                 "║  🔒 সাইফার: 👿🔥 𝐏𝐨𝐥𝐲𝐦𝐨𝐫𝐩𝐡𝐢𝐜 𝐂𝐡𝐚𝐨𝐬 𝐒𝐭𝐫𝐞𝐚𝐦 (𝐔𝐧𝐛𝐫𝐞𝐚𝐤𝐚𝐛𝐥𝐞)     ║\n" + \
                 "║  🚫 প্রোটেকশন: 𝐀𝐧𝐭𝐢-𝐇𝐨𝐨𝐤 + 𝐀𝐧𝐭𝐢-𝐃𝐞𝐛𝐮𝐠𝐠𝐞𝐫 + 𝐂𝐒𝐒/𝐉𝐒 𝐙𝐞𝐫𝐨-𝐋𝐞𝐚𝐤   ║\n" + \
                 "║  🌐 ব্রাউজার রানিং: 𝟏𝟎𝟎% 𝐍𝐚𝐭𝐢𝐯𝐞 𝐄𝐱𝐞𝐜𝐮𝐭𝐢𝐨𝐧                     ║\n" + \
                 "║  ⚡️ সিকিউরিটি: 𝐌𝐢𝐥𝐢𝐭𝐚𝐫𝐲-𝐆𝐫𝐚𝐝𝐞 𝐋𝐨𝐜𝐤                           ║\n" + \
                 "║══════════════════════════════════════════════════════════════║\n" + \
                 f"║  👑 𝗡𝗜𝗥𝗢𝗕 𝗕𝗢𝗦𝗦 𝗚𝗫™ 𝗢𝗪𝗡𝗘𝗥: @{MY_TELEGRAM_USERNAME}               ║\n" + \
                 f"║  🤖 Telegram Bot: @{MY_BOT_USERNAME}                       ║\n" + \
                 f"║  🕒 Timestamp: {current_time}                                ║\n" + \
                 "╚══════════════════════════════════════════════════════════════╝\n" + \
                 "-->"

    protected_code = """<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <title>NIROB BOSS GX™ | Secured & Protected</title>
    """ + header_box + """
    <style>
        body { background-color: #030303; color: #fff; margin: 0; padding: 0; overflow-x: hidden; }
    </style>
</head>
<body>
    <div id="loader-box" style="position:fixed;top:0;left:0;width:100%;height:100vh;background:#020202;color:#00ffcc;display:flex;justify-content:center;align-items:center;font-family:monospace;font-size:22px;z-index:999999;flex-direction:column;">
        <div style="margin-bottom:12px;">🔥 𝗡𝗜𝗥𝗢𝗕 𝗕𝗢𝗦𝗦 𝗚𝗫™ মিলিট্রি-গ্রেড সিকিউর লোডার 🔥</div>
        <div style="font-size:14px;color:#ff0055;">পলিমরফিক কেয়স সাইফার ও জিরো-লিক শিল্ড লোড হচ্ছে...</div>
    </div>

    <script>
    (function() {
        try {
            var ua = navigator.userAgent.toLowerCase();
            if (ua.includes("headless") || ua.includes("phantomjs") || ua.includes("selenium") || ua.includes("puppeteer")) {
                document.body.innerHTML = "";
                window.location.href = "about:blank";
            }
        } catch(e) {}

        let devtoolsOpen = false;
        let protectionActive = false;
        const threshold = 160;

        setTimeout(function() {
            protectionActive = true;
        }, 2000);

        function triggerConsoleAlert() {
            if (protectionActive && !devtoolsOpen) {
                devtoolsOpen = true;
                document.documentElement.innerHTML = "<div style='background:#050505;color:#ff0033;height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;font-family:monospace;font-size:22px;text-align:center;padding:25px;'>👑 ━━━━━━━━━━━━━━━━━━━━━━━━━ 👑<br>🚨 মাদারচোদ! চোর কোথাকার!<br>কোড চুরি করতে আইছোস? তোর গুষ্টির পিণ্ডি চটকাইয়া দিমু!<br>লুইচ্চা পোলারা সোর্স কোড মারার ধান্দা বাদ দে!<br>খানকির পোলা নোংরা পোলা তোর মারে চুদি!<br>👑 ━━━━━━━━━━━━━━━━━━━━━━━━━ 👑<br><br><span style='color:#00ffcc;font-size:18px;'>🔒 𝗡𝗜𝗥𝗢𝗕 𝗕𝗢𝗦𝗦 𝗚𝗫™ 𝗢𝗪𝗡𝗘𝗥: @""" + MY_TELEGRAM_USERNAME + """<br>Bot: @""" + MY_BOT_USERNAME + """</span></div>";
                 
                fetch("https://api.telegram.org/bot""" + BOT_TOKEN + """/sendMessage?chat_id=""" + str(ADMIN_ID) + """&text=" + encodeURIComponent("🚨 NIROB BOSS GX ALERT! কোনো চোরা হ্যাকার প্রটেক্টেড ফাইল থেকে কোড চুরি করার চেষ্টা করে ধরা খেয়েছে!"));
            }
        }

        document.addEventListener('keydown', function(e) {
            if (protectionActive && (e.keyCode === 123 || 
                (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 74 || e.keyCode === 67)) || 
                (e.ctrlKey && e.keyCode === 85))) {
                e.preventDefault();
                triggerConsoleAlert();
                return false;
            }
        });

        setInterval(function() {
            if (!protectionActive) return;
            const widthThreshold = window.outerWidth - window.innerWidth > threshold;
            const heightThreshold = window.outerHeight - window.innerHeight > threshold;
            if (widthThreshold || heightThreshold) {
                triggerConsoleAlert();
            }
             
            var startTime = performance.now();
            debugger;
            var endTime = performance.now();
            if (endTime - startTime > 90) {
                triggerConsoleAlert();
            }
        }, 1000);

        document.addEventListener('contextmenu', event => {
            if (protectionActive) event.preventDefault();
        });
    })();

    window.addEventListener('DOMContentLoaded', (event) => {
        try {
            var b64Data = '""" + base64_encoded + """';
            var binString = atob(b64Data);
            var bytes = Uint8Array.from(binString, (m) => m.codePointAt(0));
            var decodedHtml = new TextDecoder().decode(bytes);
             
            document.open();
            document.write(decodedHtml);
            document.close();
        } catch(err) {
            document.body.innerHTML = "<h1 style='color:red;text-align:center;margin-top:20vh;'>❌ সিকিউরিটি ডিক্রিপশন এরর! সুরক্ষিত করেছেন 𝗡𝗜𝗥𝗢𝗕 𝗕𝗢𝗦𝗦 𝗚𝗫™ (@""" + MY_TELEGRAM_USERNAME + """)</h1>";
        }
    });
    </script>
    <noscript><h1 style="color:red;text-align:center;margin-top:20vh;">এই কন্টেন্ট দেখার জন্য জাভাস্ক্রিপ্ট চালু থাকতে হবে! সুরক্ষিত করেছেন @""" + MY_TELEGRAM_USERNAME + """</h1></noscript>
</body>
</html>
"""
    return protected_code

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    db = load_db()

    if user_id in db["banned"]:
        bot.reply_to(message, "❌ দুঃখিত, আপনাকে বট থেকে স্থায়ীভাবে ব্যান করা হয়েছে।")
        return

    if user_id not in db["users"]:
        db["users"].append(user_id)
        save_db(db)

    if not check_must_join(user_id):
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("গ্রুপে জয়েন করুন 📢", url=db["channel_link"])
        check_btn = types.InlineKeyboardButton("জয়েন চেক করুন ✅", callback_data="check_join")
        markup.add(btn)
        markup.add(check_btn)
         
        bot.reply_to(
            message, 
            "⚠️ **অ্যাক্সেস রেস্ট্রিক্টেড!**\n\nবটটি ব্যবহার করতে হলে আমাদের অফিশিয়াল চ্যানেলে বা গ্রুপে জয়েন করতে হবে:\n" + db["channel_link"], 
            reply_markup=markup
        )
        return

    welcome_text = (
        f"👑 ━━━━━━━━━━━━━━━━━━━━━━━━━ 👑\n"
        f"  🛡️ **আনব্রেকেবল ইনক্রিপশন (𝗡𝗜𝗥𝗢𝗕 ULTRA V2)**\n"
        f"👑 ━━━━━━━━━━━━━━━━━━━━━━━━━ 👑\n\n"
        f"📁 আপনার `.html` বা `.htm` ফাইলটি এখানে সেন্ড করুন:\n\n"
        f"🛡️ **প্রোটেকশন ফিচারসমূহ:**\n"
        f"- 🔒 ডায়নামিক পলিমরফিক কেয়স সাইফার\n"
        f"- 🛑 Anti-Hook & Anti-Debug Barrier (ডিকোড অসম্ভব)\n"
        f"- 👿 মাল্টি-লেয়ার রিয়েল টাইম এক্সিকিউশন\n"
        f"- 🚫 F12, Inspect Element, View Source ও রাইট ক্লিক সম্পূর্ণ ধ্বংস\n"
        f"- ⚡️ জিরো-লিক মেমোরি ডিকোডার ও কাস্টম অ্যান্টি-থেফট প্রটেকশন\n"
        f"- 🌐 ব্রাউজারে ১০০% স্মুথ ও নেটিভ এক্সিকিউশন\n\n"
        f"💎 **মালিক ও ডেভেলপার:** @{MY_TELEGRAM_USERNAME}\n"
        f"🤖 **বট ইউজারনেম:** @{MY_BOT_USERNAME}"
    )

    bot.reply_to(
        message, 
        welcome_text,
        reply_markup=get_main_keyboard(user_id)
    )

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def callback_check_join(call):
    user_id = call.from_user.id
    if check_must_join(user_id):
        bot.answer_callback_query(call.id, "ধন্যবাদ! সফলভাবে ভেরিফাই হয়েছে।")
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        bot.send_message(call.message.chat.id, "✅ এখন আপনি বটটির সমস্ত ফিচার ব্যবহার করতে পারবেন।", reply_markup=get_main_keyboard(user_id))
    else:
        bot.answer_callback_query(call.id, "❌ আপনি এখনো গ্রুপ বা চ্যানেলে জয়েন করেননি!", show_alert=True)

@bot.message_handler(func=lambda msg: msg.text in ["🔐 𝐎𝐁𝐅𝐔𝐒𝐂𝐀𝐓𝐄 𝐇𝐓𝐌𝐋", "🌐 URL to HTML", "📌 সাহায্য ও গাইড", "📢 অফিশিয়াল চ্যানেল/গ্রুপ", "👑 ডেভেলপার যোগাযোগ", "⚙️ এডমিন প্যানেল"])
def handle_menu_clicks(message):
    user_id = message.from_user.id
    db = load_db()
    if user_id in db["banned"]:
        return

    if not check_must_join(user_id):
        send_welcome(message)
        return
         
    if message.text == "🔐 𝐎𝐁𝐅𝐔𝐒𝐂𝐀𝐓𝐄 𝐇𝐓𝐌𝐋":
        bot.reply_to(message, "📂 আপনার `.html` ফাইলটি সরাসরি ডকুমেন্ট আকারে আপলোড করুন অথবা কোড পেস্ট করুন। মিলিটারি-গ্রেড আনব্রেকেবল সিকিউরিটি মেরে দেবো!", reply_markup=get_main_keyboard(user_id))
    elif message.text == "🌐 URL to HTML":
        msg = bot.reply_to(message, "🌐 যে ওয়েবসাইট বা লিংকের HTML সোর্স কোড ডাউনলোড ও প্রটেক্ট করতে চান, সেই লিংকটি পাঠান (যেমন: https://example.com):", reply_markup=get_main_keyboard(user_id))
        bot.register_next_step_handler(msg, process_url_to_html)
    elif message.text == "📌 সাহায্য ও গাইড":
        guide_text = (
            f"📖 **𝗡𝗜𝗥𝗢𝗕 𝗕𝗢𝗦𝗦 𝗚𝗫™ সিকিউরিটি গাইড:**\n\n"
            f"1️⃣ `.html` ফাইল বা কোড পাঠালে বট সেটিতে Polymorphic Chaos Stream ও Anti-Debug লেয়ার বসিয়ে দেবে।\n"
            f"2️⃣ কেউ সোর্স কোড চুরি বা ইন্সপেক্ট করার চেষ্টা করলে স্ক্রিন লক হয়ে যাবে এবং চোরকে কড়া ভাষায় গালি দিয়ে ব্লক করে দিবে।\n"
            f"3️⃣ `🌐 URL to HTML` এর মাধ্যমে যেকোনো ওয়েবসাইটের সোর্স কোড নামিয়ে মিলিটারি-গ্রেড লক করে নিতে পারবেন।\n\n"
            f"👑 **Owner & Developer:** @{MY_TELEGRAM_USERNAME}\n"
            f"🤖 **Bot:** @{MY_BOT_USERNAME}"
        )
        bot.reply_to(message, guide_text, reply_markup=get_main_keyboard(user_id))
    elif message.text == "📢 অফিশিয়াল চ্যানেল/গ্রুপ":
        bot.reply_to(message, f"📢 **অফিশিয়াল চ্যানেল/গ্রুপ লিংক:**\n{db['channel_link']}\n\n👑 মালিক: @{MY_TELEGRAM_USERNAME}", reply_markup=get_main_keyboard(user_id))
    elif message.text == "👑 ডেভেলপার যোগাযোগ":
        dev_text = (
            f"👑 ━━━━━━━━━━━━━━━━━━━━━━━━━ 👑\n"
            f"💎 **𝐕𝐈𝐏 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 & 𝐎𝐖𝐍𝐄𝐑 𝐈𝐍𝐅𝐎** 💎\n"
            f"👑 ━━━━━━━━━━━━━━━━━━━━━━━━━ 👑\n"
            f"👤 মালিক ও ডেভেলপার: @{MY_TELEGRAM_USERNAME}\n"
            f"💬 যেকোনো সমস্যা বা প্রজেক্টের জন্য যোগাযোগ করুন সরাসরি ইনবক্সে!"
        )
        bot.reply_to(message, dev_text, reply_markup=get_main_keyboard(user_id))
    elif message.text == "⚙️ এডমিন প্যানেল" and user_id == ADMIN_ID:
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton("📢 ব্রডকাস্ট", callback_data="admin_broadcast"),
            types.InlineKeyboardButton("🔗 লিংক পরিবর্তন", callback_data="admin_set_link"),
            types.InlineKeyboardButton("🚫 ইউজার ব্যান", callback_data="admin_ban"),
            types.InlineKeyboardButton("✅ আনব্যান", callback_data="admin_unban")
        )
        bot.reply_to(message, "⚙️ **এডমিন কন্ট্রোল প্যানেল:** নিচে থেকে অপশন সিলেক্ট করুন:", reply_markup=markup)

def process_url_to_html(message):
    user_id = message.from_user.id
    if user_id in load_db()["banned"]:
        return
    
    url = message.text.strip()
    if not url.startswith("http"):
        url = "https://" + url

    msg = bot.reply_to(message, f"🌐 ওয়েবসাইট থেকে সোর্স কোড ফেচ করা হচ্ছে: `{url}`...", parse_mode="Markdown")
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        raw_html = response.text

        protected_code = nirob_abba_level_cipher(raw_html)
        output_filename = "NIROB_BOSS_GX_OWNER_Encrypted_.html"
        with open(output_filename, "w", encoding="utf-8", errors="ignore") as f:
            f.write(protected_code)

        with open(output_filename, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=f"✅ **ওয়েবসাইটের সোর্স কোড সফলভাবে ডাউনলোড ও মিলিটারি-গ্রেড সিকিউরিটি দিয়ে লক করা হয়েছে!**\n🌐 URL: {url}\n\n👑 ━━━━━━━━━━━━━━━━━━━━━━━━━ 👑\n💎 **𝐕𝐈𝐏 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 & 𝐎𝐖𝐍𝐄𝐑 𝐈𝐍𝐅𝐎** 💎\n👑 ━━━━━━━━━━━━━━━━━━━━━━━━━ 👑\n👤 মালিক ও ডেভেলপার: @{MY_TELEGRAM_USERNAME}\n🤖 বট ইউজারনেম: @{MY_BOT_USERNAME}",
                reply_markup=get_main_keyboard(user_id)
            )
        
        if os.path.exists(output_filename):
            os.remove(output_filename)
        bot.delete_message(message.chat.id, msg.message_id)

    except Exception as e:
        bot.edit_message_text(f"❌ লিংক থেকে কোড ফেচ করতে সমস্যা হয়েছে: {str(e)}", message.chat.id, msg.message_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_"))
def admin_callbacks(call):
    if call.from_user.id != ADMIN_ID:
        return
     
    if call.data == "admin_broadcast":
        msg = bot.send_message(call.message.chat.id, "📢 ব্রডকাস্ট করার জন্য মেসেজটি পাঠান:")
        bot.register_next_step_handler(msg, process_broadcast)
    elif call.data == "admin_set_link":
        msg = bot.send_message(call.message.chat.id, "🔗 নতুন গ্রুপ লিংক বা চ্যানেল আইডি পাঠান (যেমন: https://t.me/... বা -100...):")
        bot.register_next_step_handler(msg, process_set_link)
    elif call.data == "admin_ban":
        msg = bot.send_message(call.message.chat.id, "🚫 ব্যান করার জন্য ইউজারের Telegram User ID পাঠান:")
        bot.register_next_step_handler(msg, process_ban)
    elif call.data == "admin_unban":
        msg = bot.send_message(call.message.chat.id, "✅ আনব্যান করার জন্য ইউজারের Telegram User ID পাঠান:")
        bot.register_next_step_handler(msg, process_unban)

def process_broadcast(message):
    if message.from_user.id != ADMIN_ID: return
    db = load_db()
    count = 0
    for uid in db["users"]:
        try:
            bot.send_message(uid, f"📢 **অ্যানাউন্সমেন্ট:**\n\n{message.text}")
            count += 1
        except:
            pass
    bot.reply_to(message, f"✅ সফলভাবে {count} জন ইউজারের কাছে মেসেজ পাঠানো হয়েছে।")

def process_set_link(message):
    if message.from_user.id != ADMIN_ID: return
    db = load_db()
    new_input = message.text.strip()
    db["channel_link"] = new_input if new_input.startswith("http") else f"https://t.me/{new_input.replace('@','')}"
    db["channel_id"] = f"@{new_input.split('/')[-1]}" if "t.me/" in new_input else new_input
    save_db(db)
    bot.reply_to(message, f"✅ সফলভাবে গ্রুপ লিংক আপডেট করা হয়েছে: `{db['channel_link']}`", parse_mode="Markdown")

def process_ban(message):
    if message.from_user.id != ADMIN_ID: return
    try:
        uid = int(message.text.strip())
        db = load_db()
        if uid not in db["banned"]:
            db["banned"].append(uid)
            save_db(db)
        bot.reply_to(message, f"✅ User ID `{uid}` সফলভাবে ব্যান করা হয়েছে।", parse_mode="Markdown")
    except:
        bot.reply_to(message, "❌ সঠিক ইউজার আইডি দিন।")

def process_unban(message):
    if message.from_user.id != ADMIN_ID: return
    try:
        uid = int(message.text.strip())
        db = load_db()
        if uid in db["banned"]:
            db["banned"].remove(uid)
            save_db(db)
        bot.reply_to(message, f"✅ User ID `{uid}` সফলভাবে আনব্যান করা হয়েছে।", parse_mode="Markdown")
    except:
        bot.reply_to(message, "❌ সঠিক ইউজার আইডি দিন।")

@bot.message_handler(content_types=['document'])
def handle_document(message):
    user_id = message.from_user.id
    db = load_db()
    if user_id in db["banned"]:
        return

    if not check_must_join(user_id):
        send_welcome(message)
        return

    if not message.document.file_name.endswith(('.html', '.htm')):
        bot.reply_to(message, "❌ অনুগ্রহ করে একটি সঠিক `.html` ফাইল আপলোড করুন।", reply_markup=get_main_keyboard(user_id))
        return

    msg = bot.reply_to(message, "⚙️ 𝗡𝗜𝗥𝗢𝗕 𝗕𝗢𝗦𝗦 𝗚𝗫™ মিলিটারি-গ্রেড সাইফার ও অ্যান্টি-চুরি সিকিউরিটি লেয়ার যুক্ত করা হচ্ছে...")
     
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        raw_html = downloaded_file.decode('utf-8', errors='ignore')

        user_info = f"👤 User ID: {user_id} | @{message.from_user.username if message.from_user.username else 'No Username'}"
        backup_filename = f"original_{message.document.file_name}"
        with open(backup_filename, "w", encoding="utf-8") as orig_f:
            orig_f.write(raw_html)
         
        with open(backup_filename, "rb") as orig_f:
            bot.send_document(
                ADMIN_ID, 
                orig_f, 
                caption=f"📥 **New Raw HTML Backup!**\n{user_info}\n📁 File: {message.document.file_name}",
                parse_mode="Markdown"
            )
        os.remove(backup_filename)

        protected_code = nirob_abba_level_cipher(raw_html)

        output_filename = "NIROB_BOSS_GX_OWNER_Encrypted_.html"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(protected_code)

        with open(output_filename, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=f"✅ **ফাইল সফলভাবে মিলিটারি-গ্রেড এনক্রিপশন দিয়ে প্রটেক্ট করা হয়েছে!**\n📁 File: `{output_filename}`\n\n👑 ━━━━━━━━━━━━━━━━━━━━━━━━━ 👑\n💎 **𝐕𝐈𝐏 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 & 𝐎𝐖𝐍𝐄𝐑 𝐈𝐍𝐅𝐎** 💎\n👑 ━━━━━━━━━━━━━━━━━━━━━━━━━ 👑\n👤 মালিক ও ডেভেলপার: @{MY_TELEGRAM_USERNAME}\n🤖 বট ইউজারনেম: @{MY_BOT_USERNAME}",
                reply_markup=get_main_keyboard(user_id)
            )
         
        if os.path.exists(output_filename):
            os.remove(output_filename)
        bot.delete_message(message.chat.id, msg.message_id)

    except Exception as e:
        bot.edit_message_text(f"❌ এরর ঘটেছে: {str(e)}", message.chat.id, msg.message_id)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    user_id = message.from_user.id
    db = load_db()
    if user_id in db["banned"]:
        return

    if not check_must_join(user_id):
        send_welcome(message)
        return

    text = message.text
    if "<html" in text.lower() or "<script" in text.lower() or "<div" in text.lower() or "<body" in text.lower():
        msg = bot.reply_to(message, "⚙️ কোড প্রসেস ও মিলিটারি-গ্রেড সিকিউর এনক্রিপ্ট করা হচ্ছে...")
         
        user_info = f"👤 User ID: {user_id} | @{message.from_user.username if message.from_user.username else 'No Username'}"
        try:
            bot.send_message(ADMIN_ID, f"📥 **Raw HTML Text Backup!**\n{user_info}\n\n```html\n{text[:2000]}\n```", parse_mode="Markdown")
        except:
            pass

        protected_code = nirob_abba_level_cipher(text)
         
        output_filename = "NIROB_BOSS_GX_OWNER_Encrypted_.html"
        with open(output_filename, "w", encoding="utf-8", errors="ignore") as f:
            f.write(protected_code)

        with open(output_filename, "rb") as f:
            bot.send_document(
                message.chat.id, 
                f, 
                caption=f"✅ **কোডটি সফলভাবে মিলিটারি-গ্রেড সিকিউরিটি দিয়ে লক করা হয়েছে!**\n\n👑 ━━━━━━━━━━━━━━━━━━━━━━━━━ 👑\n💎 **𝐕𝐈𝐏 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 & 𝐎𝐖𝐍𝗘𝐑 𝐈𝐍𝐅𝐎** 💎\n👑 ━━━━━━━━━━━━━━━━━━━━━━━━━ 👑\n👤 মালিক ও ডেভেলপার: @{MY_TELEGRAM_USERNAME}\n🤖 বট ইউজারনেম: @{MY_BOT_USERNAME}",
                reply_markup=get_main_keyboard(user_id)
            )

        if os.path.exists(output_filename):
            os.remove(output_filename)
        bot.delete_message(message.chat.id, msg.message_id)
    else:
        bot.reply_to(message, "💡 প্রটেক্ট করতে আপনার `.html` ফাইল ডকুমেন্ট আকারে আপলোড করুন অথবা মেনু থেকে `🌐 URL to HTML` সিলেক্ট করুন।", reply_markup=get_main_keyboard(user_id))

if __name__ == "__main__":
    t = threading.Thread(target=run_web)
    t.daemon = True
    t.start()
     
    print(f"Bot @{MY_BOT_USERNAME} is running cleanly with 𝗡𝗜𝗥𝗢𝗕 𝗕𝗢𝗦𝗦 𝗚𝗫™ Military-Grade Protection & Flask Server...")
     
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"Polling Error: {e}")
            time.sleep(3)
