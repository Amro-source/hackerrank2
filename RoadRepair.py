def getMinCost(crew_id, job_id, row_covered, col_covered):
    # Write your code here

    crew_id.sort()
    job_id.sort()

    n = len(crew_id)
    cost = [[abs(crew_id[i] - job_id[j]) for j in range(n)] for i in range(n)]

    for i in range(n):
        min_row = min(cost[i])
        for j in range(n):
            cost[i][j] -= min_row

    for j in range(n):
        min_col = min(cost[i][j] for i in range(n))
        for i in range(n):
            cost[i][j] -= min_col

    row_covered = [False] * n # A list to keep track of which rows are covered by a zero
    col_covered = [False] * n # A list to keep track of which columns are covered by a zero
    assignment = [-1] * n # A list to store the optimal assignment of crews to jobs

    for i in range(n):
        for j in range(n):
            if cost[i][j] == 0 and not row_covered[i] and not col_covered[j]:
                # Assign crew i to job j
                assignment[i] = j
                # Cover row i and column j
                row_covered[i] = True
                col_covered[j] = True
                break

    if all(row_covered) and all(col_covered):
        return sum(abs(crew_id[i] - job_id[assignment[i]]) for i in range(n))
    else:
        return getMinCostHelper(cost, row_covered, col_covered)
    
def getMinCostHelper(cost, row_covered, col_covered):
    n = len(cost)
    
    min_uncovered = float('inf')
    for i in range(n):
        for j in range(n):
            if not row_covered[i] and not col_covered[j]:
                min_uncovered = min(min_uncovered, cost[i][j])
    
        for i in range(n):
            for j in range(n):
                if row_covered[i]:
                    cost[i][j] += min_uncovered
                if not col_covered[j]:
                    cost[i][j] -= min_uncovered
    
    return getMinCost(cost, row_covered, col_covered)
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crew_id_count = int(input().strip())

    crew_id = []

    for _ in range(crew_id_count):
        crew_id_item = int(input().strip())
        crew_id.append(crew_id_item)

    job_id_count = int(input().strip())

    job_id = []

    for _ in range(job_id_count):
        job_id_item = int(input().strip())
        job_id.append(job_id_item)

    row_covered=[]
    col_covered=[]    
    result = getMinCost(crew_id, job_id,row_covered,col_covered)

    fptr.write(str(result) + '\n')

    fptr.close()
