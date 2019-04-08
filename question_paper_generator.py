"""
Author :- CodeAayu(Aayush Ahuja)
Created :- 08.04.2019 17:05 IST
Copyright :- All wrongs reserverd
Language :- Python 3.6.7
"""

def subsetsum(data,num):
    if num < 1:
        return None
    elif len(data) == 0:
        return None
    else:
        if data[0]["Qmarks"] == num:
            return [data[0]["Qid"]]
        else:
            v = subsetsum(data[1:],(num - data[0]["Qmarks"])) 
            if v:
                return [data[0]["Qid"]] + v
            else:
                return subsetsum(data[1:],num)

fileInput = open("test.txt",'r')    """ data must be in the form of txt
file named test.txt comma seperated without spaces in the form of as following
first element is the total number of questions(let x), next 3*x elements should
be Question id, question level(easy, medium, hard) and Question marks respectively.
Then it should contain total marks needed and then the percentage of easy, medium
and hard marks in question paper respectively. Sample data file is attached.
"""
readFile = str(fileInput.read()).split(',')

numberOfQuestions = int(readFile[0])

sliceQuestion = slice(1,numberOfQuestions*3+1)
questionData = readFile[sliceQuestion]

questionBankE = []
questionBankH = []
questionBankM = []
questions = {}

for i in range(numberOfQuestions):
    questions["Qid"] = questionData[3*i]
    questions["level"] = questionData[3*i+1]
    questions["Qmarks"] = int(questionData[3*i+2])
    if questions["level"]=='easy':
        questionBankE.append(questions.copy())
    if questions["level"]=='hard':
        questionBankH.append(questions.copy())
    if questions["level"]=='medium':
        questionBankM.append(questions.copy())

totalMarks = int(readFile[numberOfQuestions*3+1])

percentageEasy = int(readFile[numberOfQuestions*3+2].split(" ")[1])
percentageMedium = int(readFile[numberOfQuestions*3+3].split(" ")[1])
percentageHard = int(readFile[numberOfQuestions*3+4].split(" ")[1])

easyMarks = int(percentageEasy/100*totalMarks)
mediumMarks = int(percentageMedium/100*totalMarks)
hardMarks = int(percentageHard/100*totalMarks)

easyQuestions = subsetsum(questionBankE,easyMarks)
mediumQuestions = subsetsum(questionBankM,mediumMarks)
hardQuestions = subsetsum(questionBankH,hardMarks)

finalQuestionPaper = []
finalQuestionPaper.extend(easyQuestions)
finalQuestionPaper.extend(mediumQuestions)
finalQuestionPaper.extend(hardQuestions)

for question in finalQuestionPaper:
    print(question)