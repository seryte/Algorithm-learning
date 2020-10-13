'''                              .::::.                                               _oo0oo_
                               .::::::::.                                            o8888888o
                              :::::::::::                                            88" . "88
                           ..:::::::::::'                                            (| -_- |)
                        '::::::::::::'                                               0\  =  /0
                          .::::::::::                                              ___/`---'\___
                     '::::::::::::::..                                           .' \\|     |# '.
                          ..::::::::::::.                                       / \\|||  :  |||# \
                        ``::::::::::::::::                                     / _||||| -:- |||||- \
                         ::::``:::::::::'        .:::.                        |   | \\\  -  #/ |   |
                        ::::'   ':::::'       .::::::::.                      | \_|  ''\---/''  |_/ |
                      .::::'      ::::     .:::::::'::::.                     \  .-\__  '-'  ___/-. /
                     .:::'       :::::  .:::::::::' ':::::.                 ___'. .'  /--.--\  `. .'___
                    .::'        :::::.:::::::::'      ':::::.            ."" '<  `.___\_<|>_/___.' >' "".
                   .::'         ::::::::::::::'         ``::::.         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
               ...:::           ::::::::::::'              ``::.        \  \ `_.   \_ __\ /__ _/   .-` /  /
              ```` ':.          ':::::::::'                  ::::..      `-.____`.___ \_____/___.-`___.-'
                                 '.:::::'                    ':'````..                `=---='
                            女神保佑         永无BUG                            佛祖保佑         永无BUG
                                                                                                     
'''
from time import sleep
from typing import List

from time_coase import coast


class Solution:
    # 暴力算法时间复杂度O（n²），空间复杂度O（1）
    @coast
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ret.append([i, j])
        return ret


s = Solution()
# print(s.twoSum([5, 12, 6, 3, 9, 2, 1, 7], 13))
# s.twoSum([3,3], 6)


# 哈希法
class Solution:
    @coast
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {nums[k]: k for k in range(len(nums))}
        ret = []
        for i in range(len(nums)):
            other = target - nums[i]
            if other in map and map[other] != i:
                ret.append(i)
                ret.append(map[other])
                del map[nums[i]]
        return ret


s = Solution()
print(s.twoSum([3,2,4], 6))
