
## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Function Signature

class music_history:

def __init__(self):
    self.tracks = []

def add(self, trackID)

def get_history(self):
    return self.tracks

parameters: initail list, name of track to add into list.

returnd: empty list if no tracks added or list of tracks added.

side effects: upon instantiation empty list made, use add fucntion to add objects(tracks) to the list. 




_Include the name of the function, its parameters, return value, and side effects._


## 3. Create Examples as Tests



given no track is added, track history shows empty 

music_history() => empty list



given a track is added to the tracks list, the track history displays track 

music_history("im still standing_elton john") => "tracklist: im still standing, elton john"



when several tracks are added, the track history displays all the tracks added

music_history("space oddity_david bowie, heartbreak hotel_elvis presley, proud mary_creedance clearwater revival") => tracklist: "space oddity_david bowie, heartbreak hotel_elvis presley, proud mary_creedance clearwater revival"




given a track is already in the list, track history does not show duplicates

music_history("im still standing_elton john, im still standing_elton john" ) => "im still standing_elton john"



## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
