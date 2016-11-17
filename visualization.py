
import matplotlib.pyplot as plt
import time

'''
The visualization class is responsible for visualizing
'''

class Visualization:

    def visualize_losses(self, train_loss, val_loss):
        assert(len(train_loss) == len(val_loss))
        epochs = [i for i in range(1,len(train_loss)+1)]
        plt.plot(epochs, train_loss, 'bs', label="training loss")
        plt.plot(epochs, val_loss, 'ro', label="validation loss")
        plt.xlabel("epochs")
        plt.ylabel("loss")
        #plt.show()
        timestamp = int(time.time())
        plt.savefig("losses_" + str(timestamp) + ".png")
        plt.show()

    def visualize_accuracy(self, accuracy):
        epochs = [i for i in range(1,len(accuracy)+1)]
        plt.plot(epochs, accuracy, 'bs')
        plt.xlabel("epochs")
        plt.ylabel("accuracy")
        plt.show()
