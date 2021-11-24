import numpy as np
import cv2
import vektor           # untuk cari nilai dan vektor eigen

def matrixSVD(M):
# mendekomposisi M menjadi U, s, dan V_T
    M_T = np.transpose(M)       # transpose(M)
    M_M_T = np.dot(M, M_T)      # M*transpose(M)
    M_T_M = np.dot(M_T, M)      # transpose(M)*M