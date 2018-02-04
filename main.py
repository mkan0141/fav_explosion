from twitter import *
from config import *

def userInput():
    userID = input('userIDを入力してください: ')
    if userID[0] == '@':
        userID.rstrip('@')
    favNum = int(input('favしたいtweetの数を入力してください(最大30): '))
    favNum = min(favNum, 30)
    return userID, favNum

def main():
    userID,favNum = userInput()
    
    twitter = Twitter(auth=OAuth(ACCESS_TOKEN,ACCESS_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_KEY_SECRET))
    timelines = twitter.statuses.user_timeline(screen_name = userID,count = 200)
    
    cnt = 0
    for timeline in timelines:
        if cnt == favNum:
            break
        
        """print(timeline['id'])"""

        if len(timeline['text']) > 4:
            if timeline['text'][0] == 'R' and timeline['text'][1] == 'T' and timeline['text'][2] == ' ' and timeline['text'][3] == '@':
                continue

        if timeline['retweeted'] == False and timeline['text'][0] != '@' and timeline['favorited'] == False:
            twitter.favorites.create(_id = timeline['id'], entities = False)
            print("tweet id " + str(timeline['id']) + " favorite.")
            cnt+=1

        """ debug用
        else:
            if timeline['retweeted'] == True:
                print("false: this tweet is retweeted.")
            if timeline['text'][0] == '@':
                print("false: this tweet is reply.")
            if timeline['favorited'] == True:
                print("false: this tweet has been favorite")
        """

if __name__ == '__main__':
    main()

    
