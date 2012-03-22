# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

def index():
    return dict()

def play():
    import os, requests
    from BeautifulSoup import BeautifulStoneSoup as bss
    import gluon.contrib.simplejson as sj
    import random

    session.forget()
    lastfmuser = request.vars.lastfmuser
    # print 'lastfmuser', lastfmuser
    api_key = os.environ['LASTFM_API_KEY']
    
    url = 'http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=%s&api_key=%s&limit=20' % (lastfmuser, api_key)
    artists = requests.get(url).content
    artists = bss(artists)
    
    artist_names = artists.findAll('name')
    random.shuffle(artist_names, random.random)
    print artist_names
    
    yt_url = 'http://gdata.youtube.com/feeds/api/videos?q=%s&max-results=5&category=Music&v=2&alt=json'
    yt_list = []
    
    for artist in artist_names:
        a = artist.text.replace(' ', '+')
        # print 'searching: ' + a
        video_json = requests.get(yt_url % a).content
        video = sj.loads(video_json)
        # randomly pick one
        index = random.randint(0,4)
        title = video['feed']['entry'][index]['media$group']['media$title']
        yt_video_id = video['feed']['entry'][index]['media$group']['yt$videoid']
        yt_list.append({'title':title['$t'], 'yt_id':yt_video_id['$t']})
        
    return response.json({'yt_list':yt_list})
    
def error():
    return dict()
