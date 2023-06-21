import cv2
import os

def img_compose(FOLDER, IMG):
    """
    stitchingモジュールを使用した場合
    """

    count = 1 #画像が何枚目かを数える
    img_list = [] #合成する画像のリスト

    #フォルダに存在する画像をすべて読み込む
    while True:
        img_path = FOLDER + IMG + str(count) + ".png"
        count += 1

        #画像を読む
        if os.path.isfile(img_path):
            img = cv2.imread(img_path)
            img_list.append(img)
        
        #存在しなければ抜ける
        else:
            break

    print("len(img_list)=" + str(len(img_list)))

    stitcher = cv2.Stitcher_create()
    img_stitched = stitcher.stitch(img_list)[1]
    
    return img_stitched
    #cv2.imwrite(FOLDER + "stiched_img.png", img_stitched)

    # 合成画像を表示
    #cv2.imshow('stiched_img', img_stitched)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


def main():
    
    FOLDER = "/home/ri-one/catkin_ws/src/receptionist/src/short_memory/"
    IMG = "chair_and_guest"
    
    img_stitched = img_compose(FOLDER, IMG)
    
    #cv2.imwrite(FOLDER + "stiched_img.png", img_stitched)

    # 合成画像を表示
    cv2.imshow('stiched_img', img_stitched)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    

if __name__ == "__main__":
    main()