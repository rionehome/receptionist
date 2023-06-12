import cv2
import time
import os

#特定のフォルダ内の写真をすべて削除する
def forget_all_memory(FOLDER, IMG):

    count = 1

    while True:
        
        img_path = FOLDER + IMG + str(count) + ".png"
        count += 1

        #画像を読む
        if os.path.isfile(img_path):
            os.remove(img_path)
            
        #存在しなければ抜ける
        else:
            break


#椅子とゲストの写真を撮影する
def memorize_chair_and_guest(FOLDER, IMG, IMG_NUM=5, TIME=1):

    count = 1 

    cap = cv2.VideoCapture(0) #カメラを開く
    start_time = time.time() #開始時刻を取得する

    #指定枚数の写真を撮影する
    while True:

        end_time = time.time() #終了時刻を取得する
        
        # 画像をキャプチャする
        ret, frame = cap.read()
        cv2.imshow('camera', frame)

        #時刻の差が指定時間を超えたら撮影する。
        if end_time - start_time > TIME:
            start_time = end_time #開始時刻の再設定

            img_path = FOLDER + IMG + str(count) + ".png" #画像の保存場所
            cv2.imwrite(img_path, frame) # 画像を保存する

            count += 1

        #指定枚数撮影後終了する
        if count > IMG_NUM:
            break

        #繰り返し分から抜けるためのif文
        key =cv2.waitKey(10)
        if key == 27:
            break


    #メモリを解放して終了するためのコマンド
    cap.release()
    cv2.destroyAllWindows()


#使用例
def main():
    
    FOLDER = "/home/ri-one/catkin_ws/src/receptionist/src/short_memory/"
    IMG = "chair_and_guest"
    IMG_NUM = 5 #[枚]
    TIME = 1 #[秒]  
    
    forget_all_memory(FOLDER, IMG)
    #memorize_chair_and_guest(FOLDER, IMG, IMG_NUM, TIME)
    
    

if __name__ == "__main__":
    main()