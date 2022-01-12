## Fluctuations in Trust/Anger on Twitter during COVID-19 in Denmark

Twitter Scrape, Preprocessing & Emotion Classification:


### Twitter Script

The folder contains a python script, where tweets from 1st of march until 1st of April were scraped. In this python script, a Bert model was also trained to classify Danish text was implemented to get the sentiment of the tweets.

### PreProcessing in R

This folder contains an R Markdown that preprocesses the tweet emotions to be daily proportions of Anger/Trust.

### Analysis in R

Contains an R Markdown with the script used for the analysis in the project. This implements a Bayesian Change Point Analysis and smooths the data.

### Data

Holds the csv file of the daily propotions of anger/trust, this is what is used in the analysis script. For GDPR purposes, only the daily proportions can be published.
