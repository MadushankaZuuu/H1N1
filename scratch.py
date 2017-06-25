import math
class Connection:
    def __init__(self, connectedNeuron):
        self.connectedNeuron=connectedNeuron
        self.weight=0.1
        self.deltaWeight=0

class Neuron:
    eta=0.9 # learning rate
    alpha=0.15 # momentum rate

    def __init__(self,layer):
        self.dendrons=[]
        self.error=0.0
        self.output=0.0
        self.gradient=0.0
        if(layer in None):
            pass
        else:
            for neuron in layer:
                con=Connection(neuron)
                self.dendrons.append(con)

    def addError(self,er):
        self.error==self.error+er

    def sigmoid(x):
        return 1/(1+math.exp(-x))

    def dSigmoid( self, x):
        return x*(1-x)

    def feedForward(self):
         sumOfOutput=0.0
         for dendron in self.dendrons:
             sumOfOutput=sumOfOutput+dendron.connectedNeuron.output*dendron.weight
         self.output=sigmoid(sumOfOutput)

    def BackPropagate():
        self.gradient=self.error*dSigmoid(self.output)
        for dendron in self.dendrons:
            dendron.deltaWeight=Neuron.eta*(dendron.connectedNeuron.output*self.gradient)+ (Neuron.alpha*dendron.deltaWeight)
            dendron.weight=dendron.weight+dendron.deltaWeight
            dendron.connectedNeuron.addError(self.gradient*dendron.weight)
        self.error=0.0;





