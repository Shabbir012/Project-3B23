# Project-3B23
Project 3 GitHub Repository
This project is about sentiment analysis using a multi modal dataset gotten from websites, pdfs and podcasts. As a case study, a company called "Tango Eye" was chosen and the problem statement revolved around it.

# Problem Statement
In response to Tango Eye's interest in exploring a new domain, the metaverse, as data analysts we are tasked with conducting a comprehensive data analysis on a multi-modal dataset. The insights gained would inform Tango Eye's decision-making process.​

The CRISP-DM methodology was followed for the successful completion of this project. This is a diagram showing all the various stages and how it was implemented in this project.

![CRISP-DM](https://github.com/Shabbir012/Project-3B23/assets/152379444/4bfd875d-7ae9-42c3-8efa-15e0d8e15021)


# Functional and Non functional requirements
Functional requirements: 

- Install libraries for web scraping, speech to text and machine learning task.​

- Get a multi modal dataset from various sources like websites, podcasts and social media. ​

- Cleaning the dataset​

- Labelling the dataset using a pretrained model​

- Data understanding using exploratory data analysis​

- Building a machine learning model using various models and feature engineering methods​

- Model tuning by changing the train: test ratio and various hyperparameters​

- Evaluating models using various metrics like Precision, Recall, Accuracy​
  
Non-functional requirements: 

- Access to the internet when working with google colab​

- Getting a Deep gram API​

- Installing necessary libraries in the environment when working with PyCharm​

- Running the speech-to-text code in PyCharm or Python shell​

# Web Scraping
Web scraping involves getting data from various web pages/social media whether structured and unstructures and using it to inform decision making, gain insights or do a comparison.
Here is our pipeline:
![web_scraping_pipeline](https://github.com/Shabbir012/Project-3B23/assets/152379444/a38fa7d3-f560-4a83-a4fe-968d0d2779c4)

The libraries used for the web-scraping process includes BeautifulSoup and Selenium. Selenium was also used because BeautifulSoup only works for static webpages.

Apart from scraping websites, we also scraped pdfs using a library called "pymupdf". 

This is the folder structure of the files containing the code files for the pdf and web scraping process;

├── Web_pdf_scraping           # This is the folder containing the code files for pdf/web scraping

│   ├── pdf       # This is pdf scraping word file

│   ├── websites       # This is the code file for speech to text

└── ...
This is the folder structure containing all the data extracted/scraped from both pdfs and websites;
├── Data              # This is the folder containing the pdf files, data gotten from various websites/pdfs after scraping. 

│   ├── PDFS        # This is the folder containing the pdf files
|   ├── Other files
│    ├── website_dataset.zip       # A zip file containing all the scraped data

|    ├── NegativeDataset.zip       # A zip file containing all the scraped data

│    └── cleaned_dataset.zip        # A zip file containing the cleaned speech to text dataset and webscraping dataset

└── ...

All code files are in .ipynb format and could be uploaded to a jupyter notebook. However, other IDE's like Pycharm, Visual Studio Code or Python shell could also be used provided that all libraries are installed in the respective IDE's.
This is a picture of implementing webscraping in Pycharm.
![Screenshot (469)](https://github.com/Shabbir012/Project-3B23/assets/152379444/86ec357f-193c-46f7-be83-27937d1cb4d8)

![Screenshot (470)](https://github.com/Shabbir012/Project-3B23/assets/152379444/31ddebc0-4532-4e3a-aa1a-2313b79d63b8)


# Speech-To-Text
This involves converting any kind of audio files to text format. In this project, podcasts were mainly used and they were gotten from Apple. The library used for this is "Deepgram".  **Before, this code can be run, you need to create an account with Deepgram and get an API which must not be forgotten.** **The codes cannot be run in Jupyter notebooks.**
Here is our pipeline: 

![image](https://github.com/Shabbir012/Project-3B23/assets/152379444/5f9ebfe7-db4b-4cc1-bb54-fde5924972f3)

This is the folder structure:

├── ...

├── Speech_to_text           # This is the folder containing the code files for pspeech to text

│   ├── 

│   ├── 

└── ...

# Data Pre-processing and Machine learning models

![ML_pipeline](https://github.com/Shabbir012/Project-3B23/assets/152379444/74de9ae3-54c8-4d5d-b07f-0f99c3341626)

For data pre-processing, 
**Data Cleaning**
The dataset was thoroughly cleaned to remove punctuations, stop words (this was also extended to remove stop words related to metaverse), numbers and also change all text to lowercase.

**Data Labelling**
After cleaning the data, it was then labelled using a pre trained sentiment analyzer called "VADER sentiment analyzer". Three different sentiments were considered including positive (1), negative (-1) and neutral (0)

**Exploratory Data Analysis**
In order to understand the data better, we had to explore it by getting the shape of the dataset, checking if there were any duplicates (we had to remove some rows which were duplicates), using wordcloud to get the most common positive and negative sentiment, getting the top 10 positive and negative words. 
here are the most common positive words: 
![image](https://github.com/Shabbir012/Project-3B23/assets/152379444/f092a7b8-dd20-4031-8f72-c951741fdf5d)


![image](https://github.com/Shabbir012/Project-3B23/assets/152379444/9b9694ca-61cb-4339-adb1-74172e12ae5a)

We already have a zipped file containing the cleaned dataset (from both webscraping and speech to text):

├── Data              # This is the folder containing the pdf files, data gotten from various websites/pdfs after scraping. 

│   ├── PDFS        # This is the folder containing the pdf files
|   ├── Other files
│    ├── website_dataset.zip       # A zip file containing all the scraped data

|    ├── NegativeDataset.zip       # A zip file containing all the scraped data

│    └── **cleaned_dataset.zip**     # A zip file containing the cleaned speech to text dataset and webscraping dataset

└── ...

**Machine Learning**
This involves training models on data where patterns are observed and used to predict outcomes of new dataset. For this project, we used supervised machine learning comparing the accuracy four different algorithms across various training to test ratio. For feature extraction, we compared Bag of Words (BOW) against TF-IDF. 

Using BOW:
![image](https://github.com/Shabbir012/Project-3B23/assets/152379444/5f2d11b6-f734-409e-918a-7e35f7f368e0)

Using TF-IDF:
![image](https://github.com/Shabbir012/Project-3B23/assets/152379444/07a24f65-e6d3-4093-8aba-d1870aa27ba0)

The best model for this dataset was Random Forest Classifier with an accuracy of 0.81.
Here is the folder structure to find the machine learning file;
├── ...

|   ├── Models              # This is the folder containing the pdf machine learning model

|   ├── machine_learning        # This is the machine learning code file
 
└── ...

Here are all the files that were used for project management and to monitor the progress of the project.

├── ...

├── PRM             # This is the folder containing all files/tables/diagrams used for project management

│   ├── Agile Test Plan      # Test plan

│   ├── CRISP_DM.png       # crisp-dm diagram

|   ├── Individual Contributions      # table of individual contributions

│   ├── ML_pipeline.png       # Machine learning pipeline

|   ├── Project 3 Sprint Plan      # sprint plan

│   ├── Project3.pptx       # presentation file

|   ├── Project3B23.mpp    # project plan

│   ├── Quality Plan     # table of quality plan

|   ├── Risk Assessment      # risk assessment table

│   └── webscraping_pipeline.png        # web scraping pipeline

└── ...

**Project Outcome**
As a team, we were able to develop a machine learning model that could perform sentiment analysis. We also got data insights for Tango Eye which they could implement as a growth strategy. Due to the fact that we got a high number of positive sentiments, we have advised Tango Eye to delve into the world of metaverse as it holds various prospects for them.

![image](https://github.com/Shabbir012/Project-3B23/assets/152379444/69857aee-daf0-4ee4-9b41-017b924548a8)






**What could be improved upon?**
- Using a different method for feature extraction like Word2Vec
- Training a deep learning model for sentiment analysis instead of pretrained models
- Increasing the dataset.




