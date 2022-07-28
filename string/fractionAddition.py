# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 13:46:27 2022
@author: xiao.chen
From Leetcode 592
Type: ++
"""

import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        # 初始化分子、分母保存列表
        numerator = []
        denominator = []
        
        # # 计算分子个数
        # fractionNum = expression.count("/")
        
        # 利用"/"拆分字符串
        splitExpress = expression.split("/")
        numerator.append(int(splitExpress[0])) # 保存第一个数的分子
        
        # 依次保存每个分数的分母、分子
        for e in splitExpress[1:len(splitExpress)-1]:
            if "+" in e:
                e = e.split("+")
                numerator.append(int(e[1]))
            if "-" in e:
                e = e.split("-")
                numerator.append(-int(e[1]))
            denominator.append(int(e[0]))
        
        denominator.append(int(splitExpress[-1]))# 保存最后一个数的分母
        
        print("numerator:",numerator)
        print("denominator:",denominator)
        
        # 获取所有分母的乘积
        # comMultiple = 1
        # for num in denominator:
        #     comMultiple *= num
        comMultiple = math.prod(denominator)
        
        # 计算分子加和
        sumNum = 0
        for i in range(len(numerator)):
            sumNum += numerator[i] * comMultiple // denominator[i]
        if sumNum == 0:
            return "0/1"
        
        # 获取分子加和和分母最小公倍数的最大公约数
        comDevisor = math.gcd(sumNum, comMultiple)
        
        # 当结果为整数时
        if sumNum % comMultiple ==0:
            return str(sumNum//comDevisor)+"/1"
        else:
            return str(sumNum//comDevisor) + "/" + str(comMultiple//comDevisor)


if __name__ == "__main__":
    so = Solution()
    
    expression = "-5/2-10/3+7/9"

    result = so.fractionAddition(expression)
    print(result)
 