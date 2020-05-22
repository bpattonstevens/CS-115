'''
Created on Nov 17, 2017

@author: 

I pledge my honor that I have abided by the Stevens Honor System

Liam King 
Pratim Patel
'''
from cs115 import map, reduce
import sys

'''Just to be safe so u guys actually look through. Ive put some crazy
zainy messages throughout, have fun you two!! I already did the work for u and 
deleted ALL MY DOCTSTRINGS and added the memey ones instead! Dont forgot to put
ur user ids at the top next to author.








what you call trust issues, i call making sure i dont get fucked'''
















'''DELET THIS'''










'''i love cs115!!!!!!!!!!!!1'''


def userInterface(database):
    username = getUser()
    if username not in database:
        enterUserPreferences(username, database)
        
    while True:   
        print('Enter a letter to choose an option:')
        print('e - Enter preferences')
        print('r - Get recommendations')
        print('p - Show most popular artists')
        print('h - How popular is the most popular')
        print('m - Which user has the most likes')
        print('q - Save and quit')

        userInput = input()
       
        if userInput == 'e':
            database = enterUserPreferences(username, database)
        if userInput == 'r':
            getRecs(username, database)
        if userInput == 'p':
            popularArtists(database)
        if userInput == 'h':
            mostPopular(database)
        if userInput == 'm':
            mostLikes(database)
        if userInput == 'q':
            save_and_quit(database)

def enterUserPreferences(username, database):
    database[username] = []
    userInput = input('Enter an artist that you like (Enter to finish): ')
    while userInput != '':
        if userInput in database[username]:
            print('Cannot enter same artist twice')
            userInput = input('Enter an artist that you like (Enter to finish): ')
        else:   
            database[username].append(userInput)
            userInput = input('Enter an artist that you like (Enter to finish): ')
    return database

def popularArtists(database):
    mostPopular = {}
    max = 1
    mostPopular_artists = []
    for user, artists in database.items():
        if user[-1] != '$':
            for i in artists:
                if i in mostPopular:
                    mostPopular[i] += 1
                    if mostPopular[i] > max:
                        max = mostPopular[i]
                else:
                    mostPopular[i] = 1
    if mostPopular == {}:
        print('Sorry, no artists found')
    else:
        for artist, frequency in mostPopular.items():
            if frequency == max:
                mostPopular_artists.append(artist)
        mostPopular_artists.sort() 
        printOnePerLine(mostPopular_artists)     
'''eb'''
def mostPopular(database):
    mostPopular = {}
    max = 1
    for user, artists in database.items():
        if user[-1] != '$':
            for i in artists:
                if i in mostPopular:
                    mostPopular[i] += 1
                    if mostPopular[i] > max:
                        max = mostPopular[i]
                else:
                    mostPopular[i] = 1
    if mostPopular == {}:
        print('No artists found')
    else:
        print(max)    

def mostLikes(database):   
    max = 0
    users_mostLikes = []
    for user, artists in database.items():
        if user[-1] != '$':
            if len(artists) > max:
                max = len(artists)
    for user, artists in database.items():
        if user[-1] != '$':
            if len(artists) == max: 
                users_mostLikes.append(user)
    if users_mostLikes == []:
        print('No user found')
    else:
        list.sort(users_mostLikes)
        printOnePerLine(users_mostLikes)
'''ted cruz died for our sins'''
def save_and_quit(database):
    handle=open("musicrecplus.txt", "w")
    for key, value in sorted(database.items()):
        if value == []:
            s = key + ':\n'
        else:            
            s = key + ':' + reduce(lambda s, t: s + ',' + t, value) +'\n'
            handle.write(s)
    handle.close() 
    sys.exit(0)           

def readInData():
    database={}
    try:
        handle = open("musicrecplus.txt", "r" )
        lines = handle.read().splitlines()
        handle.close()
        for line in lines:
        #print("line: ",line)
            parts=line.split(":")
            name=parts[0]
            artists=parts[1]
            database[name]=sorted(artists.split(","))
        #print(database)
    except:
        return database
    return database
        
def getUser():    
    print("Enter your name (put a $ symbol if you wish your music preference to remain private):")
    username=input()
    while username == '':
        print("Enter your name (put a $ symbol if you wish your music preference to remain private):")
        username=input()
    return username

def printOnePerLine(iterable):
    for thing in iterable:
        print(thing)      
        
def myMap(fn,iterable):
    ret = [0]*len(iterable)
    i=0
    for thing in iterable:
        ret[i]=fn(thing)
        i+=1
    return ret
'''do trees even think?'''
def getRecs(user,database):
    def compare(userArtists,otherArtists,otherUName):
        if otherUName[-1]=='$':
            return -1
        iUser = 0
        iOther = 0
        score =  0
        while iUser<len(userArtists) and iOther<len(otherArtists):
            aUser = userArtists[iUser]
            aOther = otherArtists[iOther]
            if aUser == aOther:
                score+=1
                iUser+=1
                iOther+=1
            elif aUser<aOther:
                iUser+=1
            else:
                iOther+=1
        if len(userArtists)==score == len(otherArtists):
            return -1
        return score
    def diff(userArtists,otherArtists):
        iUser = 0
        iOther = 0
        diffs = []
        while iUser<len(userArtists) and iOther<len(otherArtists):
            aUser = userArtists[iUser]
            aOther = otherArtists[iOther]
            if aUser == aOther:
                iUser += 1
                iOther += 1
            elif aUser<aOther:          '''LOOOOOOOOOOOOOOOOOOL'''
                iUser+=1
            else:
                diffs.append(aOther)
                iOther+=1
                
        if iOther<len(otherArtists):
            diffs.extend(otherArtists[iOther:])
        return diffs
    userArtists=database[user]
    ranked = sorted(myMap(lambda uname: (compare(userArtists, database[uname], uname), uname), database), reverse=True)
    if len(ranked) == 0 or ranked [0][0] == -1:
        print('No recommendations available at this time')
        return
    
    maxScore=ranked[0][0]
    iMax=0
    for results in ranked:
        if maxScore != results[0]:
            break
        iMax+=1
        
    artists=[]
    for i in range(iMax):
        artists.extend(diff(userArtists,database[ranked[i][1]]))
    artists = sorted(artists)
    printOnePerLine(artists)
    #printOnePerLine(ranked)
    #print(diff(userArtists,database[ranked[0][1]]))
'''shmebony'''
def main():
    database=readInData()
    userInterface(database)
main()
'''congrats u fuks, u violated the honor code'''