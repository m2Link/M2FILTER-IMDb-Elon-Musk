class script(object):
    START_TXT = """ðð¨..ðð¨..Good evening {}ð
I'm Powerful Auto-Filter Bot You Can Use Me As A Auto-filter in Your Group ....

Its Easy To Use Me; Just Add Me To Your Group As Admin, Thats All, i will Provide Movies There...ð¤

â ï¸More Help Check Help Button Below

Â©ï¸Má´ÉªÉ´á´á´ÉªÉ´á´D BÊ <a href='https://t.me/m2botz'>M2BOT</a>"""
    HELP_TXT = """Hey {}
Here is the Help For My Commands."""
    ABOUT_TXT = """â¯ My Name: <a href='https://t.me/Elon_Musk_M2Bot'>Elon Musk</a>
â¯ Creator: <a href='https://t.me/ask_admin01'>M2</a>
â¯ Support Group: <a href='https://t.me/m2botzsupport'>Click Here</a>
â¯ Update Channel: <a href='https://t.me/m2botz'>Click Here</a>
â¯ Build status: v1.0.1 [ ð±ð´ðð° ]
â¯ Credit : Everyone in this journey
â¯ Quote : The way to get started is to quit talking and begin doing."""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://github.com/EvamariaTG/EvaMaria  

<b>DEVS:</b>
- <a href=https://t.me/ask_admin01>Team M2</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Elon Musk Should Have Admin Privillage.
2. Only Admins Can Add Filters in a Chat.
3. Alert Buttons Have a Limit Of 64 Characters.

<b>Commands and Usage:</b>
â¢ /filter - <code>add a filter in chat</code>
â¢ /filters - <code>list all the filters of a chat</code>
â¢ /del - <code>delete a specific filter in chat</code>
â¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Elon Musk Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Elon Musk supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/Elon_Musk_M2Bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¢ /connect  - <code>connect a particular chat to your PM</code>
â¢ /disconnect  - <code>disconnect from a chat</code>
â¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of tessa

<b>Commands and Usage:</b>
â¢ /id - <code>get id of a specifed user.</code>
â¢ /info  - <code>get information about a user.</code>
â¢ /imdb  - <code>get the film information from IMDb source.</code>
â¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â¢ /logs - <code>to get the rescent errors</code>
â¢ /stats - <code>to get status of files in db.</code>
â¢ /users - <code>to get list of my users and ids.</code>
â¢ /chats - <code>to get list of the my chats and ids </code>
â¢ /leave  - <code>to leave from a chat.</code>
â¢ /disable  -  <code>do disable a chat.</code>
â¢ /ban  - <code>to ban a user.</code>
â¢ /unban  - <code>to unban a user.</code>
â¢ /channel - <code>to get list of total connected channels</code>
â¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â Total Files: <code>{}</code>
â Total Users: <code>{}</code>
â Total Chats: <code>{}</code>
â Used Storage: <code>{}</code> ð¼ðð±
â Free Storage: <code>{}</code> ð¼ðð±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
