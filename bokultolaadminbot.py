import telebot

# আপনার বটের টোকেনটি এখানে বসান
BOT_TOKEN = "7265940573:AAGkgORYa24OFdPOaUikUYq_6_wwkm1xKtc"
bot = telebot.TeleBot(BOT_TOKEN)

# যে মেসেজটি বট সবাইকে পাঠাবে
WARNING_MSG = (
    "This Bot has been hacked."
    ""
    "                                                                                      –Hacked by Hak4X Lab"
)

# ১. কেউ বট স্টার্ট করলে (/start) এই মেসেজটি যাবে
@bot.message_handler(commands=['start'])
def send_start_message(message):
    bot.reply_to(message, WARNING_MSG)

# ২. কোনো ইউজার বা ওয়েবসাইট থেকে যেকোনো মেসেজ, অর্ডার বা ডেটা রিসিভ হলে
# এটি সমস্ত রিকোয়েস্টকে আটকে দেবে এবং গ্রুপে বা অন্য কোথাও ডেটা ফরওয়ার্ড করবে না
@bot.message_handler(func=lambda message: True)
def block_and_reply(message):
    # অর্ডারের মূল মেসেজটি এখানেই ড্রপ (Drop) বা ব্লক হয়ে যাবে
    # তার পরিবর্তে কেবল এই সতর্কবার্তাটি রিপ্লাই হিসেবে যাবে
    bot.reply_to(message, WARNING_MSG)

if __name__ == "__main__":
    print("Hak4X Lab-এর কাস্টম স্ক্রিপ্টটি চালু হয়েছে...")
    print("এখন সব ধরণের অর্ডার রিকোয়েস্ট এবং মেসেজ ব্লক হয়ে কেবল ইংরেজি বার্তাটি যাবে।")
    bot.infinity_polling()