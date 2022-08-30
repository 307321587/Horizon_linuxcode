import cv2
# 打开摄像头并显示
capture = cv2.VideoCapture(8)
while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    cv2.imshow('frame', frame)
    # 如果输入q，则退出
    if cv2.waitKey(1) == ord('q'):
        break