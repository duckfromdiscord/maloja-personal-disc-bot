# maloja-personal-disc-bot

A very, very work-in-progress Discord bot designed to connect to your local Maloja server and provide all the information you want about your scrobbles. Soon, you will also be able to filter out information you don't want.

## Creating `config.py`
```py
prefix = "m!"
discord_api_key = "your Discord bot token"
maloja_endpoint = "http(s)://maloja ip:port"
maloja_apikey = "your maloja api token"
lastfm_apikey = "not used"
lastfm_apisecret = "not used"
user_id = 0000000 #replace with your Discord user id, no quotes
```

## Commands
Your default prefix is `m!`.
- `r`: Shows your most recent scrobble. Functions as a "now playing" command that has some latency.