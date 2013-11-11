# -*- coding: utf-8 -*-
import requests
import json
import logging
from collections import defaultdict

class SolrService:

    def __init__(self):
        self.solr_url = "http://54.200.220.111:8983/solr/core0/search"
        

    def get_sentiment_emotions(self, term, domain):
        term = ' AND '.join(["title:%s" % term for term in term.split()])
        result = {"positive":0.0, "negative":0.0, "emotions":defaultdict(int)}
        num_docs_response = requests.get(self.solr_url, params={'q': '*:*', 'rows':0, 'fq':['+(domain:%s)' % (domain), '+(%s)' % term]})
        response = json.loads(num_docs_response.text)
        num_docs = response.get('response', {}).get('numFound', 0)
        print num_docs
        current_doc = 0
        while current_doc < num_docs:
            logging.warn("Querying 100 documents, starting on %s/%s" % (current_doc, num_docs))
            params = {'q': '*:*', 'fq':['+(domain:%s)' % (domain), '+(%s)' % term], 'start':current_doc, 'rows':100, 'fl':'positive,negative,*_emo'}
            docs_response = requests.get(self.solr_url, params=params).text
            for document in json.loads(docs_response).get('response', {}).get('docs', []):
                result['positive'] += document['positive']
                result['negative'] += document['negative']
                for key in document.keys():
                    if key.endswith('_emo'):
                        emotion = key.replace('_emo', '')
                        result['emotions'][emotion] += document[key]
            current_doc += 100
        print result
        return result

    def get_normalized_sentiment_emotion(self, term, domain):
        results = self.get_sentiment_emotions(term, domain)
        try:
            normalized_sentiment = 5.0 + (results['positive'] - results['negative']) / (results['positive'] + results['negative'])/2
        except ZeroDivisionError, e:
            normalized_sentiment = 0.0
        print normalized_sentiment
        emotions = results['emotions']
        if emotions:
            max_emotion = max(emotions, key=emotions.get)
        else:
            max_emotion = None
        return {"sentiment":normalized_sentiment, "emotion":max_emotion}


if __name__ == '__main__':
    service = SolrService()
    print service.get_normalized_sentiment_emotion('hesperia nh', 'booking.com')

