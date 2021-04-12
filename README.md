# KNN & LinearRegressionFrom-Scratch
## K Nearest Neighbours
* Downloaded the Iris Dataset.
* Loading the Dataset into Pandas Dataframe.
* Dividing the data into Test & Train (70 30).
* Creating a class KNN
* Function Predict() predicts the output.
* Function Compute Distance() compute the distance between sample and all other data and return the distance vector.
* Function Fit() starts training the Model.
## Linear Regression
* Loading the Dataset into Pandas Dataframe.
* Dividing the data into Test & Train (70 30).
* def hyp(X,theta) performs mx in y = mx
* def cost_function(theta,X,Y) returns the error in the prediction. 
* def derivative_cost_function(theta,X,Y,alpha) finds the derivative.
* def GradientDescent(X,Y,thetas,cost_function,derivative_cost_function,maxniter=20000) it's the learning algorithm, which keeps on running until 20000 iterations.
