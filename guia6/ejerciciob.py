# 14:0:0
# 14:0:1
# 14:0:2
# .... 15:0:0

for h in range(14, 16): # 14, 15
    for m in range(0, 60): # 0, 1, ..., 59
        if h == 15 and s == 1:
            break
        for s in range(0, 60): # 0, 1, 2, ..., 59
            if h == 15 and s == 1:
                break
            print(f'{h}:{m}:{s}') # 14:0:0
                                  # 14:0:1
                                  # 14:0:2
                                  # 14:0:59
                                  # 14:1:0
