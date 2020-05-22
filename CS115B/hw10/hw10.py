'''
Created on Nov 13, 2017

@author: bpatton rkim4
I pledge my honor that I have abided by the Stevens Honor System

Brandon Patton
Ronald Kim
'''
from cs115 import map, reduce
import sys

def interface(database):
    '''When the program is started, user is prompted for his/her name, and then asked to enter
    an artist into the system. Then, they are offered several menu options based on the
    assignment given. This user interface will be offered after each operation
    is done until the user selects save and quit by entering 'q'. '''
    username = getUser()
    if username not in database:
        enterPreferences(username, database)
        
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
            database = enterPreferences(username, database)
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

def enterPreferences(username, database):
    '''Allows user to enter his/her preferences when the letter 'e' is entered.
    Prompts the user to enter an artist he/she likes and adds it to his/her 
    preferences in the musicrecplus.txt file. Continues to prompt the user until
    empty string is entered. The user cannot enter the same artist twice.'''
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
    '''Prints the artist that is liked by the most
    users. If there is a tie, prints all artists with the most likes. Users in 
    private mode (with a $ at the end of their name) are excluded from these 
    calculations.'''
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
    
def mostPopular(database):
    '''Prints the number of likes the most popular artist(s) received. 
    Users in private mode (with a $ at the end of their name) are
    excluded from these calculations. In the event of a tie, still only 
    print this number once.  Prints only the number.'''
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
        print('Sorry, no artists found')
    else:
        print(max)    

def mostLikes(database): 
    '''Prints the full name(s) of the user(s) who likes the most artists. User
    names are sorted according to the rule that if a is < than b ( a < b is
    True ) then a is printed before b. Excludes any user whose name ends 
    in a $ from these computations. If there is a tie, prints all tied users. The
    current user is included in this computation'''   
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
        print('Sorry, no user found')
    else:
        list.sort(users_mostLikes)
        printOnePerLine(users_mostLikes)

def save_and_quit(database):
    '''When the user chooses to quit, the current database
    is written to the musicrecplus.txt, replacing old contents (if
    any). If the file exists, its contents are overwritten. If the file doesn't
    exist, it is created with the proper contents.'''
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
    '''Given during review, gets the txt file to be used later. Sets up the 
    database dictionary'''
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
    '''Given during review, saves user's input as his/her username. This is where
    one may make their preferences private or not using the $ symbol'''
    
    print("Enter your name (put a $ symbol if you wish your music preference to remain private):")
    username=input()
    while username == '':
        print("Enter your name (put a $ symbol if you wish your music preference to remain private):")
        username=input()
    return username

def printOnePerLine(iterable):
    '''Given during review, Prints one line of output per line.'''
    for thing in iterable:
        print(thing)      
        
        
def myMap(fn,iterable):
    ret = [0]*len(iterable)
    i=0
    for thing in iterable:
        ret[i]=fn(thing)
        i+=1
    return ret

def getRecs(user,database):
    '''This function was given during the review. The recommendations come from the
    users with the most similarity to the current user.  If there are no differences
    between the user and another client's preferences, that/those client(s) are 
    discarded before similarity is rated. If two or more other clients preferences
    match the user, all the artists not currently liked by the user are included 
    in the result.'''
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
            elif aUser<aOther:
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
    
def main():
    '''Reads in the txt document, if it already exists. Starts up the user
    interface to start the program.'''
    database=readInData()
    interface(database)
main()
