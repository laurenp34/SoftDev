#links: dictionary containing all the backlinks to each page
#initial_prs: array of initial pr values for each page
#times: iterations of function
def calc_pagerank(outlinks, links, times):
    # links must be same length as outlinks!!!!
    if len(outlinks) != len(links):
        print("Bad input! Links dictionary must be the same length as the outlinks array.")
        return -1
    time = 0
    page = 0
    df = .85
    initial_prs = []
    #get first round of pr values
    #each page's pr in the first round = the # of pages linking to it (backlinks)
    for page in range(len(outlinks)):
        initial_prs.append(len(links[page]))
    page = 0
    for time in range(times):
        cur_vals = []
        #apply page rank multiplier: (PR*(1-D))/#outlinks
        for page in range(len(initial_prs)):
            initial_prs[page] = initial_prs[page]*df/outlinks[page]
        for page in range(len(initial_prs)):
            new_pr=0
            link = 0 #reset vars
            #loop through each backlink to this page (stored in links dict)
            for link in range(len(links[page])):
                #add each backlink's pr to current page's new_pr
                new_pr = new_pr + initial_prs[links[page][link]]
            new_pr = new_pr + 0.15 # add dampening factor
            cur_vals.append(new_pr)
            # ^ important to only update cur_vals this round because we still need initial val for other calculations
        initial_prs = cur_vals
    #get largest pr and round each pr value so it looks pretty
    best = 0
    page = 0
    for page in range(len(cur_vals)):
        cur_vals[page] = round(cur_vals[page],2)
        if cur_vals[page] > cur_vals[best]:
            best = page
    print(str(times)+" iterations ran. Best page is "+str(best)+" with a PageRank of "+str(cur_vals[best])+".")
    return cur_vals




outlinks = [1,1,3,2,1]
links = {0: [2], 1: [2,3], 2: [0,1], 3:[4], 4:[2,3]}

print(calc_pagerank(outlinks,links, 100))
