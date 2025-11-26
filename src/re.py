
def failedStudents(organizedData):
    try:
        failedStud = []
        for rollNo , marks in organizedData.items():
            sub = 0
            for mark in marks:
                if(0 <= mark < 33):
                    sub+=1
            if(3<=sub):
                failedStud.append(rollNo)
        return failedStud
    except:
        print("an internall error occured!! ")

def compartmentStudents(headings , organizedData):
    try:
        subjects = headings[2:].copy()
        reStud = dict()
        for rollNo , marks in organizedData.items():
            comp = 0 #store the count for marks bw 0<=mark<33
            sub = []
            for index in range(len(marks)):
                mark = marks[index]
                if(mark<0):
                    # -1 mark cased : exam not given - reappear in exam 
                    sub.append(subjects[index])
                elif(0<=mark<33):
                    comp += 1
                    sub.append(subjects[index])
                else:
                    pass
            match comp:
                case 0:
                    if(len(sub)==0):
                        #passed students
                        pass
                    else:
                        # re-appear : exam not given students
                        reStud[rollNo] = sub
                case 1|2:
                    #re-appear + comp both students
                    reStud[rollNo] = sub
                case 3:
                    #failed students    
                    pass
        return reStud
    except:
        print("an error occurred !!")