class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last_digit = len(arr) - 1

        for i in range(len(arr)):
            arr[i] = -1  # smallest fix

            for j in range(i + 1, len(arr)):
                if arr[i] < arr[j]:
                    arr[i] = arr[j]

        arr[last_digit] = -1
        return arr