class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count = defaultdict(int)
        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit == ".":
                    continue
                count[(digit,"vertical" ,i)] += 1
                count[(digit,"horizontal" ,j )] += 1
                count[(digit,"square" ,i // 3 ,j//3)] += 1
        for freq in count.values(): 
            if freq>1 : return False
        return True
