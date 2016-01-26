# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 22:03:45 2016

@author: prcobol
"""

import requests

class Actor():
    def __init__(self,first_name=None,last_name=None):
        self.first_name = first_name
        self.last_name = last_name

class Movie():
    def __init__(self,title=None,rating=None,votes=None,actors=None):
        self.title = title
        self.rating = rating
        self.votes = votes
        self.actors = self.convertActorString(actors)
    
    def convertActorString(self, actors):
        actors = actors.split(",")
        arr = []
        for e in actors:
            if e[0] == " ":
                del(e[0])
            e = e.split(" ")
            e = Actor(e[0],e[1])
            arr.append(e)
        return arr

def buildURL(id_num):
    return "http://www.omdbapi.com/?i=tt" + str(id_num)


movies = []
for i in range(4000000,4001000):
    data = requests.get(buildURL(i))
    data = data.json()
    if data['Response'] and 'Type' in data:
        if data['Type'] == "movie":
            if data['Rating'] > 6:
                movies.append(Movie(data['Title'],data['imdbRating'],data['imdbVotes'],data['Actors']))
                print data['Title']
#        
#for e in movies:
#    if e.rating > 9:
#        print e
#    