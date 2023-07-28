# Twitter API Python Client

This project provides a Python client for interacting with the Twitter API. It allows you to perform various actions such as searching for tweets, retrieving user information, and accessing tweet analytics. The client utilizes the Tweepy library, which is a widely-used Python wrapper for the Twitter API.

## Requirements

To use this client, you need to have the following:
- Libraries: requests & requests-oauthlib installed
- Tweepy library: You can install it using pip with the command `pip install tweepy`.
- Twitter API keys: You need to obtain API keys from the Twitter Developer Portal. These keys include the consumer key, consumer secret, access token, and access token secret.

## Usage

1. Import the Tweepy library:

```python
import tweepy as tw
```

2. Set up authentication using your API keys:

```python
consumer_key = 'XXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXX'

auth = tw.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tw.API(auth)
client = tw.Client(bearer_token='XXXXXXXXXXXXXX')
```

3. Open a file to write the output:

```python
fo = open("TwitterAPI.txt", "r+")
```

4. Perform actions using the client:

- Lookup tweets by ID:

```python
ids = ['1546514661587271683', '1545468528538648576', '1545407365918474242']
tweets = client.get_tweets(ids=ids, tweet_fields=['context_annotations', 'created_at', 'geo'])
for tweet in tweets.data:
    print(tweet)
    fo.write(str((tweet.text).encode('utf8')))
    fo.write('\n')
```

- Search tweets about any subject e.g. cats (excluding retweets):

```python
query1 = 'cat -is:retweet'
tweets = client.search_recent_tweets(query=query1, tweet_fields=['context_annotations', 'created_at'], expansions='author_id', max_results=100)
users = {u["id"]: u for u in tweets.includes['users']}
for tweet in tweets.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        print(user)
        print(tweet)
        fo.write(str(user)+'\n')
        fo.write(str((tweet.text).encode('utf8')))
        fo.write('\n')
```

- find tweets that have media(excluding retweets) e.g. StarWars:

```python
query2 = 'StarWars -is:retweet has:media'
tweets = client.search_recent_tweets(query=query2, tweet_fields=['context_annotations', 'created_at'], media_fields=['preview_image_url'], expansions='attachments.media_keys', max_results=100)
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
```

- Get the number of tweets made about Python in the last week by day:

```python
query3 = 'python -is:retweet'
counts = client.get_recent_tweets_count(query=query3, granularity='day')
for count in counts.data:
    print(count)
    fo.write(str(count)+'\n')
```

- Get a user's liked tweets:

```python
tweets = client.get_liked_tweets("745911914")
for tweet in tweets:
    print(tweet)
    fo.write(str((tweet.text).encode('utf8')))
    fo.write('\n')
```

- Lookup users by ID:

```python
ids = ['706864165143511041', '95675862', '847378752', '995461522359894016']
users = client.get_users(ids=ids)
for user in users.data:
    print(user.username)
    fo.write(str(user.username)+'\n')
```

- Lookup users by username:

```python
users = client.get_users(usernames='FIFAWorldCup')
for user in users.data:
    print(user.id)
    fo.write(str(user.id)+'\n')
```

- Get a user's followers:

```python
users = client.get_users_followers(id='2381578122', user_fields=['profile_image_url'])
for user in users.data:
    print(user.id)
    print(user.username)
    print(user.profile_image_url)
    fo.write(str(user.id)+'\n')
    fo.write(str(user.username)+'\n')
    fo.write(str(user.profile_image_url)+'\n')
```

- Get a user's followings:

```python
users = client.get_users_following(id="963156842598682624", max_results=50)
for user in users.data:
    print(user.username)
    fo.write(str(user.username)+'\n')
```

- Get a user's mentions:

```python
tweets = client.get_users_mentions(id='3320478908', tweet_fields=['context_annotations', 'created_at', 'geo'])
for tweet in tweets.data:
    print(tweet)
    fo.write(str((tweet.text).encode('utf8')))
    fo.write('\n')
```

- Get users that liked a tweet:

```python
users = client.get_liking_users(id="1545437932353380354")
for user in users:
    print(user)
    fo.write(str(user)+'\n')
```

5. Close the file:

```python
fo.close()
```

## Conclusion

This Python client provides a convenient way to interact with the Twitter API and perform various actions such as searching for tweets, retrieving user information, and accessing tweet analytics. Feel free to explore the different functionalities and customize them according to your needs. Happy coding!
