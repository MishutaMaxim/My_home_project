def generate(numRows: int):
    result = []
    for i in range(numRows):
        result.append([])
        for j in range(i+1):
            if i == 0 or j == 0:
                result[i].append(1)
            else:
                result[i].append(sum(result[i-1][j-1:j+1]))

    return result

print(generate(5))
