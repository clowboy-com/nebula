import core.decorators
from config import Config

@core.decorators.owner.init
def init(update, context):
    bot = context.bot
    chat_title = update.message.chat.title
    operator_id = update.message.from_user.id
    bot.leaveChat(update.message.chat_id)
    bot.send_message(Config.LOG_CHANNEL,
    text="#LOG\n {} has left the {} group\n by the operator <code>{}</code>".format(
        "@"+bot.username,
         chat_title,
         operator_id),parse_mode='HTML'
        )