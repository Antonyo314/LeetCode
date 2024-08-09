class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        d_ = {}

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                d_[f'{arr[i]}_{arr[j]}'] = arr[i] / arr[j]
        d_ = {k: v for k, v in sorted(d_.items(), key=lambda item: item[1])}

        # d_ = {}
        # 
        # for i in range(len(arr)):
        #     for j in range(i + 1, len(arr)):
        #         d_[f'{arr[i]}_{arr[j]}'] = arr[i] * np.prod(np.array(arr[:j] + arr[j+1:]))
        # d_ = {k: v for k, v in sorted(d_.items(), key=lambda item: item[1])}
        return [int(list(d_.keys())[k - 1].split('_')[0]), int(list(d_.keys())[k - 1].split('_')[1])]
