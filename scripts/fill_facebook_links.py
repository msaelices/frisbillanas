#!/usr/bin/env python

import getpass
import gspread
import facebook
import warnings

# Keep Facebook settings like APP_ID
FACEBOOK_APP_ID = '604710619655090'
FACEBOOK_APP_SECRET = 'b52b4c2330971eba6488993bfacf7876'
REFERENCE_FRIENDS_IDS = (
    '100002340416595',  # Lin
)

# Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
warnings.filterwarnings('ignore', category=DeprecationWarning)

if __name__ == '__main__':

    # Login with your Google account
    oauth_access_token = raw_input('Facebook access token (you can get it in https://developers.facebook.com/tools/explorer/): ')
    facebook_graph = facebook.GraphAPI(oauth_access_token)
    # email = raw_input('Google E-mail: ')
    email = 'msaelices@gmail.com'
    password = getpass.getpass('Password: ')
    gc = gspread.login(email, password)
    key = '1G3TcHDkY6YOEQyBFbtfMqME9nwl3JA_7syc1i97hWiw'
    # key = raw_input('Spreadsheet key (copy-paste from the browser. Should be an key like 1G3TcHDkY6YOEQyBFbtfMqME9nwl3JA_7syc1i97hWiw): ')
    # Open a worksheet from spreadsheet with one shot
    spreadsheet = gc.open_by_key(key)
    sheet = spreadsheet.sheet1
    # get all the names and surnames
    names = sheet.col_values(8)
    surnames = sheet.col_values(9)

    for name, surname in zip(names, surnames):
        full_name = '%s %s' % (name, surname)
        searched_users = facebook_graph.request('search', {'q': full_name.encode('utf-8'), 'type': 'user'})['data']

        if searched_users:
            for user_data in searched_users:
                for reference_id in REFERENCE_FRIENDS_IDS:
                    is_friend = facebook_graph.request('%s/friends/%s' % (reference_id, user_data['id']))['data']
                if is_friend:
                    obj = facebook_graph.get_object(user_data['id'])
                    print 'User located: %s' % obj

