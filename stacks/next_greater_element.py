def next_greater_element(arr):
    res = [-1 for _ in range(len(arr))]
    stack = []
    print(arr)
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            res[stack[-1]] = arr[i]
            stack.pop()
        stack.append(i)
        print(res, stack)
    return res


if __name__ == "__main__":
    print(next_greater_element([4, 1, 8, 3, 25]))
