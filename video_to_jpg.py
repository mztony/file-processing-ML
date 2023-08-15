import cv2

def video2images(Video_Dir):
    """
    function: video to pictures
    author: AIJun
    date:2021/3/17
    """
    cap = cv2.VideoCapture(Video_Dir)
    c = 1  # 帧数起点
    index = 1  # 图片命名起点，如1.jpg
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # 帧高度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # 帧速度
    while True:
        # 逐帧捕获
        ret, frame = cap.read()
        # 如果正确读取帧，ret为True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        if c % 5 == 0:
            leftframe = frame[0:height, 0:int(width / 2)]
            rightframe = frame[0:height, int(width / 2):width]
            allframe = frame
            cv2.imwrite('/home/viewer/Downloads/model_zoo/bj/2-3/left/' + '012-'+ str(index) + '.jpg', leftframe)
            #cv2.imwrite('/home/viewer/Downloads/model_zoo/0626/12_3/right/' + str(index) + '.jpg', rightframe)
            #cv2.imwrite('/home/viewer/Downloads/model_zoo/0620/' + str(index) + '.jpg', allframe)
            print(index)
            index += 1
        c += 1
        cv2.waitKey(1)
        # 按键停止
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()

Video_Dir = "/home/viewer/Downloads/model_zoo/bj/mz2-3.012.mkv"
video2images(Video_Dir)

