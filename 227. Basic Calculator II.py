#space: O(1)
#Time: O(n)
class Solution:
    def calculate(self, s: str) -> int:
        calc=0
        tail=0
        num=0
        ls= '+'
        for i in range(len(s)):
            c= s[i]
            if c.isdigit():
                num= num*10 + int(c)
            if ( c.isdigit() == False and c !=' ') or  i == len(s)-1:
                if ls == '+':
                    calc= calc + num
                    tail= num
                elif ls == '-':
                    calc= calc - num
                    tail= -num
                elif ls == '*':
                    calc= (calc - tail) + (tail*num)
                    tail= tail * num
                elif ls == '/':
                    calc= (calc - tail) + int(tail/num)
                    tail= int(tail / num)
                ls= c
                num = 0
            # print(s[i],num, calc, tail)
        return calc
