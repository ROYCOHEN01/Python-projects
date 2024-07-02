''' Exercise #9. Python for Engineers.'''

import numpy as np
import imageio
import matplotlib.pyplot as plt


#########################################
# Question 1 - do not delete this comment
#########################################

def load_training_data(weights_file, heights_file):
    f = open(weights_file, 'r')
    g = open(heights_file, 'r')
    new_weight = np.genfromtxt(f, delimiter=',', dtype= None, encoding= 'utf-8')
    table = {}
    table['data'] = new_weight[1:,1:].astype(float)
    table['column_names'] = new_weight[0,1:]
    table['row_names'] = new_weight[1:,0]

    new_height = np.genfromtxt(g, delimiter=',',dtype= None, encoding= 'utf-8')
    counter = 1
    sec_table = {}
    for i in new_height[1:,0]:
        sec_table[i] = new_height[counter,1].astype(int)
        counter = counter + 1

    f.close()
    g.close()
    return table, sec_table

def get_highest_weight_loss(data_dict,axis= None, out= None):
    f_max = data_dict['data']
    f_max_new = np.transpose(f_max)
    max = f_max_new[0] - f_max_new[-1]
    names = data_dict['row_names']
    return names[np.argmax(max)]



def get_bmi(weights_data, heights_data):
    weight = weights_data['data'].copy()
    name = weights_data['row_names'].tolist()
    bmi = weight.copy()
    for elem in name:
        for key in heights_data.keys():
            if elem == key:
                bmi[name.index(key)] = bmi[name.index(key)]/((heights_data[key]/100)**2)
    bmi = np.round(bmi, 2)
    return bmi.copy()


def get_bmi_diff(weights_data, heights_data):
    a = get_bmi(weights_data, heights_data).copy()
    c = np.diff(a)
    return c

def get_highest_bmi_loss_month(weights_data, heights_data):
    b = get_bmi_diff(weights_data, heights_data)
    c = np.sum(b, axis = 0)
    max_month_key = np.argmax(c)
    max_month = weights_data['column_names'][max_month_key]
    return max_month


def get_relative_diff_table(weights_data, heights_data):
    a = get_bmi_diff(weights_data,heights_data)
    b = get_bmi(weights_data, heights_data)
    c = a/b[0:,:-1]
    c = np.round(c,3)
    return c



#########################################
# Question 2 - do not delete this comment
#########################################

def compute_entropy(img):
    im = imageio.imread(img)
    a = np.array(im)
    counter = 0
    sum = 0
    for i in range(0, 256):
        counter = np.count_nonzero(i==im)/a.size
        log = np.log2(counter)
        sum += (-counter * log)
    return np.round(sum , 4)



#########################################
# Question 3 - do not delete this comment
#########################################

def load_image_as_matrix(img_path):
    image = np.array(imageio.imread(img_path)).copy()
    return image

def binarize_matrix(mat):
    tresh = 128
    b = mat.copy()
    b[b < tresh] = 0
    b[b >= tresh] = 1
    return b

def compress_flatten_rle(mat):
    newmat = mat.copy()
    mat_flatten = newmat.flatten()
    print(mat_flatten[0:50])
    count = 0
    t = 0
    rle_mat = np.empty(0)
    for i in mat_flatten:
        if i == t:
            count +=1
        else:
            t = i
            rle_mat = np.append(rle_mat , count)
            count = 1
    rle_mat = np.append(rle_mat, count)
    print(rle_mat[0:10])
    return rle_mat, mat.shape

def decompress_flatten_rle(mat_rle_compressed, shape):
    back_mat = np.empty(0)
    d = 0
    if mat_rle_compressed[0] == 0:
        mat_rle_compressed =mat_rle_compressed[1:]
        d = 1
    for n in mat_rle_compressed.tolist():
        back_mat = np.append(back_mat, np.repeat(d,n))
        if d != 0 :
            d = 0
        else:
            d = 1
    back_mat = back_mat.reshape((shape[0], shape[1]))
    return back_mat
def calc_compression_ratio(mat_rle_compressed, mat):
    compressed = mat_rle_compressed.size/ mat.size
    return round(compressed,2)


    
