 # -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 23:28:25 2021

@author: leen8
"""
'imports hw4_util functions'
import hw4_util
'creates a function that finds the tuple location of the specified state using enumerate to find the specific indexes\
    and returns the tuple of the specified location'
def find_state_tup(state, ind):
    for i,sub in enumerate(hw4_util.part2_get_week(ind)):
        for j,statef in enumerate(sub):
            if statef == state:
                return (i, j)
    return (None, None)
'prints starting ...'
print("...")
'loops while the function is true'
while True: 
    'gets the index from the user and converts the index into an integer for comparison'
    ind = input("Please enter the index for a week: ")
    print(ind)
    ind = int(ind)
    'determines if it is a valid index, and gets the request from the user and strips \
        it of any spaces'
    if ind >= 1 and ind <=29:
         request = input("Request (daily, pct, quar, high): ")
         print(request)
         req = request.lower().strip()
         'if the request is daily, it gets the specified state from the user and strips it from \
             any spaces, calls the function to get the specified tuple with its list location \
                 with data, if it does not exist it prints the unknown state, if it exists it \
                     calculates and prints the daily positive cases'
         if req == "daily":
            state = input("Enter the state: ")
            print(state)
            state = state.strip()
            statetup = find_state_tup(state, ind)
            if statetup == (None, None):
                print("State {} not found".format(state)+"\n...")
            else:
                stateind = statetup[0]
                wlist = hw4_util.part2_get_week(ind)[stateind]
                daily = ((sum(wlist[2:9])/7)*100000)/wlist[1]
                print("Average daily positives per 100K population: {}".format(round(daily, 1)))
                print("...")
            'if the request is pct, it gets the specified state from the user and strips it from \
             any spaces, calls the function to get the specified tuple with its list location \
                 with data, if it does not exist it prints the unknown state, if it exists it \
                     calculates and prints the average daily percentage of tests that are positive'
         elif req == "pct":
            state = input("Enter the state: ")
            print(state)
            state = state.strip()
            statetup = find_state_tup(state, ind)
            if statetup == (None, None):
                print("State {} not found".format(state)+"\n...")
            else:
                stateind = statetup[0]
                wlist = hw4_util.part2_get_week(ind)[stateind]
                p = sum(wlist[2:9])
                n = sum(wlist[9:])
                pct = p/(p + n)*100
                print("Average daily positive percent: {}".format(round(pct, 1)))
                print("...")
            'if the request is quar, it searches the lists and calculates the average daily percentage \
                of tests that are positive and determines if its higher than 9.5, if it is it adds it to \
                    the list of quarentined states, and sends the states and formats them from hw4_util'
         elif req == "quar":
           states = []
           x = 0
           for x in hw4_util.part2_get_week(ind):
                p = sum(x[2:9])
                n = sum(x[9:])
                i = p/(p + n)*100
                if i >= 9.5:
                    states.append(x[0])
           print("Quarantine states:")
           hw4_util.print_abbreviations(states)
           print("...")
           'if the request is high it searches the list and calculates the daily positive cases, appending \
               all the averages into a list and all of the states into the list, it find the max average \
                   in the list and gets the index of the max and finds the corresponding index in the list \
                       of states and prints the state and the max average'
         elif req == "high":
            savg = []
            states = []
            for x in hw4_util.part2_get_week(ind):
                i = ((sum(x[2:9])/7)*100000)/x[1]
                savg.append(i)
                states.append(x[0])
            max_avg = max(savg)
            m_ind = savg.index(max_avg)
            hstate = states[m_ind]
            print("State with highest infection rate is {}".format(hstate))
            print("Rate is {} per 100,000 people".format(round(max_avg, 1)))
            print("...")
            'prints if the request is not valid'
         else:
            print("Unrecognized request\n...")
            'prints if the index is above the max'
    elif ind>29:
        print("No data for that week\n...")
    else:
        break

        
            
    
    

