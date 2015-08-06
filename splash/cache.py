# -*- coding: utf-8 -*-
from __future__ import absolute_import
from PyQt5.QtNetwork import QNetworkDiskCache
from PyQt5.QtNetwork import QNetworkCacheMetaData
from PyQt5.QtCore import QIODevice
from PyQt5.QtNetwork import QNetworkRequest
from twisted.python import log
from splash import defaults
from PyQt5.QtCore import QByteArray


class SplashDiskCache(QNetworkDiskCache):

    def prepare(self, metadata):
        print "-----------"
        print "THIS SHOULD BLOCK CACHING!"
        print metadata.url()
        metadata.setSaveToDisk(True)
        print metadata.saveToDisk()
        metadata.setAttributes(QNetworkRequest.CustomVerbAttribute, QByteArray('GET'))
        metadata.setAttributes(QNetworkRequest.CacheSaveControlAttribute, True)
        print "-----------"
        super(SplashDiskCache, self).prepare(metadata)


    def updateMetaData(self, metadata):
        print "THIS SHOULD BLOCK CACHING FIRST!"
        print "-----------"

    # def insert(self, QIODevice):
    #     print "THIS SHOULD BLOCK INSERTING!"
    #
    #



def construct(path=defaults.CACHE_PATH, size=defaults.CACHE_SIZE):
    log.msg("Initializing cache on %s (maxsize: %d Mb)" % (path, size))
    cache = SplashDiskCache()
    cache.setCacheDirectory(path)
    cache.setMaximumCacheSize(size * 1024**2)
    cache.cacheSize()  # forces immediate initialization
    return cache
