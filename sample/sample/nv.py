import sys
class DuplicateChecker:
    def __init__(self, lst):
        self.lst = lst

    def check(self):
        for i in range(len(self.lst)):
            for j in range(i+1, len(self.lst)):
                if self.lst[i] == self.lst[j]:
                    print("True")
                    sys.exit()

list1 = [1,2,3,4,3,1]
checker = DuplicateChecker(list1)
checker.check()