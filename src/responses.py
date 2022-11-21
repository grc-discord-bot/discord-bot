import discord


def get_response(message: str) -> str:
    process_msg = message.lower()

    if process_msg == 'hello':
        return 'Welcome to Google Student Developer Club@GRC/competitive programming club!'

#    if process_msg == '!help':
#        return "`This is a help message that you can modify.`"

#    return "I don't understand what you are saying."
