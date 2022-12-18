

def indiv_stats(name,t1,t2,t3,t4,t5):
    stats = []
    stats.append(t1)
    stats.append(t2)
    stats.append(t3)
    stats.append(t4)
    stats.append(t5)
    
    mini = min(stats)
    maxi = max(stats)
    stats.remove(mini)
    stats.remove(maxi)
    avg = sum(stats)/len(stats)
    print("{}'s stats--min: {}, max: {}, avg: {:.1f}".format(name, mini, maxi, avg))
    

indiv_stats("Stan", 34, 34, 35, 31, 29)
indiv_stats("Kyle", 30, 31, 29, 29, 28)
indiv_stats("Cartman", 36, 31, 32, 33, 33)
indiv_stats("Kenny", 33, 32, 34, 31, 35)
indiv_stats("Bebe", 27, 29, 29, 28, 30)


