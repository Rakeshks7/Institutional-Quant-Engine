from transformers import pipeline

try:
    classifier = pipeline('sentiment-analysis', model='yiyanghkust/finbert-tone')
    
    sentences = [
        "Revenue grew by 20%, but margins contracted due to supply chain issues.",
        "The company is facing a lawsuit, although analysts believe the impact is priced in.",
        "Operating cash flow turned positive for the first time in three years."
    ]

    print(f"--- FinBERT SOPHISTICATED ANALYSIS ---")
    for text in sentences:
        result = classifier(text)[0]
        label = result['label']
        score = result['score']
        
        print(f"📄 Text: {text[:50]}...")
        print(f"   🧠 AI Perception: {label} (Confidence: {score:.4f})\n")

except Exception as e:
    print("Transformer library not installed or model download failed.")
    print("To run this: pip install transformers torch")