# -*- coding: utf-8 -*-
# @File     : demo2.py
# @Author   : Leonard
# @Email    : leoleechn@hotmail.com
# @Software : PyCharm

# 说明： 灰度转换

# 导入第三方模块
import cv2 as cv

# 读取图片
picRead = cv.imread("headPic.jpg")

# 灰度转换
grayImg = cv.cvtColor(picRead, cv.COLOR_BGR2GRAY)

# 展示图片
picShow = cv.imshow("show", grayImg)

# 延时
cv.waitKey(0)

# 保存图片
cv.imwrite("grayPic.jpg", grayImg)

# 释放内存
cv.destroyAllWindows()
