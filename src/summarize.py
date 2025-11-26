
#this funct reads all data and give us the avg marks for each student in a dict form having the key is roll number and value is avg marks
#the subject which exam were not given by student 'marks marked as -1' were not be taken in calculating avg

def avg_marks(organizedData):
    try:
        avgMarks = dict()
        for rollNo,marks in organizedData.items():
            sub = 0
            total = 0
            for mark in marks:
                if(mark == -1):
                    pass
                else:
                    total += mark
                    sub += 1
            try:
                avg = round(total/sub , 2)
                avgMarks[rollNo] = avg
            except ZeroDivisionError:
                print(f"rollno - {rollNo} has n't appear in a single exam")
        return avgMarks
    except:
        print("an error occured")


def avgMarksClass(avgMarks):
    stud = 0
    total = 0
    for marks in avgMarks.values():
        total += marks
        stud += 1
    try:
        avg = round(total/stud , 4)
        return avg
    except ZeroDivisionError:
        print(f"avgMarks is empty : {avgmarks}")
    except:
        print("an error occured")    
