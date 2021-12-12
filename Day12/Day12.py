with open('testinput.txt') as f:
    testinput = f.readlines()
with open('input.txt') as f:
    input = f.readlines()

def part1(input):
    nodes = {}
    for s in input:
        halved = s.strip().split("-")
        if not halved[0] in nodes.keys():
            nodes[halved[0]] = set()
        nodes[halved[0]].add(halved[1])
        if not halved[1] in nodes.keys():
            nodes[halved[1]] = set()
        nodes[halved[1]].add(halved[0])

    def findPaths(node, oldIllegal, oldPath):
        path=list(oldPath)
        illegal=set(oldIllegal)
        path.append(node)
        if node=="end": 
            #print(path)
            return 1
        if node.islower(): illegal.add(node)
        numPaths=0
        for n in nodes[node]:
            if not n in illegal:
                numPaths+=findPaths(n,illegal,path)
        return numPaths

    numPaths=findPaths("start",set(),[])
    return numPaths

def part2(input):
    nodes = {}
    for s in input:
        halved = s.strip().split("-")
        if not halved[0] in nodes.keys():
            nodes[halved[0]] = set()
        nodes[halved[0]].add(halved[1])
        if not halved[1] in nodes.keys():
            nodes[halved[1]] = set()
        nodes[halved[1]].add(halved[0])

    def findPaths(node, oldIllegal, oldPath):
        path=list(oldPath)
        illegal=dict(oldIllegal)
        path.append(node)
        if node=="end": 
            #print(path)
            return 1
        if node.islower() and node != "start":
            if not node in illegal:illegal[node]=0
            illegal[node]+=1
        numPaths=0
        for n in nodes[node]:
            if n=="start":continue
            if not 2 in illegal.values():
                numPaths+=findPaths(n,illegal,path)
            elif not n in illegal:
                numPaths+=findPaths(n,illegal,path)
        return numPaths

    numPaths=findPaths("start",{},[])
    return numPaths

print("part 1 test answer: "+str(part1(testinput)))
print("part 1 answer: "+str(part1(input)))
print("part 2 test answer: "+str(part2(testinput)))
print("part 2 answer: "+str(part2(input)))
