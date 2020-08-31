
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        words, mods = ["Fizz", "Buzz"], [3, 5]
        k, res = 2, []
        for i in range(1, n+1):
            current_str = ""
            for j in range(k):
                if i%mods[j] == 0: current_str += words[j]
                    
            if not current_str:
                res.append(str(i))
            else:
                res.append(current_str)
                
        return res