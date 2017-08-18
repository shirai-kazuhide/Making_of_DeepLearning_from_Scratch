import gradient_descent
import numpy as np

def cross_entropy_error(y,t):
    """
    正解ラベルyとPredictラベルtのクロスエントロピーを計算する
    :param y:
    :param t:
    :return:
    """
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

t = [0,0,1]
y = [0.1,0.05,0.6]

print(cross_entropy_error(np.array(y),np.array(t)))

