

def get_response(message: str) -> str:
    process_msg = message.lower()

    if process_msg == 'hello':
        return 'Welcome to Google Developer Student Club @GRC / Competitive Programming Club! I am Mardo the moderator ' \
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
        - [Tony's tutorial](https://common-paste-ea7.notion.site/Content-Topics-1c3b68e1d8894f8b99564fc5efd6836b)
        - [HackerRank](https://www.hackerrank.com/)
        """

    if process_msg == '$events':
        return """
        Here is a list of all upcoming events:
        - First Meeting (in-person) 
        Date: Wednesday Jan 25
        Salish Hall 152
        """

    if process_msg == '$join':
        return """
        Thank you for your interest in joining our club! Please fill out this form to become a member: https://forms.gle/tXvs3t5quB9q3cHF7
        """

    if process_msg == '$contact':
        return """
        If you have any questions or would like to contact us, please dm our discord or ask in the club server. We will get back to you as soon as possible.
        """
    
    if process_msg == '$website':
        return """
        This is our club website, you can find more info there! https://sites.google.com/view/gdscpclub/home
        """

#    return "I don't understand what you are saying."
