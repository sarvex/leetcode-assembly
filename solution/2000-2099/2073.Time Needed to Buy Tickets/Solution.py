class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(
            min(tickets[k], t) if i <= k else min(tickets[k] - 1, t)
            for i, t in enumerate(tickets)
        )
