
def achievers(headings , organizedData):

    subjects = headings[2:]
    output = []
    
    max1 = max2 = max3 = 0
    max1_id = max2_id = max3_id = []
    min1 = min2 = min3 = 100
    min1_id = min2_id = min3_id = []
    
    for rollNo , marks in organizedData.items():
        for index in range(len(marks)):
            mark = marks[index]
            if(max1<=mark):
                max3 = max2
                max3_id = max2_id.copy()
                max2 = max1
                max2_id = max1_id.copy()
                max1 = mark
                max1_id = [rollNo , index]
            if(-1<mark<min1):
                min3 = min2
                min3_id = min2_id.copy()
                min2 = min1
                min2_id = min1_id.copy()
                min1 = mark
                min1_id = [rollNo,index]
    
    
    maxi = dict()

    max_sub1 = subjects[max1_id[1]]
    maxi[max1_id[0]] = {}
    maxi[max1_id[0]][max_sub1] = max1

    max_sub2 = subjects[max2_id[1]]
    maxi[max2_id[0]] = {}
    maxi[max2_id[0]][max_sub2] = max2

    max_sub3 = subjects[max3_id[1]]
    maxi[max3_id[0]] = {}
    maxi[max3_id[0]][max_sub3] = max3

    mini = dict()

    min_sub1 = subjects[min1_id[1]]
    mini[min1_id[0]] = {}
    mini[min1_id[0]][min_sub1] = min1

    min_sub2 = subjects[min2_id[1]]
    mini[min2_id[0]] = {}
    mini[min2_id[0]][min_sub2] = min2

    min_sub3 = subjects[min3_id[1]]
    mini[min3_id[0]] = {}
    mini[min3_id[0]][min_sub3] = min3

    output = [maxi,mini]
    return output

    