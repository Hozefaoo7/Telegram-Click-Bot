# Telegram-Click-Bot
Python script to automate clicking of links from cryptocurrency earning bots on telegram.
The script supports @Litecoin_click_bot, @Zcash_click_bot, @BCH_clickbot, @BitcoinClick_bot, @Dogecoin_click_bot.


## Requirements
* telethon
* requests
* beautifulsoup

## How to use the script
1. Before running the script for the first time, you need to edit the script:
   - Uncomment the bot of you want automate. For example
   ```sh
    namer='@Litecoin_click_bot'
   ```

      - Fill in your phone number in international format
   ```sh
    phone_number= '+23400000001'
   ```
      - Fill in your api_id and api_hash. You can get yours [ here ](https://core.telegram.org/api/obtaining_api_id)
   ```sh
    api_id = 00000#'id is an interger'
    api_hash = 'hash is a string'
   ```
2. Script is ran from the command line with the following optional commands
   ```sh
   $ python Telegram_Click_Bot_Script.py check auth cache inf
   ```
      * `check` used to check if user is signed in on the current device.
      * `auth` used to authourise/login user
      * `cache` needed to store channel id and hash to avoid authorising each time a user runs the script as this could lead to flood wait errors on the telegram api.
      * `inf` ensures the script keeps running unless user manually terminates the program
3. When asked for your code, go to your telegram app and copy the code sent to you from telegram
4. After the first time setting up the script and logging in on the device, never use `auth` again unless you get logged out. Always use `check` to see if you are still logged in.
![screenshot](https://github.com/yande-eghosa/Telegram-Click-Bot/raw/master/IMG-20201127-WA0025.jpg)
## Licence
MIT
