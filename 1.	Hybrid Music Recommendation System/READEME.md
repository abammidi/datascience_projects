
<!-- PROJECT LOGO -->
<br />
<div align="center">
<p align="center">
  <img width="460" height="auto" src="https://github.com/vivekgriri/Datascience_projects/blob/main/images/image3.jpg">
</p>


  <h1 align="center">Hybrid Music Recommendation System</h1>
  <p align="center">
    
The Problem: Content Overload and Discovery Fatigue.

The Goal: Maximize User Retention and Time Spent Listening (TSL).

The Strategy: A Hybrid Model (Demographic + Content + Collaborative).
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This project aims to explore a unified Hybrid Recommenda3on System that combines these methodologies into a cohesive engine. By utilizing a high-dimensional dataset of 89,740 unique tracks, this research examines ten core acous3c features—such as valence, energy, and danceability— to build a system that comprehensively understands the "DNA" of a song.
Additionally, it incorporates Singular Value Decomposi3on (SVD) to model collec3ve listening habits. The resulting hybrid engine provides a robust framework for personalized music discovery. This project is the complete data science process used to create this engine,from exploratory data analysis to the final performance validation of the hybrid model.


### Built With
* Python Programming using Jupiter Notebook
* sklearn.neighbors
* seaborn module

### Summary
Hybrid Music Recommendation system is create by combining below 3 layers to built a robust, multi-layered engine that solves the problem of content overload. 

* __Popularity-Based Recommendation__ This is the simplest but most essential part of the system. It asks: 'What is everyone else listening to right now?' System uses the popularity score as a proxy for quality and trendiness. This is our primary tool for solving the 'Cold Start' problem. When a new user joins the platform, we have zero data on them. We can’t analyze their vibe or their history because they don’t have one yet. By serving these top-tier trending tracks, we provide immediate value and keep them on the platform long enough to start collecting the data we need for more advanced personalization

* __Content-Based Filtering__ The second layer is Content-Based Filtering. This is where we look at the 'Acoustic DNA.' We treat every song as a point in a multi-dimensional space. If you like a song, the system uses a K-Nearest Neighbors algorithm to find its closest neighbors in that space based on Cosine Similarity. For example, if you are listening to a high-tempo, high-energy acoustic track, the model ignores the genre label and looks for other tracks with those exact characteristics. This is what allows for 'cross-genre discovery.'

* __Collaborative Filtering__ This is the most advanced layer is Collaborative Filtering, implemented via SVD, or Singular Value Decomposition. Unlike the previous layer, this doesn't care about what the song sounds like; it cares about who is listening to it. It creates a massive matrix where rows are users and columns are songs. By factorizing this matrix, the system identifies 'latent factors'—hidden patterns that connect users. If User A and User B share ninety percent of their library, the system assumes they have similar tastes. If User B listens to a new song that User A hasn't heard, the system predicts that User A will like it too.

By balancing global popularity, acoustic metadata, and social intelligence, we’ve created a system that is both broad and deeply personal.



### Steps implemented
Step 1: Load the music tracks dataset to Panda Dataframe

Step 2: Display and view details of each datasets

Step 3.1: Check Null values

Step 3.2: Merge Movies and ratings datasets

Step 3.3: Remove Timestamp, we will not need this column for user user collaborative filtering


Step 4: Build Recommendation System - Collaborative Filtering
The Demographic  filtering approach is based on user behavior to generate music recommendation System. In this, the system identifies songs features like danceability, energy, loudness, acousticness etc. and popualrity and generate recommendation for new users.

Step 5: Content-Based Filtering - This layer uses a K-Nearest Neighbors (KNN) approach. By treating each song as a vector of acoustic features (Energy, Valence, etc.), we can find the "mathematical neighbors" of a song the user likes.System uses MinMaxScaler to ensure that features like tempo (ranges up to 240) don't disproportionately influence the model compared to energy (ranges 0 to 1) and measure the Cosine Distance between vectors.

Step 6 : Collaborative Filtering- This layer predicts user interest based on "Social Intelligence." By using Matrix Factorization (SVD), the system identifies patterns in how groups of users interact with songs.
Example: If User A and User B both like Song X and Song Y, then User A is highly likely to enjoy Song Z which User B has recently discovered.

Step 7 : Compared all the model and calculate the least RMSE (Root Mean Square Error) against the number of latent factors to reommend the song.
__A truly effective system integrates all three layers.__
In a production environment, we apply a Weighted Hybrid Score:

$$Final Score = (w_1 \cdot Pop) + (w_2 \cdot Content) + (w_3 \cdot Collaborative)$$



<!-- CONTACT -->
## Contact

Your Name - [Vivek Giri linkedin](https://www.linkedin.com/in/vivekgiri01/) - girivivek01@gmail.com

Profile Link: [Vivek Giri_ProjectProfile](https://vivekgriri.github.io/VivekGiri_portfolio/)

