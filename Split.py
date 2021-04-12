import numpy as np

def split_data(X, Y, percentage=0.7):
    """
     Split the training data into training and test set according to given percentage... 
    
    Parameters:
    --------
    X: training examples
    Y: training labels
    percentage: split data into train and test accorind to given %
    
    Returns:
    ---------    
    returns four lists as tuple: training data, training labels, test data, test labels 
    """
    
    testp=1-percentage

    #Split the data into train and test according to given fraction..

    #Creat a list of tuples according to the n-classes where each tuple will 
    # contain the pair of training and test examples for that class...
    #each tuple=(training-examples, training-labels,testing-examples,testing-labels)
    exdata=[]
    #Creat 4 different lists 
    traindata=[]
    trainlabels=[]
    testdata=[]
    testlabels=[]

    classes=np.unique(Y)

    for c in classes:
        # print c
        idx=Y==c
        Yt=Y[idx]
        Xt=X[idx,:]
        nexamples=Xt.shape[0]
        # Generate a random permutation of the indeces
        ridx=np.arange(nexamples) # generate indeces
        np.random.shuffle(ridx)
        ntrainex=round(nexamples*percentage)
        ntestex=nexamples-ntrainex
        ntrainex = int(ntrainex)
        traindata.append(Xt[ridx[:ntrainex],:])
        trainlabels.append(Yt[ridx[:ntrainex]])

        testdata.append(Xt[ridx[ntrainex:],:])
        testlabels.append(Yt[ridx[ntrainex:]])

        #exdata.append((Xt[ridx[:ntrainex],:], Yt[ridx[:ntrainex]], Xt[ridx[ntrainex:],:], Yt[ridx[ntrainex:]]))


    # print traindata,trainlabels
    Xtrain=np.concatenate(traindata)
    Ytrain=np.concatenate(trainlabels)
    Xtest=np.concatenate(testdata)
    Ytest=np.concatenate(testlabels)
    return Xtrain, Ytrain, Xtest, Ytest
