import getopt
import tornado.ioloop
import tornado.web
import sys
from api_resources import Resources
from sentiment_analysis import SentimentAnalysis

import time

class GetWordInformation(tornado.web.RequestHandler):

    def initialize(self, sentiwordnet):
        self.sentiwordnet = sentiwordnet

    def get(self):
        start = time.time()
        # Check input text
        word = self.get_argument("word")
        pos = self.get_argument("pos", ['v', 'n', 'a', 'r'])
        language = self.get_argument("language")

        if self.get_argument("format", None) == "onyx":
            self.clear()
            self.set_status(400)
            self.finish("<html><body>ONYX response not implemented</body></html>")
        else:
            # Create DS to save result
            response = {}
            if isinstance(pos, list):
                response['synsets'] = {}
                for postagging in pos:
                    pos_result = sentiwordnet.get_info_word(word, postagging, language)
                    if pos_result:
                        response['synsets'].update(pos_result)
                response["elapsed_time"] = time.time() - start
            else:
                response["synsets"] = sentiwordnet.get_info_word(word, pos, language)
                response["elapsed_time"] = time.time() - start
            # Return result
            self.write(response)

class Synonym(tornado.web.RequestHandler):

    def initialize(self, sentiwordnet):
        self.sentiwordnet = sentiwordnet

    def get(self):
        start = time.time()
        # Check input text
        word = self.get_argument("word")
        pos = self.get_argument("pos")
        language = self.get_argument("language")

        if self.get_argument("format", None) == "onyx":
            self.clear()
            self.set_status(400)
            self.finish("<html><body>ONYX response not implemented</body></html>")
        else:
            # Create DS to save result
            response = {}

            response["sentiment"] = sentiwordnet.get_synonym(word, pos, language)
            response["elapsed_time"] = time.time() - start
            # Return result
            self.write(response)

class GetAffect(tornado.web.RequestHandler):

    def initialize(self, sentiwordnet):
        self.sentiwordnet = sentiwordnet

    def get(self):
        start = time.time()
        # Check input text
        text = self.get_argument("text").encode('ascii', errors='ignore')
        language = self.get_argument("language")

        if self.get_argument("format", None) == "onyx":
            self.clear()
            self.set_status(400)
            self.finish("<html><body>ONYX response not implemented</body></html>")
        else:
            # Create DS to save result
            response = {}

            response["affects"] = sentiwordnet.get_affects(text, language)
            response["elapsed_time"] = time.time() - start
            # Return result
            self.write(response)

class GetDommain(tornado.web.RequestHandler):

    def initialize(self, sentiwordnet):
        self.sentiwordnet = sentiwordnet

    def get(self):
        start = time.time()
        # Check input text
        text = self.get_argument("text")
        language = self.get_argument("language")

        if self.get_argument("format", None) == "onyx":
            self.clear()
            self.set_status(400)
            self.finish("<html><body>ONYX response not implemented</body></html>")
        else:
            # Create DS to save result
            response = {}

            response["dommains"] = sentiwordnet.get_domains(text, language)
            response["elapsed_time"] = time.time() - start
            # Return result
            self.write(response)

class GetSentiment(tornado.web.RequestHandler):

    def initialize(self, sentiwordnet):
        self.sentiwordnet = sentiwordnet

    def get(self):
        start = time.time()
        # Check input text
        text = self.get_argument("text").encode('ascii', errors='ignore')
        language = self.get_argument("language")

        if self.get_argument("format", None) == "onyx":
            self.clear()
            self.set_status(400)
            self.finish("<html><body>ONYX response not implemented</body></html>")
        else:
            # Create DS to save result
            response = {}

            response["sentiment"] = sentiwordnet.get_sentiment(text, language)
            response["elapsed_time"] = time.time() - start
            # Return result
            self.write(response)

