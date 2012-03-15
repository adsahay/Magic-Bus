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
    
    lastfmuser = request.vars.lastfmuser
    # print 'lastfmuser', lastfmuser
    api_key = os.environ['LASTFM_API_KEY']
    
    url = 'http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=%s&api_key=%s&limit=10' % (lastfmuser, api_key)
    artists = requests.get(url).content
    artists = bss(artists)
    
    artist_names = artists.findAll('name')
    # print artist_names
    
    yt_url = 'http://gdata.youtube.com/feeds/api/videos?q=%s&max-results=1&category=Music&v=2&alt=json'
    yt_list = []
    
    for artist in artist_names:
        a = artist.text.replace(' ', '+')
        # print 'searching: ' + a
        video_json = requests.get(yt_url % a).content
        video = sj.loads(video_json)
        title = video['feed']['entry'][0]['media$group']['media$title']
        yt_video_id = video['feed']['entry'][0]['media$group']['yt$videoid']
        yt_list.append({'title':title['$t'], 'yt_id':yt_video_id['$t']})
        
    return dict(yt_list=yt_list)
    
def error():
    return dict()
