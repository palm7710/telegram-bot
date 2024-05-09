from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# アクセストークン
TOKEN = "YOUR_TOKEN_HERE"

class TelegramBot:
    def __init__(self, system):
        self.system = system

    def start(self, update, context):
        # ユーザIDを取得し、システムからの最初の発話を取得し、送信
        input = {'utt': None, 'sessionId': str(update.effective_user.id)}
        update.message.reply_text(self.system.initial_message(input)["utt"])

    def message(self, update, context):
        # ユーザからの発話とユーザIDを取得し、発話を生成して送信
        input = {'utt': update.message.text, 'sessionId': str(update.effective_user.id)}
        system_output = self.system.reply(input)
        update.message.reply_text(system_output["utt"])

    def run(self):
        # Updater インスタンスの初期化
        updater = Updater(TOKEN)
        dp = updater.dispatcher
        # コマンドハンドラとメッセージハンドラの追加
        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(MessageHandler(Filters.text, self.message))  # Filters.text を使ってテキストメッセージのみをフィルタリング
        updater.start_polling()
        updater.idle()

# Assume EchoSystem class is defined elsewhere
if __name__ == '__main__':
    system = EchoSystem()  # EchoSystem は別途定義されている必要がある
    bot = TelegramBot(system)
    bot.run()
