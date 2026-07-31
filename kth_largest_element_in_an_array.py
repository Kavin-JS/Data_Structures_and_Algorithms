import heapq

def findKthLargest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for n in nums[k:]:
        if n > heap[0]:
            heapq.heapreplace(heap, n)
    return heap[0]

if __name__ == "__main__":
    print(findKthLargest([3,2,1,5,6,4], 2))