class GetSentimentEmotion(tornado.web.RequestHandler):

    def initialize(self, sentiwordnet):
        self.sentiwordnet = sentiwordnet

    def get(self):
        start = time.time()
        # Check input text
        text = self.get_argument("text")
        language = self.get_argument("language")

        if self.get_argument("format", None) == "onyx":
            sentiment = SentimentAnalysis(text, language, self.sentiwordnet)
            sentiment.analyze()
            response = sentiment.tostring()
            self.write(response)
        else:
            # Create DS to save result
            response = {}

            response.update(sentiwordnet.get_sentiment_and_emotion(text, language))
            response["elapsed_time"] = time.time() - start
            # Return result
            self.write(response)

class PosTagging(tornado.web.RequestHandler):

    def initialize(self, sentiwordnet):
        self.sentiwordnet = sentiwordnet


    def get(self):
        start = time.time()
        # Check input text
        text = self.get_argument("text")
        language = self.get_argument("language")

        if self.get_argument("format", None) == "onyx":
            self.clear()
            self.set_status(400)
            self.finish("<html><body>ONYX response not implemented</body></html>")
        else:
            # Create DS to save result
            response = {}

            response["postagging"] = sentiwordnet.get_postagging(text, language)
            response["elapsed_time"] = time.time() - start
            # Return result
            self.write(response)

class GetInformation(tornado.web.RequestHandler):
    def initialize(self, sentiwordnet):
        self.sentiwordnet = sentiwordnet

    def get(self):
        start = time.time()
        # Check input text
        word = self.get_argument("word")
        pos = self.get_argument("pos")
        language = self.get_argument("language")

        score = sentiwordnet.get_info_first_word(word, pos, language)

        if self.get_argument("format", None) == "onyx":
            self.clear()
            self.set_status(400)
            self.finish("<html><body>ONYX response not implemented</body></html>")
        else:
            # Create DS to save result
            response = {}
            response["score"] = score

            response["elapsed_time"] = time.time() - start
            # Return result
            self.write(response)


class Translator(tornado.web.RequestHandler):
    def initialize(self, sentiwordnet):
        self.sentiwordnet = sentiwordnet

    def get(self):
        start = time.time()
        # Check input text
        word = self.get_argument("word")
        pos = self.get_argument("pos")
        from_language = self.get_argument("from_language")
        to_language = self.get_argument("to_language")

        translation = sentiwordnet.get_translation(word, pos, from_language, to_language)

        if self.get_argument("format", None) == "onyx":
            self.clear()
            self.set_status(400)
            self.finish("<html><body>ONYX response not implemented</body></html>")
        else:
            # Create DS to save result
            response = {}
            response["translation"] = translation

            response["elapsed_time"] = time.time() - start
            # Return result
            self.write(response)

# Check if server por is valid
try:
    opts, args = getopt.getopt(sys.argv[1:], "p:", ["port="])
    assert (len(opts) == 1)
except:
    print 'api_resources_service.py -p <port>'
    sys.exit()

for o, a in opts:
    if o == "-p":
        port = a
    else:
        pass

if __name__ == "__main__":
    # Init treetagger with a specific language
    sentiwordnet = Resources()

    # Init Tornado web server
    application = tornado.web.Application([
        (r"/get_information", GetInformation, dict(sentiwordnet=sentiwordnet)),
        (r"/translate", Translator, dict(sentiwordnet=sentiwordnet)),
        (r"/get_synonym", Synonym, dict(sentiwordnet=sentiwordnet)),
        (r"/get_postagging", PosTagging, dict(sentiwordnet=sentiwordnet)),
        (r"/get_sentiment", GetSentiment, dict(sentiwordnet=sentiwordnet)),
        (r"/get_affect", GetAffect, dict(sentiwordnet=sentiwordnet)),
        (r"/get_dommain", GetDommain, dict(sentiwordnet=sentiwordnet)),
        (r"/get_word_information", GetWordInformation, dict(sentiwordnet=sentiwordnet)),
        (r"/get_sentiment_emotion", GetSentimentEmotion, dict(sentiwordnet=sentiwordnet)),
    ])

    # Listen on specific port and start server
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
