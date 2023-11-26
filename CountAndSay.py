class Solution:
    def countAndSay(self, n: int) -> str:
        def sayHelper(x):
            result=[]
            current_digit=None
            count=0
            for d in x:
                if current_digit is None or current_digit==d:
                    count+=1
                else:
                    result.append([int(current_digit),count])
                    count=1
                current_digit=d
            result.append([int(current_digit),count])
            return result

        def countHelper(x):
            return ''.join(map(lambda x:str(x[1])+str(x[0]),x))

        result='1'
        for _ in range(n-1):
            result=sayHelper(result)
            result=countHelper(result)
        return result