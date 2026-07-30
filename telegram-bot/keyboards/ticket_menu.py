from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def ticket_menu(ticket_types):
    buttons = []
    for ticket in ticket_types:
        buttons.append([
            InlineKeyboardButton(
                f"{ticket['name']} - {ticket['price']}",
                callback_data=f"ticket:{ticket['id']}"
            )
        ])
    return InlineKeyboardMarkup(buttons)
