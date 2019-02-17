# The Danger Zone: A TreeHacks 2019 Project 

##### by Claudia Zhu, Daniel McCormick, Eric Han, and Sophie Wu

## What is this program?

This project is designed under the *safety* panel of Treehacks this year, using *open public safety data*, 
*machine learning/deep learning*, and using *Esri APIs and SDKs*. As such, we're taking a fairly simple
approach to addressing this.

This is done first by grabbing data in CSV form from public facing historical crime data from 
[data.sfgov.org](https://data.sfgov.org/api/views/q6gg-sa2p/rows.csv?accessType=DOWNLOAD).

Using this CSV module, this is parsed and relevant information is extracted from it to be used in our program,
and written to new files. This new information is then directly parsed into NumPy arrays, which then provide
training data for our neural network to process and can be used to predict more information.

We then use Esra to display the heatmaps for the present crime rates, and can, given points in a valid range 
inference the severity of crime likely occuring in the area.

By doing so, people can figure out which areas are (relatively) dangerous and which are save to adventure through.


**Tl;Dr**: Predictive model for crime based off historical data

You can learn more about our project [here](https://docs.google.com/presentation/d/1XxkbqphVjHbJC1_qv0HHqiGJSVYRYX2Qyxyqj460W6s/edit?usp=sharing)
