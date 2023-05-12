class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = set()
        foods = set()
        mp = Counter()
        for _, table, food in orders:
            tables.add(int(table))
            foods.add(food)
            mp[f'{table}.{food}'] += 1
        foods = sorted(list(foods))
        tables = sorted(list(tables))
        res = [['Table'] + foods]
        for table in tables:
            t = [str(table)]
            t.extend(str(mp[f'{table}.{food}']) for food in foods)
            res.append(t)
        return res
