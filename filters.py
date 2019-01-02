import cv2
import numpy as np

def main():
    file_name = input('Enter your input: ')
    original = cv2.imread(file_name, 1)
    print(original.shape)
    while(True): 
        option = int(input('filter: '))
        filtered = original.copy()
        if option is 0:
            mean_blur(original, filtered)
        elif option is 1:
            blur(original, filtered)
        elif option is 2:
            median(original, filtered)
        elif option is 3:
            cv2.destroyAllWindows()
            break
        cv2.imshow('original', original)
        cv2.imshow('filtered', filtered)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
def mean_blur(original, filtered):
    i_l = len(original)
    j_l = len(original[0])
    n = 1
    color_l = 3
    for i in range(i_l):
        for j in range(j_l):
            for k in range(color_l):
                avg = 0
                for l in range(-n, n + 1):
                    for m in range(-n, n + 1):
                        #print(i, j, k)
                        #print(i_l, j_l)
                        avg = avg + original[(i + l) % i_l, (j + m) % j_l, k]
                avg = avg / 9
                filtered[i, j, k] = avg
def blur(original, filtered):
    i_l = len(original)
    j_l = len(original[0])
    n = 2
    color_l = 3
    kernel = (1.0/273) * np.array(
            [[1, 4, 7, 4, 1],
            [4, 16, 26, 16, 4],
            [7, 26, 41, 26, 7],
            [4, 16, 26, 16, 4],
            [1, 4, 7, 4, 1]])
    for i in range(i_l):
        for j in range(j_l):
            for k in range(color_l):
                avg = 0
                for l in range(-n, n + 1):
                    for m in range(-n, n + 1):
                        #print(i, j, k)
                        #print(i_l, j_l)
                        avg = avg + original[(i + l) % i_l, (j + m) % j_l, k] * kernel[n + l, n + m]
                filtered[i, j, k] = avg
def median(original, filtered):
    med = np.zeros((9), dtype=int)
    i_l = len(original)
    j_l = len(original[0])
    color_l = 3
    for i in range(1, i_l - 1):
        for j in range(1, j_l - 1):
            for k in range(color_l):
                idx = 0
                for l in range(-1, 2):
                    for m in range(-1, 2):
                        med[idx] = original[i + l, j + m, k]
                        idx = idx + 1
                med.sort()
                filtered[i, j, k] = med[4]



if __name__ == '__main__':
    main()