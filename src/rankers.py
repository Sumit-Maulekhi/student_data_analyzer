
def topPerforming(top , organizedData , avgMarks):
    toppers = dict()
    avg = avgMarks.copy()
    count = 1
    while(count<=top):
        maxi = 0
        max_id = 0
        for rollNo , avgMark in avg.items():
            if(avgMark > maxi):
                maxi = avgMark
                max_id = rollNo
        try:
            marks = organizedData[max_id] 
            if(not marks.count(-1)):
                toppers[max_id] = dict(rank = count , average = maxi)
                count += 1
            avg.pop(max_id)
        except:
            print("you already fetched all rankers data!! remaning students record were not in the data")
    return toppers