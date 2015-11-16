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
            if currentDate not in line:
                continue
            else:
               newJobsList = [linesAfterDate.strip('\n') for linesAfterDate in inFile]
        newJobsList.sort() 

        if currentDate not in inFile.read():
            firstLine = inFile.readline()
            contentList = [companyNames.strip('\n') for companyNames in inFile.readlines()]

            contentList.sort()

    
    if not os.path.exists("D:\Software\Google Drive\Documents\jobs_applied_sorted.txt"):

        with open("D:\Software\Google Drive\Documents\jobs_applied_sorted.txt", 'w') as outFile:
            outFile.write(firstLine + '\n')
            update_count_rejections_and_applied(contentList, rejections, appliedCount, outFile)
            
    elif os.path.exists("D:\Software\Google Drive\Documents\jobs_applied_sorted.txt"):

        if currentDate not in open("D:\Software\Google Drive\Documents\jobs_applied_sorted.txt", 'r').read():

            # Means that text file is updated and should just update the existing file with the new info
            with open("D:\Software\Google Drive\Documents\jobs_applied_sorted.txt", 'a+') as existingFile:
                if currentDate not in existingFile.read():
                    existingFile.write("\n{}\n".format(currentDate))
                    update_count_rejections_and_applied(newJobsList, rejections, appliedCount, existingFile)

            #existingFile.write("\nApplied: {}\n".format(appliedCount))
            #existingFile.write("Rejections: {}".format(rejections))

def update_count_rejections_and_applied(list, rejects, applied, outFile):
    for names in list:
        if('-X' in names):
            rejects += 1
        if '/' not in names:
            if (names != ''):
                outFile.write(names + '\n')
                applied += 1
            
    outFile.write("\nApplied: {}\n".format(applied))
    outFile.write("Rejections: {}".format(rejects))
    
def print_list(inputList):
    for x in inputList:
        print(x)
        
def main():
    #providedFilename = input("Enter fileName: ")
    sort_jobs("jobs_applied.txt")
    

if __name__ == "__main__":
    main()
