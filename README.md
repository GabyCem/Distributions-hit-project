
# Distributions-hit

In this project we will predict the choices made by people given a limited amout of data using machine learning.
The project is divided into three parts: 

# Part A - Collecting  data
In this part of the project, data is collected using crawlers from various websites.

The crawlers used specific Xpaths to iterate over the required product information and exported the data to a CSV file.
As you can see in the picture below.





![App Screenshot](https://i.imgur.com/MLfpcNp.png)

The final output file could be seen in /Crawlers/amazon_headphones/amazon_headphones.csv


# Part B - Creating a website
The website link - https://distribution-hit-survey.herokuapp.com

The website will be the platform in which a user can choose between two rating distributions  

![App Screenshot](https://i.imgur.com/Hd6AI47.png)

The website was created based on MERN (MongoDB, Express, React, NodeJS) architecture.

### Server side
The server grants the data collected by the crawlers using a shared API with the client.

Using the following GET API, the server exposes the data to the client. With this data the client can display it as seen in the image above.

![App Screenshot](https://i.imgur.com/8oi6FdS.png)

Using the following POST API, all of the experiment data will be exported to MongoDB.

![App Screenshot](https://i.imgur.com/PZTA9eA.png)

When the 1st API request is sent, the time of the request is recorded. When the session is complete the total time is exported to MongoDB as well.

In ExperimentData.js we implemented the parsing of the data. Moreover we implemented the logic of the "/experimentdata" GET API.

### Client side
The client side is implemented as a React application, and it is divided into two parts:

* The registration step.
* The experiment step.

The AppRouter.js is responsible for the routing of the application.

In ExperimentService.js a singleton constructor is implemented, in which the data is requested only once and saved during the entire process.

![App Screenshot](https://i.imgur.com/lG4jWY5.png)

# Part C - Machine learning
In this part we use a machine learning algorithm. The algorithm takes part of the data collected from the users, it will train the model on it. Afterwards it will take the other part of the data and test the models accuracy on it.

We used Decision Trees (DTs) as the machine learning algorithm, which are a non-parametric supervised learning method used for classification and regression.

The attributes of the tree are the graphs columns (1 star, 2 star etc.), and the leaves are the right or left distribution.