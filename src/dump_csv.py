
def avgRecords(avgClassMarks , avgMarks , filePath):
    with open(filePath,'w') as fp:
        fp.write(f'''\n average mark of class were {avgClassMarks}''')
        fp.write("\n\n\n avg marks of each students in the class are as following :- \n\n ")
        fp.write("\tRoll no   :  avg marks \n\n" )
        for rollno , avg in avgMarks.items():
            fp.write(f'\t {rollno}\t\t :\t\t{avg}\n')

def toppersReport(toppers , toppersReportPath):
    try:
        count = len(toppers)
        if(0<count):
            with open(toppersReportPath,'w') as fp:
                fp.write(f'''\n top {count} students are following :-''')
                fp.write('\n\n')
                fp.write('''    Roll no.    Rank    Average   ''') 
                for rollNo , score in toppers.items():
                    fp.write(f'''\n       {rollNo}        {score['rank']}       {score['average']}  ''') 
        else:
            with open(toppersReportPath,'w') as fp:
                fp.write(
                '''
                Their is no records about toppers
                ''')
    except:
        print("unable to write data in toppers.txt file")

def reStudents(filePath , failedStud , compStud):
    try:
        with open(reExam_filePath,'w') as fp:
            fp.write('\n')
            fp.write('failed students roll-no were : ')
            if(len(failedStud)==0):
                fp.write("their is no fail students")
            else:
                for roll in failedStud:
                    fp.write(f'{roll} , ')
            fp.write('\n\n\n')
            fp.write('re-appearing students for compartment as following :- \n\n')
            fp.write('''    Roll no.      :        Subjects    ''')
            for rollNo , subjects in reAppearStud.items():
                fp.write(f'''\n       {rollNo}          :''')
                fp.write('        ')
                for sub in subjects:
                    fp.write(f'''{sub}  , ''')
    except:
        print("unable to write in reExam.txt")
    

def edgeMarks(filePath , highest , lowest):
    try:
        with open(filePath , 'w') as fp:
            fp.write('\n')
            fp.write('top 3 highest marks of the class were :- \n\n')
            fp.write('''   Roll no.      Subject       Mark   \n''')
            for rollNo , score in highest.items():
                fp.write(f'''      {rollNo}     ''')
                for sub,mark in score.items():
                    fp.write(f'''    {sub}        {mark}  \n''')
            fp.write('\n\n')
            fp.write('top 3 lowest marks of the class were :- \n\n')
            fp.write('''   Roll no.      Subject       Mark   \n''')
            for rollNo , score in lowest.items():
                fp.write(f'''      {rollNo}     ''')
                for sub,mark in score.items():
                    fp.write(f'''    {sub}        {mark}  \n''')
    except:
        print("unable to write data in edgeMarks.txt")
    