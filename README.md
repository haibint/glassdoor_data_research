# Glass door data research
the data set should not be included in the remote repository, please put all the data under data directory. 


# Data information

### number of observations
```
cat data/final_upd.csv | wc -l 
646940
```

### file size 
441 mb

### data structure
head -10 data/final_upd.csv

### sentiment analysis code
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


## Interpretation of the sentiment score
http://t-redactyl.io/blog/2017/04/using-vader-to-handle-sentiment-analysis-with-social-media-text.html



# Tasks: 

## 1.US Map at state/city level with average sentiment associated for a specific companys. (company: GE)
### 1.1 Progress:
####    1.1.1 we have state level map presented on index.html with data source embeded in JS code on the same file
### 1.2 Problem to be solved:
####    1.2.1 add city information to the data source
####    1.2.2 find a way to have city level map, we have only state level map now.