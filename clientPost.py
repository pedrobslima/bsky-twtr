# ---SETUP---
import os
from dotenv import load_dotenv
from tweepy import Client as TwitterClient
from atproto import Client as BlueskyClient
from utils import *
load_dotenv() # Load environment variables from .env file

BSKY_USERNAME, BSKY_PASSWORD, TWTR_CONSUMER_KEY, TWTR_CONSUMER_SECRET, TWTR_ACCESS_TOKEN, TWTR_ACCESS_TOKEN_SECRET = getAllEnv('BSKY_USERNAME', 'BSKY_PASSWORD', 'TWTR_API_KEY', 'TWTR_API_KEY_SECRET', 'TWTR_ACCESS_TOKEN', 'TWTR_ACCESS_TOKEN_SECRET')

# ---CLIENTS---

bs_client = BlueskyClient()
bs_client.login(BSKY_USERNAME, BSKY_PASSWORD)

tt_client = TwitterClient(
    consumer_key=TWTR_CONSUMER_KEY, consumer_secret=TWTR_CONSUMER_SECRET,
    access_token=TWTR_ACCESS_TOKEN, access_token_secret=TWTR_ACCESS_TOKEN_SECRET
)

# ---POSTING---

post = input('Escreva o post: ') # TODO: Add images. Save all sent posts & their responses

clientPost(bs_client, tt_client, post)