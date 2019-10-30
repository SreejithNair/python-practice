class One:
    @staticmethod
    def multiplyNums(x, y):
        return x + y

l1 = [{'id':1,'name':'a'},{'id':2,'name':'c'}]
l2 = [{'id':4,'name':'d'},{'id':6,'name':'a'}]
for x in l1:
    print(x["name"])

z= len(
    set.intersection(
        {x["name"] for x in l1},
        {x["name"] for x in l2},
    )
) > 0
print(z)
