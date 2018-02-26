
import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
#from lr_utils import load_dataset






# GRADED FUNCTION: propagate

def propagate(w, b, X, Y):
    """
    Implement the cost function and its gradient for the propagation explained above

    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of size (num_px * num_px * 3, number of examples)
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat) of size (1, number of examples)

    Return:
    cost -- negative log-likelihood cost for logistic regression
    dw -- gradient of the loss with respect to w, thus same shape as w
    db -- gradient of the loss with respect to b, thus same shape as b
    
    Tips:
    - Write your code step by step for the propagation. np.log(), np.dot()
    """
    
    m = X.shape[1]

    #print("\n\n\nThis is m:{}".format(m))
    
    # FORWARD PROPAGATION (FROM X TO COST)
    ### START CODE HERE ### (≈ 2 lines of code)
    a = np.dot(w.T,X)+b                                    # compute 
    #A = A.reshape(3,1)

    #print("\n\n\nThis is A:{}".format(A))
    #print("\nThis is A shape:{}".format(A.shape))
    A = 1/(1+np.exp(-a))
    #a = a.reshape(3,1)

    #print("\n\n\nThis is Y:{}\n".format(Y))
    #print("\nThis is y shape:{}\n\n".format(Y.shape))
    cost1 = (Y*np.log(A))+((1-Y)*(np.log(1-A)))
    cost1 = np.sum(cost1)
    print("this is cost1"+str(cost1))
    cost =  (-1/m)*cost1 # compute cost
    ### END CODE HERE ###
    
    # BACKWARD PROPAGATION (TO FIND GRAD)
    ### START CODE HERE ### (≈ 2 lines of code)
    dw = (1/m)*np.dot(X,(A-Y).T)

    #print("\n\n\n dw is {} shape: {}".format(dw, dw.shape))
    db = (1/m)*np.sum(A-Y)

    #print("\n\n\n db shape: {}".format(db.shape))
    ### END CODE HERE ###

    assert(dw.shape == w.shape)
    assert(db.dtype == float)
    cost = np.squeeze(cost)
    assert(cost.shape == ())
    
    grads = {"dw": dw,
             "db": db}
    
    return grads, cost


w, b, X, Y = np.array([[1.],[2.]]), 2., np.array([[1.,2.,-1.],[3.,4.,-3.2]]), np.array([[1,0,1]])

#print("\n\n\nW: {}".format(w))

#print("\n\n\nb: {}".format(b))

#print("\n\n\nX: {}".format(X))
#print("\n\n\nY: {}".format(Y))
grads, cost = propagate(w, b, X, Y)
print ("dw = " + str(grads["dw"]))
print ("db = " + str(grads["db"]))
print ("cost = " + str(cost))


