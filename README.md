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
## 2. US county level map for net sentiment for all company aggregated
### 2.1 Progerss:
####    2.1.1 we alread have the county level map, the geojson has 3219 rows(counties) and 3 columns (code, name value)
####            code                name  value
####    0  us-al-001  Autauga County, AL    3.9
####    1  us-al-003  Baldwin County, AL    4.3
####    2  us-al-005  Barbour County, AL    5.6

####    2.1.2 we now need to map sum_city_year.dta into a json file so we then can render the county level map with highcharts(see index2.html)
####    - sum_city_year.dta has 38977 rows of data and show none standardized county name.
####    - now loaded two set of data into one python session with pd dataframe.
####    - investigae how many unique counties were in the sum_city_year.dta 
            >>> print(len(unique_counties_from_dta))
            9540    s

            the matched counties is documented in matched_counties_with_code.tsv
### 2.2 Problem, the counties that can actually be mapped to county codes we have now are only 624.