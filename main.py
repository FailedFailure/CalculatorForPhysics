import math

print("適当な小道具です! \n")
type = input("円柱? (1) 円筒? (2) ")
# 二つの種類の物を区分
if int(type) == 1:
    list_M = []
    list_D = []
    list_L = []
    print("質量を5回いれて")
    for i in range(0,5):
        list_M.append(float(input()))
    print("直径を5回いれて")
    for i in range(0,5):
        list_D.append(float(input()))
    print("長さを5回いれて")
    for i in range(0,5):
        list_L.append(float(input()))
    sum_M = 0.0
    sum_D = 0.0
    sum_L = 0.0
    for i in range(0,5):
        sum_M = sum_M + list_M[i]
        sum_D = sum_D + list_D[i]
        sum_L = sum_L + list_L[i]
    aver_M = sum_M / 5
    aver_D = sum_D / 5
    aver_L = sum_L / 5
    diff_M = 0.0
    diff_D = 0.0
    diff_L = 0.0
    for i in range(0,5):
        diff_M = diff_M + (aver_M - list_M[i]) * (aver_M - list_M[i])
        diff_D = diff_D + (aver_D - list_D[i]) * (aver_D - list_D[i])
        diff_L = diff_L + (aver_L - list_L[i]) * (aver_L - list_L[i])
    delta_M = math.sqrt(diff_M / 4)
    delta_D = math.sqrt(diff_D / 4)
    delta_L = math.sqrt(diff_L / 4)
    averdelta_M = delta_M / math.sqrt(5)
    averdelta_D = delta_D / math.sqrt(5)
    averdelta_L = delta_L / math.sqrt(5)
    print("質量の平均值は" + str(aver_M) + "\n質量の誤差は" + str(averdelta_M))
    print("直径の平均值は" + str(aver_D) + "\n直径の誤差は" + str(averdelta_D))
    print("長さの平均值は" + str(aver_L) + "\n長さの誤差は" + str(averdelta_L))
    aver_V = math.pi * (aver_D / 2) * (aver_D / 2) * aver_L / 1000
    averdelta_V = aver_V * math.sqrt((2 * averdelta_D / aver_D) * (2 * averdelta_D / aver_D) + (averdelta_L / aver_L) * (averdelta_L / aver_L))
    aver_dens = aver_M / aver_V
    averdelta_dens = aver_dens * math.sqrt((2 * averdelta_D / aver_D) * (2 * averdelta_D / aver_D) + (averdelta_L / aver_L) * (averdelta_L / aver_L) + (averdelta_M / aver_M) * (averdelta_M / aver_M))
    print("体積は" + str(aver_V) + "\n体積の誤差は" + str(averdelta_V))
    print("密度は" + str(aver_dens) + "\n密度の誤差は" + str(averdelta_dens))

elif int(type) == 2:
    list_M = []
    list_D = []
    list_t = []
    list_L = []
    print("質量を5回いれて")
    for i in range(0,5):
        list_M.append(float(input()))
    print("直径を5回いれて")
    for i in range(0,5):
        list_D.append(float(input()))
    print("厚さを5回いれて")
    for i in range(0,5):
        list_t.append(float(input()))
    print("長さを5回いれて")
    for i in range(0,5):
        list_L.append(float(input()))
    sum_M = 0.0
    sum_D = 0.0
    sum_t = 0.0
    sum_L = 0.0
    for i in range(0,5):
        sum_M = sum_M + list_M[i]
        sum_D = sum_D + list_D[i]
        sum_t = sum_t + list_t[i]
        sum_L = sum_L + list_L[i]
    aver_M = sum_M / 5
    aver_D = sum_D / 5
    aver_t = sum_t / 5
    aver_L = sum_L / 5
    diff_M = 0.0
    diff_D = 0.0
    diff_t = 0.0
    diff_L = 0.0
    for i in range(0,5):
        diff_M = diff_M + (aver_M - list_M[i]) * (aver_M - list_M[i])
        diff_D = diff_D + (aver_D - list_D[i]) * (aver_D - list_D[i])
        diff_t = diff_t + (aver_t - list_t[i]) * (aver_t - list_t[i])
        diff_L = diff_L + (aver_L - list_L[i]) * (aver_L - list_L[i])
    delta_M = math.sqrt(diff_M / 4)
    delta_D = math.sqrt(diff_D / 4)
    delta_t = math.sqrt(diff_t / 4)
    delta_L = math.sqrt(diff_L / 4)
    averdelta_M = delta_M / math.sqrt(5)
    averdelta_D = delta_D / math.sqrt(5)
    averdelta_t = delta_t / math.sqrt(5)
    averdelta_L = delta_L / math.sqrt(5)
    print("質量の平均值は" + str(aver_M) + "\n質量の誤差は" + str(averdelta_M))
    print("直径の平均值は" + str(aver_D) + "\n直径の誤差は" + str(averdelta_D))
    print("厚さの平均值は" + str(aver_t) + "\n厚さの誤差は" + str(averdelta_t))
    print("長さの平均值は" + str(aver_L) + "\n長さの誤差は" + str(averdelta_L))
    aver_V = math.pi * (aver_D - aver_t) * aver_t * aver_L / 1000
    averdelta_V = aver_V * math.sqrt((averdelta_D / aver_D) * (averdelta_D / aver_D) + (averdelta_t / aver_t) * (averdelta_t / aver_t) + (averdelta_L / aver_L) * (averdelta_L / aver_L))
    aver_dens = aver_M / aver_V
    averdelta_dens = aver_dens * math.sqrt((averdelta_D / aver_D) * (averdelta_D / aver_D) + (averdelta_t / aver_t) * (averdelta_t / aver_t) + (averdelta_L / aver_L) * (averdelta_L / aver_L) + (averdelta_M / aver_M) * (averdelta_M / aver_M))
    print("体積は" + str(aver_V) + "\n体積の誤差は" + str(averdelta_V))
    print("密度は" + str(aver_dens) + "\n密度の誤差は" + str(averdelta_dens))

else:
    print("Nah")