# requirements
import tweepy as tw
# API keys
consumer_key = 'XXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXX'

# authentication
auth = tw.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)
api = tw.API(auth)
client = tw.Client(
    bearer_token='XXXXXXXXXXXXXX')
# opening a file
fo = open("TwitterAPI.txt", "r+")

# lookup tweets by id
fo.write('lookup a tweets by id:'+'\n')
ids = ['1546514661587271683', '1545468528538648576', '1545407365918474242']
tweets = client.get_tweets(ids=ids, tweet_fields=[
                           'context_annotations', 'created_at', 'geo'])
for tweet in tweets.data:
    print(tweet)
    fo.write(str((tweet.text).encode('utf8')))
    fo.write('\n')

# search tweets about cats (-is not including retweets)
fo.write('search tweets about cats(user,tweet):'+'\n')
query1 = 'cat -is:retweet'
tweets = client.search_recent_tweets(query=query1, tweet_fields=['context_annotations', 'created_at'],
                                     expansions='author_id', max_results=100)
# Get users list from the includes object
users = {u["id"]: u for u in tweets.includes['users']}
# print 100 usernames that tweeted about cats
for tweet in tweets.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        print(user)
        print(tweet)
        fo.write(str(user)+'\n')
        fo.write(str((tweet.text).encode('utf8')))
        fo.write('\n')

# search tweets about StarWars not including retweets that has madia
fo.write('search tweets about StarWars(tweet,image url):'+'\n')
query2 = 'StarWars -is:retweet has:media'
tweets = client.search_recent_tweets(query=query2, tweet_fields=['context_annotations', 'created_at'],
                                     media_fields=['preview_image_url'], expansions='attachments.media_keys',
                                     max_results=100)
media = {m["media_key"]: m for m in tweets.includes['media']}
for tweet in tweets.data:
    attachments = tweet.data['attachments']
    media_keys = attachments['media_keys']
    print(tweet.text)
    fo.write(str((tweet.text).encode('utf8')))
    fo.write('\n')
    if media[media_keys[0]].preview_image_url:
        print(media[media_keys[0]].preview_image_url)
        fo.write(str(media[media_keys[0]].preview_image_url)+'\n')

# geting the number of tweets made about python in the last week by day
fo.write('number tweets about python in the last week sorted by day:')
query3 = 'python -is:retweet'
counts = client.get_recent_tweets_count(query=query3, granularity='day')
for count in counts.data:
    print(count)
    fo.write(str(count)+'\n')

# getting a users liked tweets
fo.write('lookup a user\'s liked tweets:'+'\n')
tweets = client.get_liked_tweets("745911914")
for tweet in tweets:
    print(tweet)
    # fo.write(str((tweet.text).encode('utf8')))
    # fo.write('\n') 

# lookup users by id
fo.write('lookup a users by id:'+'\n')
ids = ['706864165143511041', '95675862', '847378752', '995461522359894016']
users = client.get_users(ids=ids)
for user in users.data:
    print(user.username)
    fo.write(str(user.username)+'\n')

# lookup user by username
fo.write('lookup a users by id:'+'\n')
users = client.get_users(usernames='FIFAWorldCup')
for user in users.data:
    print(user.id)
    fo.write(str(user.id)+'\n')

# getting a users followers
fo.write('lookup a user\'s followers(id, username, profile picture URL):'+'\n')
users = client.get_users_followers(
    id='2381578122', user_fields=['profile_image_url'])
for user in users.data:
    print(user.id)
    print(user.username)
    print(user.profile_image_url)
    fo.write(str(user.id)+'\n')
    fo.write(str(user.username)+'\n')
    fo.write(str(user.profile_image_url)+'\n')

# getting a users followings
fo.write('lookup a user\'s followings(username):'+'\n')
users = client.get_users_following(id="963156842598682624",max_results=50)
for user in users.data:
    print(user.username)
    fo.write(str(user.username)+'\n')    
    
# getting a users mention
fo.write('lookup a user\'s mentions:'+'\n')
tweets = client.get_users_mentions(id='3320478908', tweet_fields=[
                                   'context_annotations', 'created_at', 'geo'])
for tweet in tweets.data:
    print(tweet)
    fo.write(str((tweet.text).encode('utf8')))
    fo.write('\n')    

# getting users that liked a tweet, return User id, Name, username
fo.write('lookup users that liked a tweet(user id, name, username):'+'\n')
users = client.get_liking_users(id="1545437932353380354")
for user in users:
    print(user)
    fo.write(str(user)+'\n')
