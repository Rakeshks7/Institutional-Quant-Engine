from textblob import TextBlob

headlines = [
    "HDFC Bank reports record breaking profits for Q3",
    "Global recession fears rise as inflation hits new peak",
    "TCS wins massive deal in UK, stock likely to surge",
    "Regulatory ban hits Adani ports, shares tumble",
    "Market remains flat ahead of budget announcement"
]

print(f"--- NEWS SENTIMENT ANALYZER ---")
print(f"{'SENTIMENT':<10} | {'SCORE':<6} | HEADLINE")
print("-" * 60)

for news in headlines:
    analysis = TextBlob(news)
    score = analysis.sentiment.polarity 
    
    if score > 0.1: sentiment = "🟢 BULLISH"
    elif score < -0.1: sentiment = "🔴 BEARISH"
    else: sentiment = "⚪ NEUTRAL"
    
    print(f"{sentiment:<10} | {score:>5.2f}  | {news}")