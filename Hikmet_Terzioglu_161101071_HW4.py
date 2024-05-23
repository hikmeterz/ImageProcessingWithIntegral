import math

import cv2
import numpy as np
import matplotlib.pyplot as plt
def question_1():
    img = cv2.imread('./lena_grayscale_hq.jpg', 0)
    opencv_integral_image, sqsum_2 = cv2.integral2(img)
    # print(opencv_integral_image)
    #plt.imshow(opencv_integral_image, cmap='gray')
    #plt.show()


    img = cv2.copyMakeBorder(img, 1, 0, 1, 0, borderType=cv2.BORDER_CONSTANT)

    h, w = len(img), len(img[0])
    size = h,w
    integral_image = [[0 for y in range(w)] for x in range(h)]
    #integral_image = np.zeros(size, dtype=np.uint8) boyle yapinca istenilen sonucu vermiyor.


    for x in range(0,h):
        sum=0
        for y in range(0,w):
            sum += img[x][y] #rowlari topluyor.
            integral_image[x][y] = sum
            if(x>0):
                integral_image[x][y] = integral_image[x][y] + integral_image[x-1][y]
                #ilk satir disindaki
                # integral imagedeki verilen konumun bir ustunde yer alan konum bir önceki satirin o konuma kadarki toplamidir.
                #sum zaten original imagedaki o konuma kadarki toplamidir ve integral imagein o konumdan bir onceki satirin toplamini
                #alip topladigimizda o konumun alaninin toplami verilmesi amaclanmistir.

    print(abs(integral_image - opencv_integral_image) * 100)

    #plt.imshow(integral_image, cmap='gray')
    #plt.show()

def question_2():
    img = cv2.imread('./lena_grayscale_hq.jpg', 0)

    filter_window_size=3
    borderSize = math.floor(filter_window_size / 2)
    #First integral of an image.
    img = cv2.copyMakeBorder(img, 1, 0, 1, 0, borderType=cv2.BORDER_CONSTANT)

    h, w = len(img), len(img[0])
    size = h, w
    integral_image = [[0 for x in range(w)] for y in range(h)]

    for x in range(0, h):
        sum = 0
        for y in range(0, w):
            sum += img[x][y]  # rowlari topluyor.
            integral_image[x][y] = sum
            if (x > 0):
                integral_image[x][y] = integral_image[x][y] + integral_image[x - 1][y]



    #box filter uygulanacak.

    #4 addition 1 division  3x3 box filter to integral image.

    #I(D) + I(A) - I(B) -I(C) / W

    w_i = len(integral_image)
    for x in range(1,w_i-1):
        for y in range(1, w_i-1):

            integral_image[x][y] = (integral_image[x+1][y+1] + integral_image[x-1][y-1] - integral_image[x+1][y-1] - integral_image[x-1][y+1] ) / (filter_window_size*filter_window_size)

    #plt.imshow(int_img, cmap='gray')
    #plt.show()

    #print(len(integral_image))

    blur = cv2.blur(np.asarray(integral_image), (3, 3))
    #plt.imshow(blur, cmap='gray')
    #plt.show()
    #print(len(blur))

    #print(len(blur)) #?? 514 olmuyor.

    blur = blur/ blur.max()
    blur = 255 *  blur
    blurconv8 = blur.astype(np.uint8)



    print(abs(integral_image - blurconv8))


if __name__ == '__main__':
    question_1()
    question_2()
    