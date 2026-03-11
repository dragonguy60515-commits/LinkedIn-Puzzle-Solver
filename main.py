import pyautogui as pag
import numpy as np
import cv2
import time
import Utility
import queens

###初始點座標
x = 703
y = 342

###滑鼠找尋QUEENS遊戲圖示
location = pag.locateCenterOnScreen("Symbol.png", confidence=0.9)
if location is not None:
    pag.click(location)
else:
    print("Issues occur, can not start the game")

###輸入題目單邊方格數量
section = int(input("請輸入方格尺寸數量:", ))
# ##實作截圖

###練習圖檔
# img = cv2.imread("queens2.png")
# img111 = cv2.imread("queens.png")

###配對成可以被section整除的圖片長寬比 7
if section == 6:
    time.sleep(0.05)
    screenshot = pag.screenshot(region=(667,307,570,570))
    img = np.array(screenshot)
    vtc = img.shape[1]/section
    hrz = img.shape[0]/section

if section == 7:
    time.sleep(0.05)
    screenshot = pag.screenshot(region=(667,307,567,567))
    img = np.array(screenshot)
    vtc = img.shape[1]/section
    hrz = img.shape[0]/section
# #
# # ###配對成可以被section整除的圖片長寬比 8
if section == 8:
    time.sleep(0.05)
    screenshot = pag.screenshot(region=(667,307,568,568))
    img = np.array(screenshot)
    vtc = img.shape[1] / section
    hrz = img.shape[0] / section

if section == 9:
    time.sleep(0.05)
    screenshot = pag.screenshot(region=(667,307,567,567))
    img = np.array(screenshot)
    vtc = img.shape[1] / section
    hrz = img.shape[0] / section

imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgBox = Utility.splitBoxes(imgRGB,section) ###以扣除掉黑色格線
meanColor_Boxes = Utility.get_mean_color(imgBox,section) ###已從BGR轉成RGB
array = np.asarray(meanColor_Boxes,dtype=int) ###(49,3)
###Color_group標籤
color_group = Utility.build_color_group(array)
###全部為RGB值，已排成題目2維7*7形狀
meanColor_Boxes = array.reshape(section,section,-1)
###已經列印好座標及顏色分類
question = Utility.coordinate(meanColor_Boxes,color_group,section)
###由小排到大
question_sorted = sorted(question, key=len)
for i in question_sorted:
    print(i)
###這邊才要去做分類, 產生座標
result = queens.solve(question_sorted)
print(result)
if result:
    answer = queens.pass_Answer()
    print(answer)

    pag.moveTo(x,y)
    for pos in answer:
        pag.doubleClick(x + pos[1]*vtc, y + pos[0]*hrz)
        print("x=",x + pos[1]*vtc, "y=",y + pos[0]*hrz)
        time.sleep(0.1)
    print("破關完成")