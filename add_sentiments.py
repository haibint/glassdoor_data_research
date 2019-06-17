import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# loading dataframe
df = pd.read_csv('./data/final_upd.csv', sep="\t")
sid = SentimentIntensityAnalyzer()

summary_sentiments = []
pros_sentiments = []
cons_sentiments = []
net_sentiments = []

def head():
    print(df.head())

def analyze_sentiment_socre(tokens):
    sentiment_score = 0
    for word in tokens:
        sentiment_score += sid.polarity_scores(word)['compound']
    return sentiment_score

def analyse_sentiment():
    print("starting to analyse sentiment")
    for index, row in df.iterrows():
        try:
            summary_text_tokenized = nltk.word_tokenize(row["summary"])
            pros_text_tokenized = nltk.word_tokenize(row["pros"])
            cons_text_tokenized = nltk.word_tokenize(row["cons"])
            # calculating scores
            summary_score = analyze_sentiment_socre(summary_text_tokenized) 
            pros_score = analyze_sentiment_socre(pros_text_tokenized)
            cons_score = analyze_sentiment_socre(cons_text_tokenized)
            net_total_score = summary_score+pros_score+cons_score
            # appending records to tsv.
            summary_sentiments.append(summary_score)
            pros_sentiments.append(pros_score)
            cons_sentiments.append(cons_score)
            net_sentiments.append(net_total_score)
            # progress reporting
            if index% 10000 < 1:
                print(str(index) + " rows has been added to memory")
        except TypeError as e:
            summary_sentiments.append("Type error happen")
            pros_sentiments.append("Type error happen")
            cons_sentiments.append("Type error happen")
            net_sentiments.append("Type error happen")
    df["summary_sentiments"]=summary_sentiments
    df["pros_sentiments"]=pros_sentiments
    df["cons_sentiments"]=cons_sentiments
    df["net_sentiments"]=net_sentiments
    df.to_csv('tem_out.tsv', sep='\t', index=False)

def create_csv_output(name):
    df["summary_sentiments"]=summary_sentiments
    df["pros_sentiments"]=pros_sentiments
    df["cons_sentiments"]=cons_sentiments
    df["net_sentiments"]=net_sentiments
    df.to_csv('tem_out'+name+'.tsv', sep='\t', index=False)

def command_loop(user_command):
    if user_command == "head":
        head()
        ask_command()
    elif user_command == "analyse_sentiment":
        analyse_sentiment()
        ask_command()

def ask_command():
    user_command = input("please type a command to excute.")
    print(user_command)
    command_loop(user_command)


## initial fuction to be excuted should be ask_command() if you intend to stay in the program.
analyse_sentiment()