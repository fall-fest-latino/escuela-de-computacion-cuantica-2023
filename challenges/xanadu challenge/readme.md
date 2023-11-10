# Xanadu challenge

Rotation Latin team

- Nayeli Rodriguez
- Anthony Córdoba
- Alexa Gonzalez
- María Rojas
- Brian Navarro

#### Methodology

After reading the whole challenge and understanding what was needed to work on, we started to research a gradient function that could work for our case and came across this [blog](https://pennylane.ai/blog/2022/06/how-to-choose-your-optimizer/) pointing out some functions that Pennylane offers and different applications they were better at. We chose the  *GradientDescentOptimizer* which was an optimizer we heard before and considered could work on many cases. We went this route instead of developing our own optimizer due to a lack of expertise on the subject and the constraints of time.

After selecting our optimizer, we researched the Pennylane API reference to understand how to implement it in our code. While testing our code we found out about the *QNSPSAOptimizer* class which had an example of use, so we decided to base our implementation around that example but using our previously selected optimizer.

We also used the examples shown in the Xanadu Codebook on how to Instantiate the QNode for the variational circuit. It was a very useful resource to make our code work properly.

We had some problems when trying to run the optimizer due to our lack of how the arguments of a callable function inside another function parameter works. We sorted it out with the use of the kwargs and researched in the API reference how to obtain the information we needed from the object returned from the variational circuit. Afterward, we created a new script to call our code as an imported object (which probably will be the case when Xanadu judges test our solution) to test it out with the Hamiltonians provided by the challenge.

#### Results

We were able to obtain the same value as the expected one from the Hamiltonians provided by the challenge. We also tested it with another optimizer called *AdagradOptimizer* obtaining the same result. We also tweaked the number of steps for the optimizer and shots from our device and found out that the current solution has better results on precision, accuracy, and execution time, but can vary depending on the hardware used to run the solution. 

#### Conclusions

We can conclude that Pennylane is a very powerful tool for simulating quantum devices and can be used properly without extensive knowledge of quantum computing; knowing the basics, having good skills in python, and experience working with APIs were sufficient for us to develop this solution.