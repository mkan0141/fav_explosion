from twitter import *
from config import *

def userInput():
    userID = input('userIDを入力してください: ')
    if userID[0] == '@':
        userID.rstrip('@')
    favNum = int(input('favしたいtweetの数を入力してください(最大30): '))
    favNum = min(favNum, 30)
    return userID, favNum

def enableFavorite(tweet):
    if tweet['text'][0] == 'R' and tweet['text'][1] == 'T' and tweet['text'][2] == ' ' and tweet['text'][3] == '@':
        return False
    if tweet['retweeted'] == True or tweet['text'][0] == '@' or tweet['favorited'] == True:
        return False
    return True

def main():
    userID,favNum = userInput()
    
    twitter = Twitter(auth=OAuth(ACCESS_TOKEN,ACCESS_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_KEY_SECRET))
    timelines = twitter.statuses.user_timeline(screen_name = userID,count = 200)
    
    cnt = 0
    for tweet in timelines:
        if cnt == favNum:
            break        
        if enableFavorite(tweet) == True:
            twitter.favorites.create(_id = tweet['id'], entities = False)
            print("tweet id " + str(tweet['id']) + " liked.")
            cnt+=1

    print('total ' + str(cnt) + ' liked')

if __name__ == '__main__':
    main()

    
