def getRow(self, rowIndex: int) -> List[int]:
    memo = {}
    def getRowHelper(index, row):
        if index == 0:
            return [1]
        if index == 1:
            return [1, 1]
        if index in memo:
            return memo[index]
        prev_row = getRowHelper(index - 1, row)
        new_row = [1]
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])
        new_row.append(1)
        memo[index] = new_row
        return new_row
    
    return getRowHelper(rowIndex, [])