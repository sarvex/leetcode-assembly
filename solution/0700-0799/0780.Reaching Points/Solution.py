class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy and tx != ty:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if tx == sx:
            return True if ty == sy else ty > sy and (ty - sy) % tx == 0
        return tx > sx and (tx - sx) % ty == 0 if ty == sy else False
