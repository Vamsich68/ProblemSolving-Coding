# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

# If it cannot be done, return -1.

# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        faceA=[0]*7
        faceB = [0]*7
        equal=[0]*7
        for i in range(len(tops)):
            faceA[tops[i]] +=1
            faceB[bottoms[i]] +=1
            if tops[i]==bottoms[i]:
                equal[tops[i]] +=1
            minrotation= float('inf')
        for i in range(1,7):
            if (faceA[i] + faceB[i] - equal[i]==len(tops)):
                minrotation = min(minrotation, min(faceA[i], faceB[i])-equal[i])
        if minrotation == float('inf'):
            return -1
        else:
            return minrotation