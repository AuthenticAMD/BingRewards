#!/usr/bin/env python3

#
# Dictionary queries generator
# developed by AuthenticAMD (2014)
#

import linecache
from random import randint
from bingRewards import BingRewards

DICT_FILE = "/usr/share/dict/linux.words"

class queryGenerator:
    def __init__(self, br):
        """
        param br is a pointer to the calling class bingRewards (used for variables)
        """
        if br is None or not isinstance(br, BingRewards):
            raise ValueError("br is not set or is not an instance of BingRewards")
        self.bingRewards = br
        
    def __file_len(self, fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

        
    def generateQueries(self, queriesToGenerate, history, maxQueryLen = None):
        """
        Parses /usr/share/dict/words file and generates queries
        from the words in the file.

        param queriesToGenerate the number of queries to return
        param history a set of previous searches
        param maxQueryLen the maximum query length

        returns a set of queries - self.queries
        """
        if queriesToGenerate <= 0:
            raise ValueError("numberOfQueries should be more than 0, but it is %d" % queriesToGenerate)
        if history is None or not isinstance(history, set):
            raise ValueError("history is not set or not an instance of set")

        fileLength = self.__file_len(DICT_FILE)
        
        searchTerms = list()
        
        for x in range(0, 1000):
            ri = randint(1,fileLength - 1)
            searchTerms.append(linecache.getline(DICT_FILE, ri).rstrip())
            
        queries = set()
        queriesNeeded = queriesToGenerate
        while queriesNeeded > 0 and len(searchTerms) > 0:
            # ignore things in your history
            if searchTerms[0] in history:
                del searchTerms[0]
                continue
            queries.add(searchTerms[0])
            del searchTerms[0]
            queriesNeeded -= 1

        return queries
