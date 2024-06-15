<div align="center">
<center><img src="https://raw.githubusercontent.com/tienanh109/TAZ-Discord-Bot/main/image-banner.svg"/></center>
	<!--h1>TAZ Bot</h1-->
	<b>An open source bot by tienanh109</b>
	<br>
	
<img alt="Discord" src="https://img.shields.io/discord/1205813697361215568?label=Discord&style=for-the-badge&logo=discord&color=5865F2&logoColor=white">

[![Version][version-shield]](version-url)
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
</div>

# Introduction
## About TAZ Bot
TAZ Bot is a simple bot with simple yet interesting features.
Includes features for moderators and games
Code by tienanh109 and some other souces

[**Vote for TAZ Bot**](https://top.gg/bot/926795496469704765)

**Prefix**: !


# Install & Setup
Lazy to host **quickly**? [**Quick Deploy**](#quick-deploy) is the best!
## Quick Deploy
[![Run on Repl.it](https://repl.it/badge/github/tienanh109/TAZ-Discord-Bot)](https://replit.com/@tienanh109/TAZ-Discord-Bot?v=1#README.md)
## Set up your own hosting
> NOTES: Ram is 100MB which is the minimum for TAZ Bot! Anything less will cause the bot to crash or run slowly!
### For Windows
#### 1. Download Python
- Go to the official Python website: [python.org](https://www.python.org)
- Click on "Downloads" and select the version of Python you want to install (usually the latest version).
- Download the installer (.exe) file.

#### 2. Install Python
- Open the downloaded installer file.
- Check the box that says "Add Python to PATH" to make Python accessible from the command line.
- Click "Install Now" and follow the prompts to complete the installation.

#### 3. Verify Installation
- Open Command Prompt (CMD).
- Type `python --version` to check the installed Python version.

### For MacOS
#### 1. Download Python
- Go to the official Python website: [python.org](https://www.python.org)
- Click on "Downloads" and select the version of Python you want to install (usually the latest version).
- Download the installer (.pkg) file.

#### 2. Install Python
- Open the downloaded installer file.
- Follow the installation instructions provided by the installer.

#### 3. Verify Installation
- Open Terminal.
- Type `python3 --version` to check the installed Python version.

### For Linux
#### 1. Download Python
- Open your terminal.
- Ensure your package list is up to date by running: `sudo apt update` (for Debian-based systems like Ubuntu) or `sudo yum update` (for Red Hat-based systems).

#### 2. Install Python
- For Debian-based systems (like Ubuntu), run: `sudo apt install python3`
- For Red Hat-based systems (like Fedora), run: `sudo yum install python3`

#### 3. Verify Installation
- Open Terminal.
- Type `python3 --version` to check the installed Python version.

### For Termux and Other Terminal
#### 1. Download Python & Setup
- Open Terminal
- Type
```bash
pkg install python3
```
And run
#### 2. Verify Installation
- Open Terminal.
- Type `python --version` to check the installed Python version.

#### Verify if pip is already installed
- pip is included with Python 3.4 and later. Verify by typing `pip --version` or `pip3 --version` in your command line interface.

***NOTES: [All OS]***
#### If pip is not installed, follow these steps:
- Download `get-pip.py` from [bootstrap.pypa.io](https://bootstrap.pypa.io/get-pip.py).
- Run the following command in your command line interface:
  - `python get-pip.py` or `python3 get-pip.py`.

## Start your bot (Hosting):
### 1. Install some necessary things 
- Download this repo, [click here to download](https://github.com/tienanh109/TAZ-Discord-Bot/archive/refs/heads/main.zip)!
- Unzip file
- Go to your directory
- Open Terminal, run: `pip install -r requirements.txt` to install some **necessary library** for **Python**

### 2. Start your bot
- Replace your token and api key in `.env` file
- Run `python3 main.py` in Terminal and let it run in the background
- Enjoy!
**[NOTES: Create a bot at **discord.dev** and get the token and enable all intents if you haven't already]**

## Quick setup to server
You feel too lazy to **Host Yourself**? No problem, [click here to invite TAZ Bot!](https://discord.com/oauth2/authorize?client_id=926795496469704765&permissions=8&scope=bot).


## List of Commands
<details>
<summary>😎 Moderation (6):</summary>

- `/ban`: User a ban
- `/kick`: Kick a user
- `/timeout`: Timeout a user
- `/removetimeout`: Remove timeout from a user
- `/purge`: Delete a number of messages in the channel
- `/changeusername`: Change the username of a user on the server

</details>

<details>
<summary>🛠️ Server management (10):</summary>

- `/create-channel`: Create a new channel
- `/give_role`: Give the role to a user
- `/slowmode`: Turn on slow mode for channel
- `/create_webhook`: Create a webhook on server
- `/createcategory`: Create a category
- `/removecategory`: Remove a category
- `/createrole`: Create a new role
- `/deleterole`: Create a role
- `/createvoicechannel`: Create a new voice channel
- `/deletevoicechannel`: Delete a voice channel

</details>

<details>
<summary>💻 Statistics / Information (10): </summary>

- `/serverinfo`: View statistics / information about the server
- `/userinfo`: View information about a user
- `/ping`: View bot latency
- `/weather`: Displays the current weather of a city
- `/wikisearch`: Search on Wikipedia
- `/summary`: Return to Wikipedia
- `/wikiurl`: Find a link to a wikipedia
- `/wikirandom`: Random something on Wikipedia
- `/time`: Show time in all continents of the world
- `/google`: Create search links on Google

</details>

<details>
<summary>✨ Funs (12) :</summary>

- `/say`: Tell the bot to say anything
- `/calculate`: A Calculator on a bot (+;-;*;/)
- `/google`: Create quick google search links!
- `/ai-prompt`: Generate content from prompt!!!!
- `/tic`: Play tic tac toe game with friends on your server!
- `/guess`: Guess numbers from 1 to 10
- `/counter`: idk...
- `/meme`: Random and show a meme image
- `/joke`: Tell a random joke
- `/fact`: Say random fun fact
- `/rps`: Play rock paper scissors with bots
- `/8ball`: Ask 8ball a question and let it answer!

</details>

<details>
<summary>💻 For Developer and Owner (5) :</summary>

- `!restart`: Restart bot (Only work at DM and for Owner of bot)
- `/get_ip`: Get the ip of a website
- `/check_port`: Check whether the port of an IP is open or closed
- `/check_status_code`: Check if the website is uptime or downtime
- `/ping_to_website`: Check how many ms it takes to ping a website

</details>

<details>
<summary>🗿 Other (6):</summary>

- `/help`: Show help & all commands
- `/invite`: Show invite link of bot
- `/vote`: Show link to vote for bot (Soon)
- `/info`: Displays information and parameters about the bot
- `/translate`: Translate a text
- `/createembed`: Create an embed

</details>

**NOTES: This is a beta, not everything works yet!**

# Credits:
## How to Contribution?
1. Fork this GitHub repository
2. Make changes
3. Create a pull request

## Reporting Bugs and Making Suggestions
1. Create an issue on this Github Repo
2. Contact me on Discord (Username: @tienanh109)
3. [Join my discord server for support](https://tienanh109.github.io/dc)

## Contributors:
### Code writer:
- **tienanh109** (Main Developer): Write main code for TAZ Bot
- **[TAZ910 Dev Community](https://tienanh109.github.io/dc)** Members (Tester): Be a tester for TAZ Bot
- **jennycute3744** (Hosting Services): The person responsible for operating TAZ Bot's hosting service

### Other sources:
- **Python** - The main coding language of TAZ Bot
- **Pycord** - Main python library used to make bots
- **Pycord Docs** - Research source for source code
- **Pycord Repo** - Understand how Pycord works with examples
- **Github Users** - Provide source code with examples

**And u <3 Thanks for reading this repo ^-^**


This is my passionate open source project. If you refer to it, please credit me. Thanks 💖



[version-shield]: https://img.shields.io/badge/version-1.1.0_beta-purple?style=for-the-badge
[version-url]: https://github.com/tienanh109/TAZ-Discord-Bot
[contributors-shield]: https://img.shields.io/github/contributors/tienanh109/TAZ-Discord-Bot.svg?style=for-the-badge&color=blue
[contributors-url]: https://github.com/tienanh109/TAZ-Discord-Bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/tienanh109/TAZ-Discord-Bot.svg?style=for-the-badge&color=red
[forks-url]: https://github.com/tienanh109/TAZ-Discord-Bot/network/members
[stars-shield]: https://img.shields.io/github/stars/tienanh109/TAZ-Discord-Bot.svg?style=for-the-badge&color=yellow
[stars-url]: https://github.com/tienanh109/TAZ-Discord-Bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/tienanh109/TAZ-Discord-Bot.svg?style=for-the-badge
[issues-url]: https://github.com/tienanh109/TAZ-Discord-Bot/issues
[license-shield]: https://img.shields.io/github/license/tienanh109/TAZ-Discord-Bot.svg?style=for-the-badge&&color=orange
[license-url]: https://github.com/tienanh109/TAZ-Discord-Bot/blob/master/LICENSE
