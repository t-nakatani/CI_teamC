import tweepy
 
# ---------------------Twitter APIを使うための設定------------------------
# 各種キー、トークンを格納
# 機密情報は別で管理しておく
api_key = '（api_keyをここにかく）'
api_key_secret = '（api_key_secretをここにかく）'
access_token = '（access_tokenをここにかく）'
access_token_secret = '（access_token_secretをここにかく）'
 
# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# -------------------------------------------------------------------

# -------------------この部分をアプリ画面で操作する----------------------------
# 例えば、「大阪」の「グルメ」を知りたいとする

prefecture = '大阪' # ほかに'京都','兵庫','奈良','滋賀'など
purpose = 'グルメ'  # ほかに'観光'など
# -------------------------------------------------------------------

# ---------------------------ハッシュタグ検索------------------------------
query_hashtag = '#' + prefecture + purpose

# q（検索クエリ）で検索するハッシュタグを指定
get_tweets = api.search_tweets(q = query_hashtag, lang = 'ja', count = 50, tweet_mode = 'extended')

tweet_num = 0
for tweet in get_tweets:
    # リツイートの場合、tweetのjsonには、「retweeted_status」というプロパティが含まれる
    # 今回はリツイートは除きたいため、not inでリツイートではないことを判定している
    if ('retweeted_status' not in tweet._json.keys()):
        tweet_num += 1
        print('・' + str(tweet_num) + 'つ目のツイート\n')
        user = tweet.user.screen_name
        print('user : @' + user + '\n')
        print('date : ' + str(tweet.created_at) + ' (UTC) \n')
        print(tweet.full_text + '\n')
        print('favo : ' + str(tweet.favorite_count) + '　retw : ' + str(tweet.retweet_count) + '\n')
        print('=' * 80 + '\n')
        
        # 4件検索
        if (tweet_num == 4):
            break
# -------------------------------------------------------------------