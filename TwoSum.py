#V úloze twosum se snažíme najít z číselné sady (která mají indexy od 0 až po daný počet čísel) součet který máme zadaný
#např pro hodnoty v mém řešení máme pro čísla v sadě 1, 2, 5 se snažíme najít čísla která se rovnají sedmi
class Solution: 
    def twoSum(seelf, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_dict:
                return [num_dict[complement], i]
            
            num_dict[num] = i

        return []
