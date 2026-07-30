from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def payment_menu(order_id):
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "💳 پرداخت",
                callback_data=f"pay:{order_id}"
            )
        ],
        [
            InlineKeyboardButton(
                "❌ لغو سفارش",
                callback_data=f"cancel:{order_id}"
            )
        ]
    ])
