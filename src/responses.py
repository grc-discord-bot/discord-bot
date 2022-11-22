

def get_response(message: str) -> str:
    process_msg = message.lower()

    if process_msg == 'hello':
        return 'Welcome to Google Student Developer Club@GRC/competitive programming club! I am Mardo the moderator ' \
               'bot for this club, click on my icon to see how to interact with me! '

    if process_msg == '$help':
        return "`This is a help message that you can modify.`"

#    return "I don't understand what you are saying."
