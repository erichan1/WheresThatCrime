# The Danger Zone: A TreeHacks 2019 Project 

##### by Claudia Zhu, Daniel McCormick, Eric Han, and Sophie Wu

### What is this program?

This project is designed under the *safety* vertical of Stanford's 2019 Treehacks. For this project, our team used *open public safety data*, *machine learning/deep learning*, and *Esri APIs and SDKs* to develop a heat map for how dangerous certain areas are for pedestrians and then suggest a safest path route. 

### Motivation

For approximatley the past 20 years, only 37% of Americans feel safe walking home at night (Gallup Polls). Despite major technological advances, we have not been able to eliminate this issue. Recently, CMU startup [PredPol](predpol.com) as well as other tech companies have started dabbling in predictive policing. We hope to address this issue from the perspective of the everyday citizen by developing a software to suggest the safest route between destinations. 

### Methodology 

We create our dataset by grabbing data in CSV form from public facing historical crime data from 
[data.sfgov.org](https://data.sfgov.org/api/views/q6gg-sa2p/rows.csv?accessType=DOWNLOAD).

The data, which consists of date, location, and severity of crime, is then parsed as a new file using this CSV module to extract relevant information for our program. This new information is then directly parsed into NumPy arrays and serve as training data for our neural network so that we can predict future location/severity of crimes. Note that this is a valid correlation as shown by numerous studies, namely the [2008 UChicago study on predictive crime analysis](https://chicagounbound.uchicago.edu/cgi/viewcontent.cgi?article=1374&context=law_and_economics). 

We then use Esra to display the heatmaps for the present crime rates. Given points in a valid range, we are also able to inference the severity of crime likely occuring in the area. Furthermore, we were able to generate the safest path based on our Danger Index metric. 

With this project, we hope that people can easily and unstressfully figure out which areas are (relatively) dangerous and which are safe to adventure through.


**Tl;Dr**: Predictive model for crime based off historical data

You can learn more about our project [here](https://docs.google.com/presentation/d/1XxkbqphVjHbJC1_qv0HHqiGJSVYRYX2Qyxyqj460W6s/edit?usp=sharing)
