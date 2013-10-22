from lxml import etree
import logging

MARL_NS = 'http://purl.org/marl/ns#'
RDF_NS = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
NSMAP = {"marl" : MARL_NS,
         "rdf" : RDF_NS}

class SentimentAnalysis:

    def __init__(self, text, language, sentiwordnet):
        self.sentiwordnet = sentiwordnet
        self.text = text
        self.language = language
        self.result = etree.Element("{%s}opinion" % MARL_NS, nsmap = NSMAP)
        self.analyzed = False


    def analyze(self):
        try:
            sentiment = self.sentiwordnet.get_sentiment(self.text, self.language)
            sentiment_value = sentiment['positive']-sentiment['negative']
            extracted_from = etree.Element('{%s}extractedFrom' % MARL_NS, nsmap = NSMAP)
            extracted_from.text = self.text
            self.result.append(extracted_from)
            # describes_object = etree.Element('{%s}describesObject' % MARL_NS, nsmap = NSMAP)
            # has_polarity.attrib['{%s}resource' % RDF_NS] = rafa_dbpedia
            # self.result.append(describes_object)
            # describes_object_feature = etree.Element('{%s}describesObjectFeature' % MARL_NS, nsmap = NSMAP)
            # describes_object.attrib['{%s}resource' % RDF_NS] = rafa_dbpedia
            # self.result.append(describes_object_feature)
            # for_domain = etree.Element('{%s}forDomain' % MARL_NS, nsmap = NSMAP, rdfResource=rafa_dbpedia)
            # for_domain.attrib['{%s}resource' % RDF_NS] = rafa_dbpedia
            # self.result.append(for_domain)
            has_polarity = etree.Element('{%s}hasPolarity' % MARL_NS, nsmap = NSMAP)
            has_polarity.attrib['{%s}resource' % RDF_NS] = self.marl_polarity(sentiment)
            self.result.append(has_polarity)
            polarity_value = etree.Element('{%s}polarityValue' % MARL_NS, nsmap = NSMAP)
            polarity_value.text = str(sentiment_value)
            self.result.append(polarity_value)
            algorithm_confidence = etree.Element('{%s}algorithmConfidence' % MARL_NS, nsmap = NSMAP)
            algorithm_confidence.text = '0.8'
            self.result.append(algorithm_confidence)
            # self.opinion_text = etree.Element('{%s}opinionText' % MARL_NS, nsmap = NSMAP)
            # self.opinion_text = sentiment_opinion_text
            # self.result.append(opinion_text)
            self.analyzed = True
        except Exception, e:
            logging.error(e, exc_info=True)

    def marl_polarity(self, sentiment):
        if sentiment > 0.0:
            return "http://purl.org/marl/ns#Positive"
        elif sentiment < 0.0:
            return "http://purl.org/marl/ns#Negative"
        else:
            return "http://purl.org/marl/ns#Neutral"

    def tostring(self):
        if not self.analyzed:
            raise Exception('Cannot get MARL representation, run analyze first')
        else:
            return etree.tostring(self.result, pretty_print=True)

if __name__ == '__main__':
    sentiment = SentimentAnalysis("Movistar me gusta mucho", "es")
    sentiment.analyze()
    print sentiment.tostring()