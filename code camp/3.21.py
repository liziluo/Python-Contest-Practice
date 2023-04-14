from PIL import Image
import numpy as np
import cv2
import os
 
 
# 切割图片
def splitimage(src, rownum, colnum, dstpath, arr):
    img = Image.open(src)
    w, h = img.size
    if rownum <= h and colnum <= w:
        print('原图基本信息:宽:{}px,高:{}px,图片格式:{}'.format(w, h, img.format))
        print('图片切割开始处理, 请稍候...')
        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]
        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                img.crop(box).save(os.path.join(dstpath, rewrite_filename(arr.pop()) + '.' + ext), ext)
                num = num + 1
 
        print('图片切割完成，共生成 {}张小图片'.format(num))
    else:
        print('行列切割参数不合法')
 
 
# 合并图片
def merge_picture(merge_path, num_of_cols, num_of_rows):
    filename = file_name(merge_path, ".png")
    shape = cv2.imread(filename[0], -1).shape  # 三通道的影像需把-1改成1
    cols = shape[1]
    rows = shape[0]
    channels = shape[2]
    dst = np.zeros((rows * num_of_rows, cols * num_of_cols, channels), np.uint8)
    for i in range(len(filename)):
        img = cv2.imread(filename[i])
        m, n = filename[i].split("\\")[-1].split(".")[0].split("_")
        cols_th = int(n)
        rows_th = int(m)
        roi = img[0:rows, 0:cols, :]
        dst[rows_th * rows:(rows_th + 1) * rows, cols_th * cols:(cols_th + 1) * cols, :] = roi
    cv2.imwrite(merge_path + "merge.png", dst)
 
 
# 遍历文件夹下的图片
def file_name(root_path, picturetype):
    filename = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if os.path.splitext(file)[1] == picturetype:
                filename.append(os.path.join(root, file))
    return filename
 
 
# 重写文件名称
def rewrite_filename(num):
    num = int(num)
    if (num < 10):
        return "0_{}".format(num)
    else:
        i = num % 10
        return "1_{}".format(i)
 
 
if __name__ == '__main__':
    # 正确的文件块顺序
    arr = "18,13,9,5,3,10,2,7,19,14,6,1,12,17,11,0,8,15,4,16".split(",")
    arr.reverse()
    # 切割图片
    splitimage(r'C:\vdemo\img\code.png', 2, 10, r'E:\vdemo\img\file', arr)
    # 合并图片
    merge_picture(r'E:\vdemo\img\file', 10, 2)

# from skimage import data
# from matplotlib import pyplot as plt
# import numpy as np

# astronaut = data.astronaut()
# coffee    = data.coffee()

# arr = np.stack([coffee[:400, :400, :], astronaut[:400, :400, :]])
# plt.imshow(arr[0])
# plt.title('arr[0]')
# plt.figure()
# plt.imshow(arr[1])
# plt.title('arr[1]')
# arr_blocks = arr.reshape(arr.shape[0], 4, 100, 4, 100, 3, ).swapaxes(2, 3)
# arr_blocks = arr_blocks.reshape(-1, 100, 100, 3)


# for i, block in enumerate(arr_blocks):
#     plt.figure(10+i//16, figsize = (10, 10))
#     plt.subplot(4, 4, i%16+1)
#     plt.imshow(block)
#     plt.title(f'block {i}')


    

# batch_size = 9
# some_outputs_list = []
# for i in range(arr_blocks.shape[0]//batch_size + ((arr_blocks.shape[0]%batch_size) > 0)):
#     some_outputs_list.append(some_function(arr_blocks[i*batch_size:(i+1)*batch_size]))
