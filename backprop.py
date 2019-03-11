#!/usr/bin/env python

#-----------------------------------------------------------------------
# backprop.py
# Author: Ikaia Chu
#-----------------------------------------------------------------------

from sys import argv
from os import environ
from time import localtime, asctime, strftime
from urllib import quote_plus
from bottle.ext import beaker
from bottle import route, request, response, error, redirect, run, get
from bottle import template, TEMPLATE_PATH, app

# CAS things
sessionOptions = {
    'session.type': 'file',
    'session.cookie_expires': True,
    'session.data_dir': './data',
    'session.auto': True
}
pawswapApp = beaker.middleware.SessionMiddleware(app(), sessionOptions)

@route('/')
@route('/landingpage')
def landingpage():
    errorMsg = request.query.get('errorMsg')
    if errorMsg is None:
        errorMsg = ''   

    templateInfo = {
    }
    return template('landingpage.html', templateInfo)


@error(404)
def notFound(error):
    return 'Not found'

if __name__ == '__main__':
    # for i in range(1,1000):
    #     print('8===D~~  ( . Y . )')
    #     print
    if len(argv) != 2:
        print 'Usage: ' + argv[0] + ' port required'
        exit(1)
    run(app=pawswapApp, host='0.0.0.0', port=argv[1], debug=True)
