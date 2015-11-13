import os

# Sort jobs applied and count amount of jobs
def sort_jobs(inputFile):
    appliedCount = 0
    rejections = 0

    # Put text file contents into a list to sort
    with open(inputFile, 'r') as inFile:
        firstLine = inFile.readline()
        contentList = [companyNames.strip('\n') for companyNames in inFile.readlines()] 

    # Sort List alphabetically
    contentList.sort()

    with open("D:\Software\Google Drive\Documents\jobs_applied_sorted.txt", 'w') as outFile:
        outFile.write(firstLine + '\n')
        for names in contentList:
            if('-X' in names):
                rejections += 1
            if '/' not in names:
                if (names != ''):
                    outFile.write(names + '\n')
                    appliedCount += 1
                
        outFile.write("\nApplied: {}\n".format(appliedCount))
        outFile.write("Rejections: {}".format(rejections))

    inFile.close()
    outFile.close()
    
def print_list(inputList):
    for x in inputList:
        print(x)
        
def main():
    providedFilename = input("Enter fileName: ")
    sort_jobs(providedFileName + ".txt")
    

if __name__ == "__main__":
    main()
