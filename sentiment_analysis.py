from pyld import jsonld
import json
import logging
from api_resources import Resources

context = {
    "@base": "http://paradigma.com/example-sentiments",
    "marl": "http://gsi.dit.upm.es/ontologies/marl/ns#",
    "onyx": "http://gsi.dit.upm.es/ontologies/onyx/ns#"}

class SentimentAnalysis:

    def __init__(self, text, language, sentiwordnet):
        self.sentiwordnet = sentiwordnet
        self.text = text
        self.language = language
        self.document = {"@id": "sentiment-pt", "@type": ["marl:Opinion", "onyx:EmotionExpression"]}
        self.analyzed = False


    def analyze(self):
        try:
            self.document["marl:algorithmConfidence"] =0.8
            sentiment = self.sentiwordnet.get_sentiment(self.text, self.language)
            sentiment_value = sentiment['positive']-sentiment['negative']
            self.document["marl:hasPolarity"] = self.marl_polarity(sentiment)
            self.document["marl:polarityValue"] = sentiment_value
            emotions = self.sentiwordnet.get_affects(self.text, self.language).get('affects', [])
            if emotions:
                self.document["onyx:hasEmotion"] = []
                for emotion, intensity in emotions.items():
                    self.document["onyx:hasEmotion"].append({
                        "@type": "onyx:Emotion",
                        "onyx:hasEmotionIntensity":intensity,
                        "onyx:hasEmotionCategory":emotion
                    })
            self.analyzed = True
        except Exception, e:
            logging.error(e, exc_info=True)

    def marl_polarity(self, sentiment):
        if sentiment > 0.0:
            return "marl:Positive"
        elif sentiment < 0.0:
            return "marl:Negative"
        else:
            return "marl:Neutral"

    def tostring(self):
        if not self.analyzed:
            raise Exception('Cannot get ONYX representation, run analyze first')
        else:
            compacted = jsonld.compact(self.document, context)
            return json.dumps(compacted, indent=2)

if __name__ == '__main__':
    sentiwordnet = Resources()
    sentiment = SentimentAnalysis("I feel encouragement, I have bought a good Movistar smartphone on Monday, it is amazing", "english", sentiwordnet)
    sentiment.analyze()
    print sentiment.tostring()