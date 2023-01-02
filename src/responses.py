

def get_response(message: str) -> str:
    process_msg = message.lower()

    if process_msg == 'hello':
        return 'Welcome to Google Student Developer Club@GRC/competitive programming club! I am Mardo the moderator ' \
               'bot for this club, click on my icon to see how to interact with me! '

    if process_msg == '$help':
        return """
        **`You can type in the commands below in the channel #bot-commands to interact with Mardo:`**
        `1. $help -> which will make this current message appear`
        `2. hello -> which will give you a welcome message`
        `3. ?hello -> to start a private message with Mardo`
        `4. $resources -> to get a list of useful programming and tech resources`
        `5. $events -> to get a list of upcoming events`
        `6. $join -> to get information on how to join our club`
        `7. $contact -> to get information on how to contact us`
        """

    if process_msg == '$resources':
        return """
        Here are some useful resources for programming and tech:
        - [Insert resource 1]
        - [Insert resource 2]
        - [Insert resource 3]
        """

    if process_msg == '$events':
        return """
        Here is a list of all upcoming events:
        - [Insert event 1] (Date: [Insert date])
        - [Insert event 2] (Date: [Insert date])
        - [Insert event 3] (Date: [Insert date])
        """

    if process_msg == '$join':
        return """
        Thank you for your interest in joining our club! Please fill out this form to become a member: [Insert link to form]
        """

    if process_msg == '$contact':
        return """
        If you have any questions or would like to contact us, please email us at [Insert email address]. We will get back to you as soon as possible.
        """

#    return "I don't understand what you are saying."