if __name__ == '__main__':

      print('==== Q1: Basic tests/output====')
      weights, heights = load_training_data("weights.csv", "heights.csv")
      print(f'load_training_data:\n {weights}\nheight_data: {heights}\n======')
      print(f'get_highest_weight_loss:\n {get_highest_weight_loss(weights)}\n======')
      print(f'get_bmi:\n {get_bmi(weights, heights)}\n======')
      print(f'get_bmi_diff:\n {get_bmi_diff(weights, heights)}\n======')
      print(f'get_highest_bmi_loss_month:\n {get_highest_bmi_loss_month(weights, heights)}\n======')
      print(f'get_relative_diff_table:\n {get_relative_diff_table(weights, heights)}\n======')
     

      print('==== Q2: Write your sanity check/output here!====')
      print(compute_entropy('rick_and_morty_gray.png'))

      print('==== Q3: Basic/output====')

      img_original=load_image_as_matrix('rick_and_morty_gray.png')
      img=binarize_matrix(img_original)
      mat_rle_compressed, shape=compress_flatten_rle(img)
      mat_rle_decompressed=decompress_flatten_rle(mat_rle_compressed, shape)

      fig, axs= plt.subplots(1, 3, figsize=(30,10))
      axs[0].set_title("original_image")
      axs[0].imshow(img_original,cmap = plt.cm.gray)
      axs[1].set_title("binarized_image")
      axs[1].imshow(img,cmap = plt.cm.gray)
      axs[2].set_title("decompressed_image")
      axs[2].imshow(mat_rle_decompressed,cmap = plt.cm.gray)
      plt.show()

      print(f'Are decompreseed and original matrices identical? {np.all((img==mat_rle_decompressed))}')
      print(f'calc_compression_ratio: {calc_compression_ratio(mat_rle_compressed, img)}')


      img_original=np.array([[0,0,0,0,200,200,0,0,0,0,0,200,200,0,0,0,0], 
                    [0,0,0,200,200,200,200,0,0,0,200,201,200,200,0,0,0], 
                    [0,0,200,1,1,1,1,200,0,200,200,200,1,1,200,0,0], 
                    [0,200,1,100,1,101,1,200,200,1,1,1,1,101,1,200,0], 
                    [0,200,1,1,1,200,1,1,1,21,1,101,1,150,1,200,0], 
                    [0,200,1,101,100,1,100,1,10,1,1,100,100,1,1,200,0], 
                    [0,200,1,200,1,201,1,1,1,1,201,1,1,100,1,200,0], 
                    [0,200,1,1,1,1,1,21,1,1,1,1,21,1,1,200,0], 
                    [0,0,200,1,101,1,1,1,250,1,200,1,1,1,200,0,0], 
                    [0,0,0,200,200,1,200,1,1,1,1,10,1,200,0,0,0], 
                    [0,0,0,0,200,1,1,1,1,10,1,1,200,0,0,0,0], 
                    [0,0,0,0,0,170,1,10,1,1,1,200,0,0,0,0,0], 
                    [0,0,0,0,0,0,230,1,1,1,200,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,200,1,200,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,200,0,0,0,0,0,0,0,0]])

      img=binarize_matrix(img_original)
      mat_rle_compressed, shape=compress_flatten_rle(img)
      mat_rle_decompressed=decompress_flatten_rle(mat_rle_compressed, shape)
      print(f'Are decompreseed and original matrices identical? {np.all((img==mat_rle_decompressed))}')
      print(f'calc_compression_ratio: {calc_compression_ratio(mat_rle_compressed, img)}')

      fig, axs= plt.subplots(1, 3, figsize=(30,10))
      axs[0].set_title("original_image")
      axs[0].imshow(img_original,cmap = plt.cm.gray)
      axs[1].set_title("binarized_image")
      axs[1].imshow(img,cmap = plt.cm.gray)
      axs[2].set_title("decompressed_image")
      axs[2].imshow(mat_rle_decompressed,cmap = plt.cm.gray)
      plt.show()
