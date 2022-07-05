n = int(input("Enter number of nodes:"))
nodes = []
for i in range(n):
    nodes.append({"path":1000, "child": [], "name":i})

m = int(input("Enter number of edges:"))
for i in range(m):
    print("Enter details of edge:")
    n1 = int(input("node1:"))
    n2 = int(input("node2:"))
    w = int(input("weight:"))

    nodes[n1]["child"].append([n2,w])
    nodes[n2]["child"].append([n1,w])



# nodes1=[
#  {"path":1000,"child":[[1,4],[7,8]],"name":0},
#  {"path":1000,"child":[[0,4],[2,8],[7,11]], "name":1},
#  {"path":1000,"child":[[1,8],[8,2],[5,4],[3,7]], "name":2},
#  {"path":1000,"child":[[2,7],[5,14],[4,9]], "name":3},
#  {"path":1000,"child":[[3,9],[5,10]], "name":4},
#  {"path":1000,"child":[[6,2],[2,4],[3,14],[4,10]], "name":5},
#  {"path":1000,"child":[[5,2],[7,1],[8,6]], "name":6},
#  {"path":1000,"child":[[0,8],[1,11],[8,7],[6,1]], "name":7},
#  {"path":1000,"child":[[2,2],[6,6],[7,7]], "name":8}
# ]

while 1:
    str = int(input("Enter starting node:"))
    gl = int(input("Enter goal node:"))
    start = nodes[str]
    nodes[str]["path"] = 0
    goal = nodes[gl]

    opened = []
    closed = []
    distance = 1000
    opened.append(start)
    minimum = 1000

    while len(opened) != 0:
        counter=-1
        
        
        for i in opened:
            counter+=1
            if minimum > i["path"]:
                minimum = i["path"]
                index = counter
                
        closed.append(opened[index])
        ##node = opened[index]
        node = opened.pop(index)    
        
        if node["name"] == goal["name"]:
            if distance > node["path"]:
                distance = node["path"]
        

        for i in node["child"]:
            flag = 0
            flag2 = 0
            dict = nodes[i[0]]
            dist = i[1]
            
            
            for j in closed:
                if dict["name"] == j["name"]:
                    flag = 1
            if flag == 1:
                continue
            for j in opened:
                if j["name"] == dict["name"]:
                    dist2 = node["path"] + dist
                    flag2 = 1
                    if dist2 < j["path"]:
                        j["path"] = dist2
                        
            if flag2 == 1:
                continue

            dict["path"]= node["path"]+ dist
            opened.append(dict)

        ##print("opened")
        ##print(opened)
        ##print("closed")
        ##print(closed)
        
        

    print(distance)
