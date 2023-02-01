from argparse import ArgumentParser
from requests import post as requests_post
from os import environ as env
from dotenv import load_dotenv
from time import sleep

# Load environment variables from .env file
load_dotenv()

parse = ArgumentParser()

# Define the target URL and form data
sub_url = 'https://steamcommunity.com/sharedfiles/subscribe'
unsub_url = 'https://steamcommunity.com/sharedfiles/unsubscribe'

# get workshop ids from .env file, split by space
ids = env.get('STEAM_WORKSHOP_ID').split(' ')

# get form data from .env file
form_data = {
    'appid': env.get('STEAM_APP_ID'),
    'sessionid': env.get('STEAM_SESSION_ID'),
}

# get cookies from .env file
cookies = {
    'sessionid': env.get('STEAM_SESSION_ID'),
    'steamLoginSecure': env.get('STEAM_LOGIN_SECURE'),
}

# get delay time from .env file
delay_time = env.get('STEAM_DELAY_TIME', 0)


# Make a POST request to the target URL with the form data
def post(url, w_id):
    form_data['id'] = w_id
    return requests_post(url, data=form_data, cookies=cookies)


def subscribe(w_id):
    return post(sub_url, w_id)


def unsubscribe(w_id):
    return post(unsub_url, w_id)


if __name__ == '__main__':
    try:
        # get flags from command line
        # if -a flag is present, override the app id
        # if -s flag is present, override the session id
        # if -l flag is present, override the login secure
        # if -d flag is present, override the delay time

        parse.add_argument('workshop_id', type=str, nargs='*', help='Workshop id')
        parse.add_argument('-a', '--appid', help='Override the app id')
        parse.add_argument('-s', '--sessionid', help='Override the session id cookie')
        parse.add_argument('-l', '--loginsecure', help='Override the steam login secure cookie')
        parse.add_argument('-d', '--delay', help='Override the delay time between requests')
        args = parse.parse_args()

        # override environment variables if flags are present
        if args.workshop_id:
            ids = args.workshop_id
        if args.appid:
            form_data['appid'] = args.appid
        if args.sessionid:
            cookies['sessionid'] = args.sessionid
        if args.loginsecure:
            cookies['steamLoginSecure'] = args.loginsecure
        if args.delay:
            delay_time = int(args.delay)

        # get args from command line
        for workshop_id in ids:
            # Check the response status code to see if the request was successful
            resp = unsubscribe(workshop_id)
            if resp.status_code == 200:
                print(f'Un-subscription for {workshop_id} successful.')
                sleep(delay_time)
                resp = subscribe(workshop_id)
                if resp.status_code == 200:
                    print(f'Subscription for {workshop_id} successful.')
                else:
                    print(f'Subscription failed. Response code: {resp.status_code}\n{resp.text}')
            else:
                print(f'Un-subscription failed. Response code: {resp.status_code}\n{resp.text}')
    except KeyboardInterrupt:
        print('Exiting...')
