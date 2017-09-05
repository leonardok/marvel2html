===============================
marvel2html
===============================

Show marvel comic as html


Requirements
------------

In order to run this project you will need:

- Heroku account
- Git
- Marvel API keys (visit https://developer.marvel.com)


Quickstart
----------
::

    $ git clone https://github.com/leonardok/marvel2html.git
    $ heroku create
    $ heroku config:set MARVEL_PRIV_KEY=<marvel private key> MARVEL_PUB_KEY=<marvel pub key>
    $ git push heroku master
    $ heroku open
