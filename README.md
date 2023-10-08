# fake-ai-discord
Troll your friends by pretending to be an AI!

## Installation
### Repository cloning
To clone this repository, simply type in the console:
```
git clone https://github.com/fg817sw751478/fake-ai-discord.git
```
Another way is to just download the source code and extract it.
### Important things
You need to install the packages, which is done by doing:
```
pip install -r requirements.txt
```
Next, you will need to rename the `.exampleenv` to `.env`. Open the `.env` file in notepad or whatever code editor you use, and copy paste your bot token into the `.env` file.

A provided example would be:
```
BOT_TOKEN="GMEROIGNN95NG4875GNSIO5NG9SE85NRG"
```
*(NOTE, THIS IS NOT A REAL TOKEN AND WILL NOT WORK, PASTE IN THE WORKING TOKEN INSTEAD OF A WRONG ONE)*

Next, you have to set your user id so the bot DMs you and you can give a response. The response will be forwarded as the AI's answer to another user's question.
## Usage
### Using it for the first time
Add your bot to a server, mention it or reply to it's message to begin. The bot will DM your user and wait for a response.
**Additional bonus:** It will also show that the bot is typing, show a reaction and remove the reaction when a response is provided. You can use unicode for an emoji, or a custom emoji *(which is already specified by default in `.env`.)*
### 
### Change the activity
Go to line 67, and change the string in `name="questions && Responding to them"` to whatever you want. A provided example:
```
name="people"
```
Therefore, the bot's activity would be 'Listening to people'.
### Logging
The bot auto logs data into `logs.txt`. You can change this. The default minimum log level is `INFO`.
### Default timeout
The default timeout for the bot is 60 seconds before it tells the user an 'error' occured, meaning you have to type fast and so that users don't suspect why it takes so long to write a message. You can set it to never or any timeout. The error message is also configurable.
## Example
```
INFO - An user has interacted with the bot (fg817sw751478#0 replying to Artificial Intelligence#8198: @Artificial Intelligence hello)
fg817sw751478 — @Artificial Intelligence hello
DM USER ID - USER RESPONDS (Hello there!)
Artificial Intelligence — Hello there!
```
![image](https://github.com/fg817sw751478/fake-ai-discord/assets/147082067/0c09826a-997c-450f-9db8-4bcc02f72d62)
