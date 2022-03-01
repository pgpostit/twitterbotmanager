#You will need to PIP INSTALL tweepy for this to work and also create a twitter API. Run this on your own machine.
#Packages
import tweepy
import time
from basfunc import title, menu

#Error handling. To not overload twitter public API.
#Ps: sometimes the same sleep time may or not raise the error. Test and change to make your bot work correctly.
def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(2)


#Keys_data input (from twitter API)
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'acess_token'
access_token_secret = 'acess_token_secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()

#Printing your data
title()
print('Your account data:')
print (f'@{user.screen_name}')
print (f'Nickname: {user.name}')
print (f'Followers: {user.followers_count}')
print('-'*20)

#Main program
while True:
    option = menu()
    if option == 1:
        follback = input('Tell the username: ')
        for follower in limit_handle(tweepy.Cursor(api.followers).items()):
            if follower.name == follback:
                print(f'All done! {follower.name} was followed back.')
                follower.follow()
                print('ALL DONE')
                break
    if option == 2:
        search_string = input('Tell specific words to like the tweet: ')
        while True:
            try:
                numberOfTweet = int(input('Tell how much tweets to like: '))
                break
            except:
                print('Please enter a number.')
        for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweet):
            try:
                tweet.favorite()
                print('Liked that tweet')
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
    if option == 3:
        for follower in limit_handle(tweepy.Cursor(api.followers).items()):
            print(follower.name)
        print('All done!')
    if option == 4:
        break