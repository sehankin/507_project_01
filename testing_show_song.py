import random
import helper_functions

# SI 507 Fall 2017
# Project 1 - Structure & Testing
# Provided cards code

######### DO NOT CHANGE PROVIDED CODE #########

# Very silly. Grabbing the functionality from the helper functions file here.
def show_song(inp="Winner"): # default winner ... but also could be something else if it works correctly, which it does not (put in description and remove this clarity)
    songs_resp = helper_functions.get_and_cache_songs(random.choice(["win","winner","hurrah","hooray"]))
    song_objs = [helper_functions.Song(s) for s in songs_resp["results"]]
    single_song = helper_functions.random_song(song_objs)
    return single_song

## NOTE: if you see a message like so, running this on a Mac computer:
## 0:94: execution error: "https://itunes.apple.com/us/album/bears-adventure/id495954957?i=495955054&uo=4" doesn’t understand the “open location” message. (-1708)
## That's an Apple-related error but will not cause you a problem. Don't worry about it.

########### DO NOT CHANGE CODE ABOVE THIS LINE ###############

#ss = show_song()
ss2 = show_song("Thriller")
