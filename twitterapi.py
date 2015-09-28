import twitter
import random
import time


api = twitter.Api(consumer_key='IbzjJgrFxWlAPGmAxReBXXnig',
                      consumer_secret='Chp1K0zjPFFOje6w0zJ1UGtCkSXm6DVjnXvbmlBu4UyiQpFoww',
                      access_token_key='103594875-b227JLfEAfQz34dfSXFjrUxDT9J36JDxZzhNstwh',
                      access_token_secret='kAcisrslYUSiP0Zv9rupSiqWiOStSNMiFEtQORZj0ePBs')





'''
statuses = api.GetUserTimeline(screen_name='StationCDRKelly')

for s in statuses:
    print s.text 
'''


#Dictionary of data

data = {}

#status = api.PostUpdate('Testing Twitter API through python-twitter')



f = open('data.txt','r')



l = list(f)

f.close()

print len(l)



for i in range(50000):

    target = open('output.txt', 'a')
    userid = l[i]
    exUser = False

    print(userid)

    counter = 0
    #number of users from the US
    userUsP = 0

    #number of users with more than 4,000 followers
    followerP = 0

    #number of users with more than 500 friends
    friendP = 0

    #number of Exception User
    exUser = 0
    #Twitter 





    try:
        user = api.GetUser(user_id = userid)
        followerCount = user.GetFollowersCount()
        friendCount = user.GetFriendsCount()
        timezone = user.GetTimeZone()
        if (timezone == 'Pacific Time (US & Canada)' or timezone=='Central Time (US & Canada)' or timezone == 'Eastern Time (US & Canada)'):
            #userUsP += 1
            US = True
        else:
            US = False
        if followerCount > 4000:
            followerP += 1
        if friendCount > 500:
            friendP += 1

        counter += 1
        target.write('%d %d %d %d %d' % (counter,US,followerCount,friendCount,exUser))
        target.write("\n")
        l.remove(userid)

        time.sleep(5)

    except:
        #exUser += 1
        exUser = True

    target.close()
    
'''

'''




#stat = twitter.user('Dino Xie')