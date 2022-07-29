board = [
["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]


arb_numb_list = ['1','2','3','4','5','6','7','8','9']
"""        
#O(n^2) efficiency
for j in range(len(board)):

    # embedded column checker less memory
    hashset_col = {key: 0 for key in arb_numb_list}
    for k in range(len(board)):
        board_pos = board[k][j]
        if board_pos in hashset_col and hashset_col[board_pos] == 1:  # instant return
            #return False
            #print(False)
            continue
        elif board_pos in hashset_col and hashset_col[board_pos] == 0:
            hashset_col[board_pos] += 1

    # row checker
    hashset_row = {key: 0 for key in arb_numb_list}
    for intgr in board[j]:      
        if intgr in hashset_row and hashset_row[intgr] == 1:  # instant return
            #return False
            #print(False)
            continue
        elif intgr in hashset_row and hashset_row[intgr] == 0:
            hashset_row[intgr] += 1
    """
        
#box checker
box_cord = [1,4,7]
for row in box_cord:
    for col in box_cord:        
        hashset_box = {key: 0 for key in arb_numb_list}


        center = str(board[row][col])
        up = str(board[row-1][col])
        down = str(board[row+1][col])
        left = str(board[row][col-1])
        right = str(board[row][col+1])
        topleft = str(board[row-1][col-1])
        topright = str(board[row-1][col+1])
        botleft = str(board[row+1][col-1])
        botright = str(board[row+1][col+1])


        if center in hashset_box and hashset_box[center] == 0:
            hashset_box[center] += 1
        else:
            continue

        if up in hashset_box and hashset_box[up] == 0:
            hashset_box[up] += 1
        elif up in hashset_box and hashset_box[up] == 1:
            #return False
            print(False)
        else:
            continue

        if down in hashset_box and hashset_box[down] == 0:
            hashset_box[down] += 1
        elif down in hashset_box and hashset_box[down] == 1:
            #return False
            print(False)
        else:
            continue

        if left in hashset_box and hashset_box[left] == 0:
            hashset_box[left] += 1
        elif left in hashset_box and hashset_box[left] == 1:
            #return False
            print(False)
        else:
            continue

        if right in hashset_box and hashset_box[right] == 0:
            hashset_box[right] += 1
        elif right in hashset_box and hashset_box[right] == 1:
            #return False
            print(False)
        else:
            continue

        if topleft in hashset_box and hashset_box[topleft] == 0:
            hashset_box[topleft] += 1
        elif topleft in hashset_box and hashset_box[topleft] == 1:
            #return False
            print(False)
        else:
            continue

        if topright in hashset_box and hashset_box[topright] == 0:
            hashset_box[topright] += 1
        elif topright in hashset_box and hashset_box[topright] == 1:
            #return False
            print(False)
        else:
            continue

        if botleft in hashset_box and hashset_box[botleft] == 0:
            hashset_box[botleft] += 1
        elif botleft in hashset_box and hashset_box[botleft] == 1:
            #return False
            print(False)
        else:
            continue

        if botright in hashset_box and hashset_box[botright] == 0:
            hashset_box[botright] += 1
        elif botright in hashset_box and hashset_box[botright] == 1: 
            #return False
            print(False)
        else:
            continue
        
        
    print(hashset_box)

print(True)
#return True 

    
    
            

            