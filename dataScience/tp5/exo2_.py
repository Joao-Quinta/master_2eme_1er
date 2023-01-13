import numpy as np
import time
from matplotlib import pyplot as plt
import pandas as pd


# Define a class for the channel:
class Message:
    def __init__(self, M, nWordsString, rate, perror, input_message):
        # The size of the alphabet
        self.M = M
        self.nWordsString = nWordsString
        self.rate = rate
        # Probability of error (a flip of a bit)
        self.perror = perror
        # The length of the binary description of the words in the alphabet
        self.n = self.rate * self.M
        self.input_message = input_message

    # Function to simulate the error
    def check_error(self, bit):
        # Choose a random number in 0,1 is > 0.1 => no error return the bit itself
        if np.random.rand() > self.perror: return bit
        # else return 1-bit => a flip of the bit
        return 1 - bit

    def bsc(self, bits):
        bf = np.vectorize(self.check_error)
        return bf(bits)

    # Compute the communication rate
    def communicationRate(self):
        return np.log2(2 ** self.M) / self.n

    def startCommunication(self):

        start = time.time()
        # Add the redondancy, for example if msg is [0110] and rate=3 => [000111111000]
        preprocessed_message = np.repeat(self.input_message, self.rate)
        output_bsc = self.bsc(preprocessed_message)

        # Decoding the output message
        output_message = np.ndarray.astype(np.sum(output_bsc.reshape((-1, self.rate)), 1) > rate / 2, 'int')
        transmission_time = time.time() - start


        # Convert bits to words for the input and the output message
        input_words = np.dot(self.input_message.reshape((-1, self.M)), 2 ** np.arange(self.M)[::-1])
        output_words = np.dot(output_message.reshape((-1, self.M)), 2 ** np.arange(self.M)[::-1])

        # Fraction of Error
        nbrError = np.sum(input_words != output_words) / len(input_words)

        return nbrError, transmission_time, self.communicationRate()


def plot(data):
    fig, ax1 = plt.subplots()
    ax1.set_xlabel(data['x'])
    ax1.set_ylabel(data['y1'], color='pink')
    ax1.plot(data[data['x']], data[data['y1']], color='pink', marker='.', markersize=10)
    ax1.tick_params(axis='y', labelcolor='pink')
    ax2 = ax1.twinx()
    ax2.set_ylabel(data['y2'], color='purple')
    ax2.plot(data[data['x']], data[data['y2']], color='purple', marker='.', markersize=10)
    ax2.tick_params(axis='y', labelcolor='purple')
    fig.tight_layout()


# Starting--------------------------------------------------------------------

# Initialization of values
rates = [1, 3, 5, 11, 23]
perror = 0.1
nWordsString = 1000
m = 32
M = int(np.ceil(np.log2(m)))
# A dictionnary with keys
# We will stock the informations inside each list
results = {'Rates = [1,3,5,11,23]': [], 'Error': [], 'Transmission time': [], 'Rate of communication': []}

# Generate the input msg: choose nWordsString*M times a int in [0,2[
input_message = np.random.randint(0, 2, nWordsString * M)

# Sending message
for rate in rates:
    pe, tt, r = Message(M, nWordsString, rate, perror, input_message).startCommunication()
    results['Rates = [1,3,5,11,23]'].append(rate)
    results['Error'].append(pe)
    results['Transmission time'].append(tt)
    results['Rate of communication'].append(r)

# Showing the results
pd_results = pd.DataFrame.from_dict(results)
print(pd_results)

# plot 1
results['x'] = 'Rate of communication'
results['y1'] = 'Error'
results['y2'] = 'Transmission time'
plot(results)

# plot 2
results['x'] = 'Rates = [1,3,5,11,23]'
plot(results)
plt.show()