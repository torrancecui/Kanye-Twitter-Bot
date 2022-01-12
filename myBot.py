import tweepy
import time

## not best practice just here for simplicity
consumer_key = "moUByhaC0XrSMvFT3zfCQBnXZ"
consumer_secret = "wvqLyBWM9EnE7u2s0qcMLVBeAXm6y95VbKdUuIZZV0acwtcHV2"
access_token = "1423018716321566720-ReNGB2xOPhSDBBbsdr8fpKhFIM55PW"
access_token_secret = "mZCsZOsNzK1K5KYPaaJeqymk59kb6ywiTYpFWGjbOPcsm"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
FILE_NAME = 'last_seen_id.txt'

def whenImInNeed():
    return "when i'm in nEEEEed..."

def iMissTheOldKanye():
    return "straight from the go kanye, chop up the soul kanye, set on his goals kanye, i hate the new kanye, the bad mood kanye, the always rude kanye, spaz in the news kanye.."

def sheBleachedHerAsshole():
    return "and she just bleached her asshole"

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def replyToTweets():

    print("replying.... ")

    # last_seen_id = retrieve_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(tweet_mode = 'extended')

    for mention in mentions:
        # store_last_seen_id(last_seen_id, FILE_NAME)
        if '#shetakemymoney' in mention.full_text.lower():
            api.update_status('@' + mention.user.screen_name + " " + whenImInNeed(), mention.id)
        elif '#imisstheoldkanye' in mention.full_text.lower():
            api.update_status('@' + mention.user.screen_name + " " + iMissTheOldKanye(), mention.id)
        elif '#nowififuckthismodel' in mention.full_text.lower():
            api.update_status('@' + mention.user.screen_name + " " + sheBleachedHerAsshole(), mention.id)
            
        print("replied to @" + mention.user.screen_name)

if __name__ == "__main__":
    try:
        replyToTweets()
    except tweepy.TweepError as e:
        print("all responses sent")
