# fake-ai-discord
Troll your friends by pretending to be an AI!

## Installation
### Repository cloning
To clone this repository, simply type in the console:
```
git clone https://github.com/fg817sw751478/fake-ai-discord.git
```
Another way is to just download the zip and extract it.
### Important things
You will need to rename the `.exampleenv` to `.env`. Open the `.env` file in notepad or whatever code editor you use, and copy paste your bot token into the `.env` file.

A provided example would be:
```
BOT_TOKEN="GMEROIGNN95NG4875GNSIO5NG9SE85NRG"
```
*(NOTE, THIS IS NOT A REAL TOKEN AND WILL NOT WORK, PASTE IN THE WORKING TOKEN INSTEAD OF A WRONG ONE)*
## Usage
### Using it for the first time
Add your bot to a server, mention it or reply to it's message to begin. The console will show the user's message and prompt you to respond. In this way, you can pretend to be the AI. Enter in your response, press enter, and it will send.
**Additional bonus:** It will also show that the bot is typing, show a reaction and remove the reaction when a response is provided.
### Change the activity
Go to line 67, and change the string in `name="questions && Responding to them"` to whatever you want. A provided example:
```
name="people"
```
Therefore, the bot's activity would be 'Listening to people'.
### Logging
The bot auto logs data into `logs.txt`. You can change this. The default minimum log level is `INFO`.
### A known issue
A known issue is that if you don't respond fast enough, discord might disconnect from the gateway. I can't really fix it here. It's an issue with the `input()` behaviour.
## Example
```
user#0: [BOT.MENTION] hello ((RESPONSE > Hello there!
```
