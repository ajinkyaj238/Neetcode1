class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        var_dicts = {}
        for i in range(strs):
            j = sorted(strs(i))
            if j in var_dicts:
                var_dicts[j].append(strs[i])
        return var_dicts.values


        

        

            


            

            
            