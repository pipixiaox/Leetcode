# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 19:52:06 2022

@author: xiao.chen
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <=1:
            return len(s)
        exited = {}
        start = 0
        end = 0
        length = end - start
        i = 0
        while i < len(s):
            
            # print("s[i]:",s[i])
            if s[i] not in exited:
                # 将当前字符添加到字典中
                exited[s[i]] = i
                
                # 当字符从未出现时，更新子串下索引为当前字符
                end = i
                # 若为最后一个字符，则更新子串end索引
                if i == len(s)-1 and end-start+1 > length:
                    length = end -start+1
            else:
                # 当字符存在时，子串下索引为当前字符的前1字符
                end = i-1
                # 若新子串长度更大，则更新子串的索引值
                if end-start+1 > length:
                   length = end-start+1
                
                # 记录重复字符所在下标
                nstart = exited[s[i]]
                
                # 更新重复出现元素的下标
                exited[s[i]] = i
                
                # 删除新子串之前的值
                for j in range(start,nstart):
                    if exited[s[j]] < nstart:
                        exited.pop(s[j])
                
                # 从重复字符上一次的下标+1开始重新计算子串
                start = nstart+1
            # print("now the longestSubstring is:",s[start:end])
            i += 1
        return length




if __name__ == '__main__':
    s = Solution()
    s1 = "aaaaaaaaaaa"
    result = s.lengthOfLongestSubstring(s1)
    print(result)




