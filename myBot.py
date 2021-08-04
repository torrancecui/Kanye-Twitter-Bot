import tweepy
import time

consumer_key = "moUByhaC0XrSMvFT3zfCQBnXZ"
consumer_secret = "wvqLyBWM9EnE7u2s0qcMLVBeAXm6y95VbKdUuIZZV0acwtcHV2"
access_token = "1423018716321566720-ReNGB2xOPhSDBBbsdr8fpKhFIM55PW"
access_token_secret = "mZCsZOsNzK1K5KYPaaJeqymk59kb6ywiTYpFWGjbOPcsm"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def whenImInNeed():
    return "when i'm in nEEEEed..."

def iMissTheOldKanye():
    return "straight from the go kanye, chop up the soul kanye, set on his goals kanye, i hate the new kanye, the bad mood kanye, The always rude kanye, spaz in the news kanye.."

def replyToTweets():

    mentions = api.mentions_timeline()

    for mention in mentions:
        if '#shetakemymoney' in mention.full_text.lower():
            api.update_status('@' + mention.user.screen_name + whenImInNeed(), mention.id)

if __name__ == "__main__":
    while True:
        time.sleep(15)
        replyToTweets()