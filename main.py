
def spiralOrder(matrix):
    direction = 1 #1 = East, 2 = South, 3 = West, 4 = North
    h = 0
    v = 0
    width = len(matrix[0])
    height = len(matrix)
    placesIveBeen = []
    answer = []
    totalNodes = width*height
    nodesVisited = 0

    while True:
        answer.append(matrix[v][h])
        nodesVisited += 1
        if nodesVisited == totalNodes:
            return answer
        
        placesIveBeen.append([v, h])

        match direction:
            case 1:
                #East
                if h < width - 1 and not [v, h + 1] in placesIveBeen:
                    h += 1
                    continue
                #South
                if v < height - 1 and not [v + 1, h] in placesIveBeen:
                    v += 1
                    direction = 2
                    continue
                #West
                if h > 0 and not [v, h - 1] in placesIveBeen:
                    h -= 1
                    direction = 3
                    continue
                #North
                if v > 0 and not [v - 1, h] in placesIveBeen:
                    v -= 1
                    direction = 4
                    continue
            case 2: #South
                #South
                if v < height - 1 and not [v + 1, h] in placesIveBeen:
                    v += 1
                    direction = 2
                    continue
                #West
                if h > 0 and not [v, h - 1] in placesIveBeen:
                    h -= 1
                    direction = 3
                    continue
                #North
                if v > 0 and not [v - 1, h] in placesIveBeen:
                    v -= 1
                    direction = 4
                    continue
                #East
                if h < width - 1 and not [v, h + 1] in placesIveBeen:
                    h += 1
                    continue
            case 3: #West
                #West
                if h > 0 and not [v, h - 1] in placesIveBeen:
                    h -= 1
                    direction = 3
                    continue
                #North
                if v > 0 and not [v - 1, h] in placesIveBeen:
                    v -= 1
                    direction = 4
                    continue
                #East
                if h < width - 1 and not [v, h + 1] in placesIveBeen:
                    h += 1
                    continue
                #South
                if v < height - 1 and not [v + 1, h] in placesIveBeen:
                    v += 1
                    direction = 2
                    continue
            case 4: #North
                #North
                if v > 0 and not [v - 1, h] in placesIveBeen:
                    v -= 1
                    direction = 4
                    continue
                #East
                if h < width - 1 and not [v, h + 1] in placesIveBeen:
                    h += 1
                    continue
                #South
                if v < height - 1 and not [v + 1, h] in placesIveBeen:
                    v += 1
                    direction = 2
                    continue
                #West
                if h > 0 and not [v, h - 1] in placesIveBeen:
                    h -= 1
                    direction = 3
                    continue


# Example 1:
# Input: 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: 
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
