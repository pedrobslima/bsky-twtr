import os

def getAllEnv(*args):
    var_list = []
    for var in args:
        var_list.append(os.getenv(var))
    return var_list

def clientPost(bsky_client, tt_client, post:str):
    bsky_response = bsky_client.send_post(text=post)
    print('BlueSky POST response:\n', bsky_response)
    tt_response = tt_client.create_tweet(text=post)
    print('\nTwitter POST response:\n', tt_response)