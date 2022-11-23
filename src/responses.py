

def get_response(message: str) -> str:
    process_msg = message.lower()

    if process_msg == 'hello':
        return 'Welcome to Google Student Developer Club@GRC/competitive programming club! I am Mardo the moderator ' \
               'bot for this club, click on my icon to see how to interact with me! '

    if process_msg == '$help':
        return "`You can type in the commands below in the channel #bot-commands to interact with Mardo:" \
               " 1. $help -> " "which will make this current message appear` " \
               " 2. hello -> which will give you a welcome message 3. " \
               " ? " "-> to start a private message with Mardo "

#    return "I don't understand what you are saying."
