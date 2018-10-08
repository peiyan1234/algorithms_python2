graph = {} # by a hash table
graph["you"] = ["alice", "bob", "claire"] # the friends of "you"
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque

def search(name):
    search_queue = deque() # Creates a new queue
    search_queue += graph["you"]
    searched = [] # This array is how you keep track of which people you've searched before
    while search_queue: # Whle the queue is not empty
        person = search_queue.popleft() # ... grabs the first person off the queue
        if person_is_seller(person):
            print person + " is a mango seller!"
            return True
        else:
            search_queue += graph[person] # No, they're not. Add all of this person's friends to the search queue
            searched.append(person) # Marks this person as searched
    return False

def person_is_seller(name):
    return name[-1] == 'm' # checks if the person's name ends with the letter m

search("you")
