import os
import cv2


def video_frame(input, output):
    if not os.path.exists(output):
        os.mkdir(output)
    times = 0
    frame_frequency = 10
    count = 0
    cap = cv2.VideoCapture(input)
    print('video loading', input, 'video image')
    while (True):
        times += 1
        res, image = cap.read()
        if not res:
            print('loading finishing')
            break
        if times % frame_frequency == 0:
            img_name = str(count).zfill(6) + '.jpg'
            # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            size=cv2.resize(image,(360,480))
            cv2.imwrite(output + os.sep + img_name, image)
            count += 1

    # print(output + os.sep + img_name)
    cap.release()


def video_defined_frame(input, output, start, end=-1):
    if not os.path.exists(output):
        os.mkdir(output)
    
    times = 0
    frame_frequency = 10
    count = 0
    cap = cv2.VideoCapture(input)
    cap.set(cv2.CAP_PROP_POS_FRAMES,float(start))
    print('video loading', input, 'video image')

    if end == -1:
        print('loading',input,'from',start,' frame to the end frame')
        while (True):
            times += 1
            res, image = cap.read()
            if not res:
                print('loading finishing')
                break
            if times % frame_frequency == 0:
                img_name = str(count).zfill(6) + '.jpg'
                # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                size=cv2.resize(image,(360,480))
                cv2.imwrite(output + os.sep + img_name, image)
                count += 1
    else:
        print('loading', input, 'from', start, ' frame to', end, ' end frame')
        k = end - start + 1
        while (k >= 0):
            times += 1
            k -= 1
            res, image = cap.read()
            if not res:
                print('loading finishing')
                break
            if times % frame_frequency == 0:
                img_name = str(count).zfill(6) + '.jpg'
                # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                size=cv2.resize(image,(360,480))
                cv2.imwrite(output + os.sep + img_name, image)
                count += 1

    # print(output + os.sep + img_name)
    cap.release()

def show_frame(path,index):
    cap = cv2.VideoCapture(path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, float(index))
    if cap.isOpened():
        val, frame = cap.read()
        cv2.imshow('image:' + str(index) , frame)
        cv2.waitKey()
        cap.release()


if __name__ == '__main__':
    input = 'D://Code_Workspace_python/opencv/example_driven_guide_opencv/src/video/video_example/Sample of output.mp4'
    output = 'D://Code_Workspace_python/opencv/example_driven_guide_opencv/src/video/image_example'
    show_frame(input, 4)
    # video_frame(input, output)
    video_defined_frame(input, output, 0, 70)
    
    
    
