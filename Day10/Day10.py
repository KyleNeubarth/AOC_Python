import math

with open('testinput.txt') as f:
    testinput = f.readlines()
with open('input.txt') as f:
    input = f.readlines()

def part1(input):
    errorSum=0
    for line in input:
        unresolved = ""
        for i in range(0,len(line)):
            print(unresolved)
            if line[i]== '(' or line[i] == '[' or line[i] == '{'or line[i] == '<':
                unresolved+=line[i]
                continue
            if len(unresolved)== 0:
                errorSum+=errorVal(line[i])
                break
            if unresolved[len(unresolved)-1] == '(' and line[i] == ')':
                unresolved = unresolved[0:len(unresolved)-1]
                continue
            if unresolved[len(unresolved)-1] == '[' and line[i] == ']':
                unresolved = unresolved[0:len(unresolved)-1]
                continue
            if unresolved[len(unresolved)-1] == '{' and line[i] == '}':
                unresolved = unresolved[0:len(unresolved)-1]
                continue
            if unresolved[len(unresolved)-1] == '<' and line[i] == '>':
                unresolved = unresolved[0:len(unresolved)-1]
                continue
            errorSum+=errorVal(line[i])
            print("line num: "+str(i))
            print("issue: "+line[i])
            print("errorval: "+str(errorVal(line[i])))

            print("errorsum: "+str(errorSum))
            break
    return errorSum

def part2(input):
    scoreList = []
    for line in input:
        unresolved = ""
        error = False
        for i in range(0,len(line)):
            print(unresolved)
            if line[i] == '\n': continue
            if line[i]== '(' or line[i] == '[' or line[i] == '{'or line[i] == '<':
                unresolved+=line[i]
                continue
            if len(unresolved)== 0:
                error = True
                break
            if unresolved[len(unresolved)-1] == '(' and line[i] == ')':
                unresolved = unresolved[0:len(unresolved)-1]
                continue
            if unresolved[len(unresolved)-1] == '[' and line[i] == ']':
                unresolved = unresolved[0:len(unresolved)-1]
                continue
            if unresolved[len(unresolved)-1] == '{' and line[i] == '}':
                unresolved = unresolved[0:len(unresolved)-1]
                continue
            if unresolved[len(unresolved)-1] == '<' and line[i] == '>':
                unresolved = unresolved[0:len(unresolved)-1]
                continue
            error = True
            break
        print("error"+str(error))
        if error == False:
            print("hello?")
            completeSum=0
            for i in range(len(unresolved)-1,-1,-1):
                print(str(completeVal(unresolved[i])))
                completeSum=completeSum*5+completeVal(unresolved[i])
                print(completeSum)
            print("this line got a complete sum of "+str(completeSum))
            scoreList.append(completeSum)
    scoreList = sorted(scoreList)
    for i in scoreList:
        print(i)
    return scoreList[math.floor((len(scoreList)/2))]

def completeVal(c):
    match c:
        case '(':
            return 1
        case '[':
            return 2
        case '{':
            return 3
        case '<':
            return 4
        case _:
            return 0

def errorVal(c):
    match c:
        case ')':
            return 3
        case ']':
            return 57
        case '}':
            return 1197
        case '>':
            return 25137
        case _:
            return 0
# print("Part 1 test answer: "+str(part1(testinput)))
# print("Part 1 answer: "+str(part1(input)))
print("Part 2 test answer: "+str(part2(testinput)))
print("Part 2 answer: "+str(part2(input)))
