import theano
import numpy as np

def shared_glorot_uniform(shape, dtype=theano.config.floatX, name='', n=1):
    high = np.sqrt(6. / (np.sum(shape[:2]) * np.prod(shape[2:])))
    shape = shape if n == 1 else (n,) + shape
    return theano.shared(np.asarray(
        np.random.uniform(
            low=-high,
            high=high,
            size=shape),
        dtype=dtype), name=name)

def shared_zeros(shape, dtype=theano.config.floatX, name='', n=1):
    shape = shape if n == 1 else (n,) + shape
    return theano.shared(np.zeros(shape, dtype=dtype), name=name)

def weight_and_bias_init(shape, dtype=theano.config.floatX, name='', n=1):
    return (shared_glorot_uniform(shape, dtype=dtype, name='W_' + name, n=n), \
            shared_zeros((shape[1],), dtype=dtype, name='b_' + name, n=n))