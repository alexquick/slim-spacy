## slim spaCy

Heroku's slug size limit is 500MB while a basic spaCy / flask install is 148MB of that. Fortunately, If you only intend on using spaCy for english[^1], you can use the (undocumented?) [post compile](https://github.com/heroku/heroku-buildpack-python/blob/master/bin/steps/hooks/post_compile) hook from the python buildpack to strip out the other languages. This brings it down to 88MB zipped. Good luck.

[^1] https://github.com/explosion/spaCy/issues/2851
