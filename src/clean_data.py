
# marks that are assigned as "Null" were now became -1 : that defines the marks are not given yet
# a student is passed in a sub when he get more than 33 or 33 marks exactly
# a student failed in 3 subjects marks as completly failed in the class 
# a student who got back into 2 subjects max appear for compartment 


def clean_data(raw_data):
    try :
        for i in range(1,len(raw_data)):
            row = raw_data[i]
            for j in range(0,len(row),1):
                match j:
                    case 0:
                        roll_no = row[j]
                        row[j] = int(roll_no)
                    case 1:
                        pass
                    case 2|3|4|5|6:
                        marks = row[j]
                        try :
                            mark = int(marks)
                            row[j] = mark
                        except ValueError :
                            mark = -1
                            row[j] = mark
                        except :
                            print("an error occured ")
            raw_data[i] = row
    except :
        print("unable to clean data!! ")


def analysis_data(clean_data):
    organizedData = {}
    for row in clean_data[1:]:
        roll_no = row[0]
        marks = row[2:]
        organizedData[roll_no] = marks
    return organizedData