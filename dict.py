
nums = [3, 2, 4]
d = dict(enumerate(nums))
itemsofd = list(d.items())
secondval = 3
idx = 0
for i in range(len(itemsofd)):
    if secondval in itemsofd:
        if idx == (itemsofd[i][1] == secondval):
            pass
        else:
            print(itemsofd[i][0])
print(secondval)
print(idx)
print(itemsofd)
