import numpy as np

class Solution:
    def penalty(self, prev, current):
        return (200 - (current-prev))**2
    def hotel(self, locs):
        dp = [[0] * len(locs) for _ in range(len(locs))]
        for i in range(1, len(locs)):
            for j in range(0, i):
                if locs[i] - locs[j] <= 200:
                    if dp[j][:j] == []:
                        prev_penalty = 0
                    else:
                        prev_penalty = min(dp[j][:j])
                    dp[i][j] = prev_penalty + self.penalty(locs[j], locs[i])
                else:
                    dp[i][j] = float("inf")
        min_penalty = min(dp[-1][:j+1])
        min_idx = np.argmin(dp[-1][:j+1])
        path = [len(locs)-1, min_idx]
        while min_idx > 0:
            min_idx = np.argmin(dp[min_idx][:min_idx])
            path.append(min_idx)
        return min_penalty, path[::-1]



def main():
    hotel_locations = [0, 10, 150, 220, 250, 370, 400, 410, 417, 550, 570]
    s = Solution()
    minPenalty, route = s.hotel(hotel_locations)
    print(minPenalty, route)

if __name__ == "__main__":
    main()