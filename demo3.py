# -*- coding: utf-8 -*-
# @File     : demo3.py
# @Author   : Leonard
# @Email    : leoleechn@hotmail.com
# @Software : PyCharm

# 说明： 修改尺寸

# 导入第三方模块
import cv2 as cv

# 读取图片
picRead = cv.imread("headpic.jpg")

# 修改图片大小
resizePic = cv.resize(picRead, dsize=(500, 500))

# 展示原图
initialPicShow = cv.imshow("initialShow", picRead)

# 展示修改图
reshapePicShow = cv.imshow("reshapeShow", resizePic)

# 打印尺寸
print("原图尺寸为:", picRead.shape)
print("修改后图尺寸为:", resizePic.shape)

# 退出
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()
