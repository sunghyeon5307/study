import matplotlib.pyplot as plt
figure = plt.figure()
axes = figure.add_subplot(111)
# x축
x1 = [0,1,2,3,4]
x2 = [4,1,3,5,2]
# y축
y1 = [4,1,3,5,2]
y2 = [4,1,3,5,1]
axes.plot(x1, y1, color = 'r', linestyle = 'dotted')
axes.plot(x2, y2, marker = '^', linewidth = 2, linestyle = '--')
plt.show()

# color : 선의 색상 설정
# 실선(- / solid), 점선(. / dotted), 대시(-- / dashed)

# linewidth : 선의 두께 설정
# 포인트(pt) 단위의 실수 

# color : 선의 색상 설정
# 빨강(red), 파랑(blue), 노란색(yellow)

# marker : 각 데이터 포인트에 대한 마커 설정
# 표식 (o : 원, ^ : 삼각형, s : 사각형)
