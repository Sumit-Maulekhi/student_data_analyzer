
import csv
#csv module is used to work with csv related files

def load_csv(filePath):
    try:
      records = []
      with open(filePath,'r') as fp:
          obj = csv.reader(fp) #this csv reader objects contain each line of file as a list 
          records = list(obj)
      return records
    except FileNotFoundError:
        print("unable to find the file at your given path")
    except:
        print("an error occured")
    else:
        print("data loaded successfully")
      


    