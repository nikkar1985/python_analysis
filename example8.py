import json 

bbc_items = [
    "Homan said Operation Metro Surge raise profit...",
    "The teenage suspect success profit fail...",
    "But the International Olympic Committee raise...",
    "China has been attempting profit death...",
    "I'm floating on a jet stream success loss...",
    "loss death fail"
]


number_of_articles=len(bbc_items)


positive_words = ["raise", "success", "profit"]
negative_words = ["loss", "death", "fail"]


scored_news = []
total_sentiment = 0

for headline in bbc_items:
    score = 0
    lower_headline = headline.lower()
    
    for word in positive_words:
        if word in lower_headline: score += 1
    for word in negative_words:
        if word in lower_headline: score -=1
        
    total_sentiment += score
    scored_news.append({"title": headline, "score":score})
    
    
report = {
    "overall_market_mood": "Bullish" if total_sentiment > 0 else  "Bearish",
    "sentiment_score": total_sentiment,
    "detailed_analysis": scored_news
    
}


json_data=json.dumps(report, indent=4)

print(f"Mood αγοράς: {report['overall_market_mood']}")
print(f"Συνολικό σκορ : {total_sentiment}")


print(json_data)
