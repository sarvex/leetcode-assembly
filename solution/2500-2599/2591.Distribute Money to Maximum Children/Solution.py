class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        if money > 8 * children:
            return children - 1
        return children - 2 if money == 8 * children - 4 else (money - children) // 7
