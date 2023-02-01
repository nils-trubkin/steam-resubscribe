# steam-resubscribe

![Demo gif](https://raw.githubusercontent.com/nils-trubkin/steam-resubscribe/master/demo.gif)

## Description
Simple python script to unsubscribe and resubscribe to one or more steam workshop items.
Useful if you want to update a mod without having to manually unsubscribe and resubscribe to it with the steam client.

## Requirements
- Python 3
- requests
- python-dotenv

## Installation
```
git clone git@github.com:nils-trubkin/steam-resubscribe.git
cd steam-resubscribe
pip install -r requirements.txt
```

## Usage
### Alternative 1: Use with env file
Create a file called `.env` in the same directory as the script and fill it with the following content:
```
STEAM_APP_ID="<your steam app id>"
STEAM_WORKSHOP_ID="<your steam workshop id>" (separate multiple ids with a space)
STEAM_SESSION_ID="<your steam session id>" (get it from your browser cookies, it's the value of the "sessionid" cookie)
STEAM_LOGIN_SECURE="<your steam login secure>" (get it from your browser cookies, it's the value of the "steamLoginSecure" cookie)
STEAM_DELAY="<delay between requests in seconds>" (optional, default is 0)
```
Then run the script with the following command:
```
python resubscribe.py
```

### Alternative 2: Use with command line arguments
```
python resubscribe.py [-a|--appid] [-s|--sessionid] [-l|--loginsecure] [-d|--delay] [workshop id ..]
```
