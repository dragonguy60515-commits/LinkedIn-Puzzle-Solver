# yellow = [
#     [0, 0], [0, 3], [0, 4], [0, 6],
#     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 6],
#     [2, 0], [2, 1], [2, 4], [2, 6],
#     [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6],
#     [4, 1], [4, 2], [4, 6],
#     [5, 0], [5, 1], [5, 5], [5, 6],
#     [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6]
# ]
#
# color_array = [
#     [[2, 2], [2, 3]],          # red
#     [[0, 5], [1, 5], [2, 5]],  # orange
#     yellow,                    # yellow
#     [[3, 0], [4, 0]],          # white
#     [[4, 3], [5, 2], [5, 3]],  # green
#     [[4, 4], [4, 5], [5, 4]],  # blue
#     [[0, 1], [0, 2]]           # purple
# ]
#
# ###小區域先放（剪枝）
# question = sorted(color_array, key=len)
answer = []  # [[y, x], ...]
color_idx = -1

def is_safe(y, x):
    for py, px in answer:
        if py == y:                  # same row
            return False
        if px == x:                  # same column
            return False
        if abs(py - y) == 1 and abs(px - x) == 1:  # diagonal
            return False
    return True

def solve(question):
    global color_idx
    if color_idx == len(question):
        return True   # 找到第一組解，直接回傳
    color_idx += 1
    for y, x in question[color_idx]:
        if is_safe(y, x):
            answer.append([y, x])
            if color_idx == len(question)-1:
                return True  # 找到第一組解，直接回傳
            if solve(question):   # 關鍵：只要成功就一路傳 True
                # print(color_idx)
                return True
            answer.pop()
            color_idx -= 1# 回溯
    return False  # 此顏色無解 → 退回上一層


def pass_Answer():
    return answer