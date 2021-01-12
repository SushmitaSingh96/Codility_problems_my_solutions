'''
Links for ref:
https://codility.com/media/train/solution-stone-wall.pdf
https://www.martinkysel.com/codility-stonewall-solution/
'''

'''
Using the for loop we traverse each element/height. We add the first element/height into the stack by default and count one block for it. 
Now as we traverse, if we encounter a height such that tos is larger than present height,
we pop tos till either stack is empty check if its equal to tos or we add the present height to the stack and count one block for it ,
or we encounter a number in the stack which is smaller than present number than check if it's equal if not we add it to the tos and count one block for it. 
So basically we are counting stones that were once present or is still present if the stack. 
So which numbers are not added to the stack or not counted? Simply numbers which we find ARE already PRESENT in the stack when are travering the heights. 
Note here it's ARE PRESENT not WERE PRESENT. 
'''


def solution(H):
    block_cnt = 0
    stack = []
     
    for height in H:
        # remove all blocks that are bigger than my height
        while len(stack) != 0 and stack[-1] > height:
            stack.pop()
         
        if len(stack) != 0 and stack[-1] == height:
            # we already paid for this size
            pass
        else:
            # new block is required, push it's size to the stack
            block_cnt += 1
            stack.append(height)
         
    return block_cnt