# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:20:36 2022

@author: xiao.chen
"""
# import time

class WordFilter():
    
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words

    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        length = len(self.words) # 获取列表大小
        prefLen = len(pref) # 获取前缀长度
        suffLen = len(suff) # 获取后缀长度
        left = 0
        right = length
        
        while left < right:
            mid = (left+right)//2
            for i in range(right-1, mid-1, -1):
                word = self.words[i]
                if word[0:prefLen] == pref and word[-suffLen:] == suff:
                    newmid = (mid + right) //2
                    if i > newmid:
                        left = newmid+1
                    elif i == newmid:
                        return i
                    else:
                        right = newmid
                    break
                elif i == mid:
                    right = mid
                    break

        return -1
                    
                
        
        



if __name__ == '__main__':
    # Your WordFilter object will be instantiated and called as such:
    # obj = WordFilter(words)
    # param_1 = obj.f(pref,suff)
    
    words = ['a','b','c','e','f','c','d','g','d']
    obj = WordFilter(words)
    pref = 'c'
    suff = 'c'
    param_1 = obj.f(pref, suff)
    print(param_1)
    
    # pref = 'c'
    # suff = 'c'
    # param_2 = obj.f(pref, suff)
    # print(param_2)