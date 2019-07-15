import pandas as pd
import nltk
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer

df = pd.read_csv('complaint_narrative_drop.csv')
df2 = df.set_index("Complaint.ID", drop = False)

# example_complaint = 'I am beyond exhausted with all my efforts to resolve this matter with ability recovery for a # of months Ive been back and forth trying to find a solution to have this account remove off my consumer report. I have no response back from any of my corresponders within all departments. Ive been advisedby my attorney to file a suit and sue for for damages that Im entitled to under the FCRA. I prefer to work directly with this company in resolving this issue that will result in removal of this account off my consumer report. I have no choice but to sue should I find no response once more after this complaint, this is my final attempt. I will therefore move forward with my supporting document. Ability recovery has this account # on this report thatI have absolutely no knowledge of. This has been a complete devastation to my entire family and myself due to fact this has held up an entire mortgageprocess having us nearly homeless. Please assist me in the aggressive removing of this account.'
# example_tokens = nltk.word_tokenize(example_complaint)
# print(example_tokens)

sid = SentimentIntensityAnalyzer()

def analyze_socre(tokens):
    sentiment_obj = {"score":0, "negative_words":""}
    for word in tokens:
        if sid.polarity_scores(word)['compound'] <= -0.3:
            sentiment_obj["score"] += sid.polarity_scores(word)['compound']
            sentiment_obj["negative_words"] = sentiment_obj["negative_words"] + word +", "
    return sentiment_obj

sentiment_score_list = []
global_negative_words = []

print("Data Frame is loaded")
row_count = 0

for index, row in df2.iterrows():
    tokens = nltk.word_tokenize(row["Consumer.complaint.narrative"])
    # print(analyze_socre(tokens))
    if analyze_socre(tokens) is not None:
        sentiment_score_list.append(analyze_socre(tokens)["score"])
        global_negative_words.append(analyze_socre(tokens)["negative_words"])
    else:
        sentiment_score_list.append(0)
        global_negative_words.append("no negative word found")
    if row_count%1000<1:
        print(row_count)
    row_count += 1



# create a new column to an existing dataframe
df2 = df2.assign(sentiment_score=pd.Series(sentiment_score_list).values)
df2 = df2.assign(negative_words=pd.Series(global_negative_words).values)
print(df2.head(10))

# export the dataframe as csv file
df2.to_csv('out.csv', sep='\t', index=False)
