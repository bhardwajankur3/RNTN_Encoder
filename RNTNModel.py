import numpy as np
import utils


class RNTNModel:

    def __init__(self, dictionary):

        # use tensor?
        self.use_tensor = True

        self.dim = 25  # word vector dimension

        # regularization constants
        self.lambda_L = 0.0001
        self.lambda_W = 0.001
        self.lambda_V = 0.001

        # Params for SGD
        self.learning_rate = 0.01
        self.max_epochs = 200
        self.batch_size = 27

        # initialize parameters uniform(-r ~ r)
        self.r = 0.0001

        # constant for previously unknown word
        self.UNKNOWN_WORD = '*UNK*'

        # Word vector matrix
        self.L = np.random.randn(self.dim, len(dictionary))

        # Composition matrix W
        self.W = np.zeros((self.dim, 2*self.dim+1))
        range = 1.0 / (np.sqrt(self.dim) * 2.0)
        self.W[:, :-1] = np.random.uniform(-1*range, range, size=(self.dim, 2*self.dim))

        # Socher adds identity matrix here. Why?
        self.W[:, :self.dim] += np.identity(self.dim)
        self.W[:, self.dim:-1] += np.identity(self.dim)

        # Composition matrix V
        range = 1.0 / (4 * self.dim)
        self.V = np.random.uniform(-1*range, range, size=(2*self.dim, 2*self.dim, self.dim))

        # Keep total number of parameters for checks
        self.num_parameters = self.W.size + self.L.size
        if self.use_tensor:
            self.num_parameters += self.V.size

        # Hash table of (string) word -> (int) index in L
        self.word_lookup = dict()
        for i, word in enumerate(dictionary):
            self.word_lookup[word] = i

    # return vectorized params
    def getTheta(self):
        if self.use_tensor:
            return utils.vectorizeParams(self.L, self.W, self.V)
        else:
            return utils.vectorizeParams(self.L, self.W)

    # update parameters from theta
    def updateParamsGivenTheta(self, theta):
        assert theta.size == self.num_parameters, "[Error] input theta dim doesn't match the dimension."

        bound1 = self.L.size
        self.L = theta[:bound1].reshape(self.L.shape)
        bound2 = bound1 + self.W.size
        self.W = theta[bound1:bound2].reshape(self.W.shape)

        if self.use_tensor:
            self.V = theta[bound2:].reshape(self.V.shape)