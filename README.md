# Work in progress

This is a simple mashup of [Last.fm][1] and [YouTube][2] to demonstrate how [web2py][3] can be used to quickly create a web app prototype from scratch.

## INSTALLATION
===============

(Assuming a GNU/Linux or Mac system, please adapt for Windows.)

1. Download [web2py source][4].
2. Unzip it in the folder of your choice.
3. cd /path/to/web2py/applications
4. git clone git@github.com:adsahay/Magic-Bus.git magicbus
5. Install these python dependencies (either in your main installation or virtual environment). 
        - pip install BeautifulSoup
        - pip install requests
6. export LASTFM_API_KEY='yourapikey' (Get an API key for Last.fm from [here][5]). Without this key we can't fetch data from Last.fm.
7. cd /path/to/web2py 
8. python web2py.py -p 8010
9. Open http://127.0.0.1:8010/magicbus/default/index

## TODO
=======

- Add a "Skip" button/icon/link.
- Better "Loading/Fetching" indicator.

[1]: http://last.fm
[2]: http://www.youtube.com
[3]: http://www.web2py.com
[4]: http://www.web2py.com/examples/static/web2py_src.zip
[5]: http://www.last.fm/api/account
