class State:
    def __init__(self, board):
        self.bitboard = [0 for _ in range(2)]
        self.height = [0 for _ in range(7)] # stores the first empty bit
        self.counter = 1
        self.moves = [0 for _ in range(43)]
        self.convertToBitboard(board)

    def convertToBitboard(self, board):
        print(board)
        for col in range(7):
            for row in range(6):
                val = board[row][col]
                if val == 1:
                    self.bitboard[0] = (self.bitboard[0] << 1) | 1
                elif val == 2:
                    self.bitboard[1] = (self.bitboard[1] << 1) | 1
            self.bitboard[0] = (self.bitboard[0] << 1)
            self.bitboard[1] = (self.bitboard[1] << 1)


    def makeMove(self, col):
        move = 1 << self.height[col] # get the first empty row and set it to 1
        move = move << (7 * col)
        self.height[col] += 1 # update the height array
        self.bitboard[self.counter & 1] ^= move # update bitboard for the correct player
        self.moves[self.counter] = col # add move
        self.counter += 1

    def undoMove(self):
        self.counter -= 1
        col = self.moves[self.counter]
        self.height[col] -= 1
        move = 1 << self.height[col]
        move = move << (7*col)
        self.bitboard[self.counter & 1] ^= move

    def checkFiveAndBeyond(self, bitboard_current_player):
        left_diagonal = bitboard_current_player &  (bitboard_current_player >> 6) & (bitboard_current_player >> 12) & (bitboard_current_player >> 18) & (bitboard_current_player >> 24)
        right_diagonal = bitboard_current_player &  (bitboard_current_player >> 8) & (bitboard_current_player >> 16) & (bitboard_current_player >> 24) & (bitboard_current_player >> 32)
        horizontal = bitboard_current_player &  (bitboard_current_player >> 7) & (bitboard_current_player >> 14) & (bitboard_current_player >> 21) & (bitboard_current_player >> 28)
        vertical = bitboard_current_player &  (bitboard_current_player >> 1) & (bitboard_current_player >> 2) & (bitboard_current_player >> 3) & (bitboard_current_player >> 4)
        return self.count_ones_in_binary(left_diagonal) + self.count_ones_in_binary(right_diagonal) + self.count_ones_in_binary(horizontal) + self.count_ones_in_binary(vertical) 

    def checkFourAndBeyond(self, bitboard_current_player):
        left_diagonal = bitboard_current_player &  (bitboard_current_player >> 6) & (bitboard_current_player >> 12) & (bitboard_current_player >> 18)
        right_diagonal = bitboard_current_player &  (bitboard_current_player >> 8) & (bitboard_current_player >> 16) & (bitboard_current_player >> 24)
        horizontal = bitboard_current_player &  (bitboard_current_player >> 7) & (bitboard_current_player >> 14) & (bitboard_current_player >> 21)
        vertical = bitboard_current_player &  (bitboard_current_player >> 1) & (bitboard_current_player >> 2) & (bitboard_current_player >> 3)
        return self.count_ones_in_binary(left_diagonal) + self.count_ones_in_binary(right_diagonal) + self.count_ones_in_binary(horizontal) + self.count_ones_in_binary(vertical) 

    def checkThreeAndBeyond(self, bitboard_current_player):
        left_diagonal = bitboard_current_player &  (bitboard_current_player >> 6) & (bitboard_current_player >> 12)
        right_diagonal = bitboard_current_player &  (bitboard_current_player >> 8) & (bitboard_current_player >> 16)
        horizontal = bitboard_current_player &  (bitboard_current_player >> 7) & (bitboard_current_player >> 14)
        vertical = bitboard_current_player &  (bitboard_current_player >> 1) & (bitboard_current_player >> 2)
        return self.count_ones_in_binary(left_diagonal) + self.count_ones_in_binary(right_diagonal) + self.count_ones_in_binary(horizontal) + self.count_ones_in_binary(vertical) 

    def checkTwoAndBeyond(self, bitboard_current_player):
        left_diagonal = bitboard_current_player &  (bitboard_current_player >> 6)
        right_diagonal = bitboard_current_player &  (bitboard_current_player >> 8)
        horizontal = bitboard_current_player &  (bitboard_current_player >> 7)
        vertical = bitboard_current_player &  (bitboard_current_player >> 1)
        return self.count_ones_in_binary(left_diagonal) + self.count_ones_in_binary(right_diagonal) + self.count_ones_in_binary(horizontal) + self.count_ones_in_binary(vertical) 

    def count_ones_in_binary(self, number):
        binary_representation = bin(number)[2:]  # [2:] to remove the '0b' prefix
        count_ones = binary_representation.count('1')
        return count_ones

    def getPossibleMoves(self):
        possibleMoves = []
        TOP = 0b1000000_1000000_1000000_1000000_1000000_1000000_1000000
        for col in range(7):
            if (TOP & (1 << self.height[col])) == 0:
                possibleMoves.append(col)
        return possibleMoves
    
    def isLeafNode(self):
        return self.count_ones_in_binary(self.bitboard[0]) + self.count_ones_in_binary(self.bitboard[1]) == 42

    def getTurn(self):
        return self.counter & 1

    def getScore(self, turn):
        fives = self.checkFiveAndBeyond(self.bitboard[turn])
        fours = self.checkFourAndBeyond(self.bitboard[turn])
        threes = self.checkThreeAndBeyond(self.bitboard[turn])
        twos = self.checkTwoAndBeyond(self.bitboard[turn])
        baseScore = 100
        return fives * 20 * baseScore + fours * baseScore * 10 + threes * 0.1 * baseScore + twos * 0.05 * baseScore