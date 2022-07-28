#version 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_reverse = [i for i in nums]
        nums_reverse.reverse()

        if 0 in nums is True:
            zero_indicies = []
            nums_check = [k for k in nums]
            while 0 in nums_check is True: # Checks to see the index of the zeros. 
                arb_var = nums.index(0) 
                zero_indicies.append(arb_var)
                nums_check[arb_var] = 1

            #answer
            if len(zero_indicies) > 1:
                answer = [0] * len(nums)

            elif len(zero_indicies) == 1:
                #prefix
                prefix = []
                x=1
                for n in nums:
                    if n == 0:
                        x*=1
                    else:
                        x*=n
                    prefix.append(x)

                #posfix
                posfix = []
                y = 1 
                for m in nums_reverse:
                    if m == 0:
                        y*=1
                    else:
                        y*=m
                    posfix.append(y)
                posfix.reverse()

                answer = [0] * len(nums)
                for a in range(len(nums)):
                    if nums[a] == 0:
                        if a == 0: 
                            answer[a] = posfix[a+1]
                        elif a == len(nums) - 1:
                            answer[a] = prefix[a-1]
                        else:
                            answer[a] = posfix[a+1] * prefix[a-1]
            return answer

        else:
            #prefix
            prefix = []
            x=1
            for n in nums:
                x*=n
                prefix.append(x)

            #posfix
            posfix = []
            y = 1 
            for m in nums_reverse:
                y*=m
                posfix.append(y)
            posfix.reverse()

            answer = []
            for a in range(len(nums)):
                if a == 0: 
                    answer.append(posfix[a+1])
                elif a == len(nums) - 1:
                    answer.append(prefix[a-1])
                else:
                    answer.append(posfix[a+1] * prefix[a-1])
            return answer

#version 2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_reverse = [i for i in nums]
        nums_reverse.reverse()
        
        #prefix
        prefix = []
        x=1
        for n in nums:
            x*=n
            prefix.append(x)

        #posfix
        posfix = []
        y = 1 
        for m in nums_reverse:
            y*=m
            posfix.append(y)
        posfix.reverse()

        answer = []
        for a in range(len(nums)):
            if a == 0: 
                answer.append(posfix[a+1])
            elif a == len(nums) - 1:
                answer.append(prefix[a-1])
            else:
                answer.append(posfix[a+1] * prefix[a-1])
        return answer