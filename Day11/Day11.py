with open('testinput.txt') as f:
    testinputtext = f.readlines()
with open('input.txt') as f:
    inputtext = f.readlines()

testinput = []
input = []
for i in range(0,len(testinputtext)):
    testinput.append([])
    input.append([])
    for j in range(0,len(testinputtext[i])):
        c = testinputtext[i][j]
        c2 = inputtext[i][j]
        
        if not c=='\n': testinput[i].append(int(c))
        if not c2=='\n': input[i].append(int(c2))

def part1(input):
    numFlashes = 0
    for d in range(0,100):
        hasFlashed = [[False for j in range(0,len(input[0]))] for i in range(0,len(input))]
        def increment(i,j):
            if i < 0 or i >= len(input) or j < 0 or j >= len(input[i]): return 0
            numFlashes=0
            input[i][j]+=1
            if input[i][j] > 9 and hasFlashed[i][j]==False:
                hasFlashed[i][j]=True
                numFlashes+=1
                numFlashes+=increment(i-1,j-1)
                numFlashes+=increment(i-1,j)
                numFlashes+=increment(i-1,j+1)
                numFlashes+=increment(i,j+1)
                numFlashes+=increment(i+1,j+1)
                numFlashes+=increment(i+1,j)
                numFlashes+=increment(i+1,j-1)
                numFlashes+=increment(i,j-1)
            return numFlashes
            numFlashes+=1
        for i in range(0,len(input)):
            for j in range(0,len(input[i])):
                numFlashes+=increment(i,j)

        for i in range(0,len(input)):
            for j in range(0,len(input[i])):
                if hasFlashed[i][j]: input[i][j] = 0

        # for i in range(0,len(input)):
        #     for j in range(0,len(input[i])):
        #         print(input[i][j],end='')
        #     print("")
        # print("numFlashes: "+str(numFlashes))
    return numFlashes
def part2(input):
    numFlashes = 0
    step = 0
    while True:
        step+=1
        hasFlashed = [[False for j in range(0,len(input[0]))] for i in range(0,len(input))]
        def increment(i,j):
            if i < 0 or i >= len(input) or j < 0 or j >= len(input[i]): return
            input[i][j]+=1
            if input[i][j] > 9 and hasFlashed[i][j]==False:
                hasFlashed[i][j]=True
                increment(i-1,j-1)
                increment(i-1,j)
                increment(i-1,j+1)
                increment(i,j+1)
                increment(i+1,j+1)
                increment(i+1,j)
                increment(i+1,j-1)
                increment(i,j-1)
            return
        for i in range(0,len(input)):
            for j in range(0,len(input[i])):
                increment(i,j)

        hasNotFlashed = False
        for i in range(0,len(input)):
            for j in range(0,len(input[i])):
                if hasFlashed[i][j]: input[i][j] = 0
                if input[i][j] != 0: hasNotFlashed = True

        if not hasNotFlashed:
            return step
    return -1

print("Part 1 test answer: "+str(part1(testinput)))
print("Part 1 answer: "+str(part1(input)))
print("Part 2 test answer: "+str(part2(testinput)))
print("Part 2 answer: "+str(part2(input)))