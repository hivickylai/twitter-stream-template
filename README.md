# Twitter Stream Template

A template for experimenting with the Twitter Streaming API with helpful comments in plain English.  
Uses Python threading and queues to process tweets provided using Twitter's search API.  
Also includes a method of encoding tweets in ASCII to make Python play nice with Windows 10 terminal.

You can find a full overview in [my blog post](https://coffeeattheairport.com/2017/01/06/twitter-streaming-in-python-on-windows-10/), or ask me about it [@vickylaixy](https://twitter.com/vickylaixy).
***

## Requirements  
* __Python__
  * Uses [Twython](https://github.com/ryanmcgrath/twython) (`pip install Twython`)
* __API access credentials__ of your own
  * Register your application and get these from: https://dev.twitter.com/apps
***

Tested with Python 3.5.2