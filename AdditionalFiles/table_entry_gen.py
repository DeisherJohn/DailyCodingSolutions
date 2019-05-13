ProblemSummery = list()
detailList = list()


with open("problem_titles.txt", "r") as f:
    for line in f:
        ProblemSummery.append(line)

with open("details_pages.txt", "r") as f:
    for line in f:
        detailList.append(line)

gitPyPath = "https://github.com/DeisherJohn/DailyCodingSolutions/blob/master/PythonSolutions/p"
gitCppPath = "https://github.com/DeisherJohn/DailyCodingSolutions/blob/master/CppSolutions/p"
pathDetail = "[Link](https://deisherjohn.github.io/DailyCodingSolutions/"
with open("problemIndexTable.txt", "w+") as f:
    for i, problem in enumerate(ProblemSummery, 1):

        pNum = str(i)

        if i < 10:
            pNum = '0'+pNum

        if i < 100:
            pNum = '0'+pNum

        textString = "| " + pNum + " | "  + ProblemSummery[i-1][:-1] + " | [p" + pNum + ".py](" + gitPyPath + pNum + ".py)/[p" + pNum + ".cpp](" + gitCppPath + pNum + ".cpp)|"
        if detailList[i-1] is not '\n':
            textString += pathDetail + detailList[i-1][:-1] + ")"
        textString += "|"
        
        f.write(textString + '\n')