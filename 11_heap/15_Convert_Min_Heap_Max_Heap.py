# User function Template for python3
def max_heapify(arr, N, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < N and arr[left] > arr[largest]:
        largest = left
    if right < N and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, N, largest)


class Solution:
    def convertMinToMaxHeap(self, N, arr):
        idx = N // 2 - 1
        for i in range(idx, -1, -1):
            max_heapify(arr, N, i)


# {
# Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.convertMinToMaxHeap(N, arr)
        for val in arr:
            print(val, end=" ")
        print()
# } Driver Code Ends
