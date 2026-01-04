class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        result = 0
        for num in nums:
            divisors = 0
            temp = 0
            for i in range(1, math.floor(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisors += 1
                    temp += i
                    if num / i != i:
                        divisors += 1
                        temp += num / i

            if divisors == 4:
                result += temp
        
        return int(result)