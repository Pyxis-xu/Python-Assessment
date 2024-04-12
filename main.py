def sort(N, M, data, K):
    # 对数据按照第K列进行排序
    sort_data = sorted(data, key=lambda x: x[K])
    # 去除排序后相同属性的重复行，只保留首次出现的行
    seen = set()
    unique_data = []
    for row in sort_data:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_data.append(row)
    return unique_data

# 读取输入
N, M = map(int, input().split())
data = []
for i in range(N):
    row = list(map(int, input().split()))
    data.append(row)

K = int(input())

# 检查约束条件
if not (1 <= N <= 1000 and 1 <= M <= 1000 and 0 <= K < M):
    print("Invalid input.")
else:
    # 排序并打印结果
    sorted_data = sort(N, M, data, K)
    for row in sorted_data:
        print(*row)

