import os
import sys

def find_connect(n,cast):
    conn = 0
    try:
        if set(cast[0])&set(cast[1]):        # Convert the list into set and find common actor using intersection
            conn = 1
            actor = list(set(cast[0])&set(cast[1]))
            return "shortest connection = {} , actor/actors = {}".format(conn,actor)
        for i in range(2,n):                 # Check for cast 2 to cast n for shortest connection
            if set(cast[i])&set(cast[0]):
                if set(cast[i])&set(cast[1]):
                    conn = 2
                    return "shortest connection = {} , cast = {}".format(conn,cast[i])
        return "shortest connection > 2 or no connection"
    except:
        return "Please try it again!!"

if __name__ == '__main__':
    with open('input.txt','r') as fl:  # Reading Text file
        cases = int(fl.readline())      # Reading the first line which number of test cases
        while cases:
            n = int(fl.readline())      # Reading the length of list
            cast = [[]]*n               # Creating list of casts
            for i in range(n):
                cast[i] = list(map(str.strip,fl.readline().replace('\n','').split(','))) # Processing each line and store in the list.
            #print(cast)
            print(find_connect(n,cast)) # Calling the function
            cases-=1
        
