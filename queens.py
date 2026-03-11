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
