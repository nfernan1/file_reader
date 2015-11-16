import os.path, time

# Sort jobs applied and count amount of jobs
def sort_jobs(inputFile):
    appliedCount = 0
    rejections = 0

    # Current Date
    currentDate = time.strftime("%m/%d/%Y")

    # Put text file contents into a list to sort
    with open(inputFile, 'r') as inFile:

       #if currentDate in inFile.read():
        for line in inFile:
            line = line.strip('\n')

            a, r = update_applied_and_rejection_count(line, 1, 1)
            appliedCount += a
            rejections += r
            
            if currentDate not in line:
                continue
            else:
                newJobsList = []
                for linesAfterDate in inFile:
                    linesAfterDate = linesAfterDate.strip('\n')
                    
                    a2, r2 = update_applied_and_rejection_count(linesAfterDate, 1, 1)
                    appliedCount += a2
                    rejections += r2
                    
                    newJobsList.append(linesAfterDate)
                # newJobsList = [linesAfterDate.strip('\n') for linesAfterDate in inFile]
                
                        
        newJobsList.sort() 

        if currentDate not in inFile.read():
            firstLine = inFile.readline()
            contentList = [companyNames.strip('\n') for companyNames in inFile.readlines()]

        contentList.sort()
            
    
    if not os.path.exists("D:\Software\Google Drive\Documents\jobs_applied_sorted.txt"):

        with open("D:\Software\Google Drive\Documents\jobs_applied_sorted.txt", 'w') as outFile:
            outFile.write(firstLine + '\n')
            update_sorted_file(contentList, rejections, appliedCount, outFile)
            
    elif os.path.exists("D:\Software\Google Drive\Documents\jobs_applied_sorted.txt"):

        if currentDate not in open("D:\Software\Google Drive\Documents\jobs_applied_sorted.txt", 'r').read():

            # Means that text file is updated and should just update the existing file with the new info
            with open("D:\Software\Google Drive\Documents\jobs_applied_sorted.txt", 'a+') as existingFile:
                if currentDate not in existingFile.read():
                    existingFile.write("\n{}\n".format(currentDate))
                    update_sorted_file(newJobsList, rejections, appliedCount, existingFile)

                existingFile.write("\nApplied: {}\n".format(appliedCount - 1))
                existingFile.write("Rejections: {}".format(rejections))
        #else:
            

def update_applied_and_rejection_count(line, rCount, aCount):
    ap = 0
    rj = 0
    
    if('-X' in line):
        rj += rCount
    if '/' not in line:
        if (line != ''):
            ap += aCount
    return (ap, rj)
                            
def update_sorted_file(list, rejects, applied, outFile):
    for names in list:
        if '/' not in names:
            if (names != ''):
                outFile.write(names + '\n')
            
def print_list(inputList):
    for x in inputList:
        print(x)
        
def main():
    #providedFilename = input("Enter fileName: ")
    sort_jobs("jobs_applied.txt")
    

if __name__ == "__main__":
    main()
