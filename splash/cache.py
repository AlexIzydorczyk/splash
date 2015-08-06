# -*- coding: utf-8 -*-
from __future__ import absolute_import
from PyQt5.QtNetwork import QNetworkDiskCache
from PyQt5.QtNetwork import QNetworkCacheMetaData
from PyQt5.QtCore import QIODevice
from twisted.python import log
from splash import defaults

class SplashDiskCache(QNetworkDiskCache):

    def prepare(self, metadata):
        print "THIS SHOULD BLOCK CACHING!"
        return 0

    def insert(self, QIODevice):
        print "THIS SHOULD BLOCK INSERTING!"


    def updateMetaData(self, QIODevice):
        print "THIS SHOULD BLOCK CACHING FIRST!"
        return 0


def construct(path=defaults.CACHE_PATH, size=defaults.CACHE_SIZE):
    log.msg("Initializing cache on %s (maxsize: %d Mb)" % (path, size))
    cache = SplashDiskCache()
    cache.setCacheDirectory(path)
    cache.setMaximumCacheSize(size * 1024**2)
    cache.cacheSize()  # forces immediate initialization
    return cache
