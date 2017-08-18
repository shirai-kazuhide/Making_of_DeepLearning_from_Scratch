import numpy as np

def _numerical_gradient_no_batch(f, x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)  # f(x+h)

        x[idx] = tmp_val - h
        fxh2 = f(x)  # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2 * h)

        x[idx] = tmp_val  # 値を元に戻す

    return grad


def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)

        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)

        return grad


def gradient_descent(f, init_X, lr=0.01, step_num=100):
    x = init_X

    for i in range(step_num):
        grad = numerical_gradient(f,x)
        x -= lr * grad
    return x

def function_2(x):
    u"""
    :type x: in or float
    """

    if x.ndim == 1:
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1)


init_x = np.array([-3.0,4.0])
print(gradient_descent(function_2,init_X=init_x, lr=10.0, step_num=100))