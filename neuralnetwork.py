import keyword
keyword.kwlist
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
        if(layer is None):
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
        if(len(self.dendrons)==0):
            pass
        sumOfOutputs=0.0
        for dendron in self.dendrons:
            sumOfOutputs=sumOfOutputs+dendron.connectedNeuron.output*dendron.weight
        self.output=self.sigmoid(sumOfOutputs)

    def BackPropagate():
        self.gradient=self.error*self.dSigmoid(self.output)
        for dendron in self.dendrons:
            dendron.deltaWeight=Neuron.eta*(dendron.connectedNeuron.output*self.gradient)+ (Neuron.alpha*dendron.deltaWeight)
            dendron.weight=dendron.weight+dendron.deltaWeight
            dendron.connectedNeuron.addError(self.gradient*dendron.weight)
        self.error=0.0;

class Net:
    def __init__(self,topology):
        self.layers=[]
        for numNeuron in topology:
            layer=[]
            for i in range(numNeuron):
                if(len(self.layers)==0):
                    neuron=Neuron(None)
                else:
                    neuron=Neuron(self.layers[-1])
                layer.append(neuron)
            layer.append(Neuron(None))
            layer[-1].output=1
            self.layers.append(layer)

    def setInputs(self,inputs):
        for i in range(len(inputs)):
            self.layers[0][i].output=inputs[i];


    def feedForward(self):
        for layer in self.layers:
            for neuron in layer:
                 neuron.feedForward();

    def backPropagate(self,targets):
        for i in range(len(targets)):
            self.layers[-1][i].error=targets[i]-self.layerws[-1][i].output;

        for layer in self.layers[::-1]:
            for neuron in layer:
                neuron.backPropagate();

    def getError(self,targets):
        avgErr=0
        for i in range(len(targets)):
            err=targets[i]-self.layerws[-1][i].output;
            avgErr=avgErr+(err*err)
        avgErr=avgErr/len(targets)
        return avgErr

    def getOutputs(self):
        outputs=[]
        for neuron in self.layers[-1]:
            outputs.append(neuron.output)
    
            
def main():
    net=Net([2,3,5,1])
    inputs=[[0,0],[0,1],[1,0],[1,1]]
    outputs=[[0],[1],[1],[1]]
    while True:
        err=0
        for i in range (len(inputs)):
            print (inputs[i])
            net.setInputs(inputs[i])
            net.feedForward();
            net.backPropagate(outputs[i])
            err=err+net.getError(outputs[i])
            print net.getOutputs()
            print net.getError(outputs[i])
        err=err/len(inputs)
        if(err<0.01):
            break;

    while True:
        i1=input("enter first input")
        i2=input("enter first input")
        i=[i1,i2]
        net.setInputs(i)
        net.feedForward()
        print net.getOutputs()

if __name__=="__main__":
    main()
            
                





                    





