#50th question!

def generate(numRows: int) -> list[list[int]]:
    depth = 0
    triangle = []
    while depth < numRows:
        row = [1] * (depth + 1)
        for i in range(1, len(row) - 1):
            row[i] = triangle[depth - 1][i - 1] + triangle[depth - 1][i]
        triangle.append(row)
        depth += 1

    return triangle