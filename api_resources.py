# coding=utf-8
import csv
import json
import time
import treetagger
import treetagger_wordnet


class Resources:
    """Sentimentwordnet bindind class

    This class provides a binding to lookup sentiment meassure for
    English and Spanish words
    """


    def __init__(self):
        """
        Initialite datastructures
        """
        self.map_lenguage = {"english": "en",
                             "spanish": "sp",
                             "italian": "it",
                             "portuguese": "pt",
                             "french": "fr"}

        """
        Init TreeTagger
        """
        # Init treetagger with a specific language
        self.treetagger_english = treetagger.TreeTagger(encoding='latin-1', language="english")
        self.treetagger_spanish = treetagger.TreeTagger(encoding='utf8', language="spanish")
        self.treetagger_italian = treetagger.TreeTagger(encoding='utf8', language="italian")
        self.treetagger_portuguese = treetagger.TreeTagger(encoding='latin-1', language="portuguese")
        self.treetagger_french = treetagger.TreeTagger(encoding='utf8', language="french")
        # self.treetagger_portuguese = treetagger.TreeTagger(encoding='latin-1', language="galician")

        self.tt_to_wordnet = treetagger_wordnet.TreetaggerToWordnet()

        """
        Load domains
        """
        self.domains = {}
        f_in = file("data/domains/wordnet-domains30.txt", "r")
        for line in f_in:
            line = line.replace("\n", "")
            chunks = line.split("\t")
            self.domains[chunks[0]] = chunks[1].split(' ')
        f_in.close()

        """
        Load affects
        """
        self.affects = {}
        f_in = file("data/affects/wn-affect-1.1-30.txt", "r")
        for line in f_in:
            line = line.replace("\n", "")
            chunks = line.split("\t")
            self.affects[chunks[0]] = chunks[1].split(' ')
        f_in.close()

        """
        Load senti
        """
        self.senti = {}
        f_in = file("data/senti/senti.tsv", "r")
        for line in f_in:
            line = line.replace("\n", "")
            chunks = line.split("\t")
            self.senti[chunks[2] + '#' + chunks[0]] = {}
            self.senti[chunks[2] + '#' + chunks[0]]["positive"] = chunks[3]
            self.senti[chunks[2] + '#' + chunks[0]]["negative"] = chunks[1]
            self.senti[chunks[2] + '#' + chunks[0]]["objective"] = 1 - abs(float(chunks[3][1:]) + float(chunks[1][1:]))
        f_in.close()

        """
        Load words_en
        """
        self.words_en = {}
        f_in = file("data/words/en.tsv", "r")
        for line in f_in:
            line = line.replace("\n", "")
            line = line.replace("\r", "")
            chunks = line.split("\t")
            self.words_en[chunks[0]] = {}
            self.words_en[chunks[0]]["word"] = chunks[1]
            self.words_en[chunks[0]]["pos"] = chunks[2]
            self.words_en[chunks[0]]["synsets"] = chunks[3].split(' ')
        f_in.close()

        """
        Load words_sp
        """
        self.words_sp = {}
        f_in = file("data/words/sp.tsv", "r")
        for line in f_in:
            line = line.replace("\n", "")
            line = line.replace("\r", "")
            chunks = line.split("\t")
            self.words_sp[chunks[0]] = {}
            self.words_sp[chunks[0]]["word"] = chunks[1]
            self.words_sp[chunks[0]]["pos"] = chunks[2]
            self.words_sp[chunks[0]]["synsets"] = chunks[3].split(' ')
        f_in.close()

        """
        Load words_it
        """
        self.words_it = {}
        f_in = file("data/words/it.tsv", "r")
        for line in f_in:
            line = line.replace("\n", "")
            line = line.replace("\r", "")
            chunks = line.split("\t")
            self.words_it[chunks[0]] = {}
            self.words_it[chunks[0]]["word"] = chunks[1]
            self.words_it[chunks[0]]["pos"] = chunks[2]
            self.words_it[chunks[0]]["synsets"] = chunks[3].split(' ')
        f_in.close()

        """
        Load words_pt
        """
        self.words_pt = {}
        f_in = file("data/words/pt.tsv", "r")
        for line in f_in:
            line = line.replace("\n", "")
            line = line.replace("\r", "")
            chunks = line.split("\t")
            self.words_pt[chunks[0]] = {}
            self.words_pt[chunks[0]]["word"] = chunks[1]
            self.words_pt[chunks[0]]["pos"] = chunks[2]
            self.words_pt[chunks[0]]["synsets"] = chunks[3].split(' ')
        f_in.close()

        """
        Load words_fr
        """
        self.words_fr = {}
        f_in = file("data/words/pt.tsv", "r")
        for line in f_in:
            line = line.replace("\n", "")
            line = line.replace("\r", "")
            chunks = line.split("\t")
            self.words_fr[chunks[0]] = {}
            self.words_fr[chunks[0]]["word"] = chunks[1]
            self.words_fr[chunks[0]]["pos"] = chunks[2]
            self.words_fr[chunks[0]]["synsets"] = chunks[3].split(' ')
        f_in.close()

        """
        Load synsets_en
        """
        self.synsets_en = {}
        f_in = file("data/synsets/en.tsv", "r")
        for line in f_in:
            line = line.replace("\n", "")
            line = line.replace("\r", "")
            chunks = line.split("\t")
            self.synsets_en[chunks[0]] = {}
            self.synsets_en[chunks[0]]["synset"] = chunks[1]
            self.synsets_en[chunks[0]]["pos"] = chunks[2]
            self.synsets_en[chunks[0]]["meaning"] = chunks[3]
            self.synsets_en[chunks[0]]["words"] = chunks[4].split(' ')
        f_in.close()

        """
        Load synsets_sp
        """
        self.synsets_sp = {}
        f_in = file("data/synsets/sp.tsv", "r")
        for line in f_in:
            line = line.replace("\n", "")
            chunks = line.split("\t")
            self.synsets_sp[chunks[0]] = chunks[1].split(' ')
        f_in.close()

        """
        Load synsets_it
        """
        self.synsets_it = {}
        f_in = file("data/synsets/it.tsv", "r")
        for line in f_in:
            line = line.replace("\n", "")
            chunks = line.split("\t")
            self.synsets_it[chunks[0]] = chunks[1].split(' ')
        f_in.close()

        """
        Load synsets_pt
        """
        self.synsets_pt = {}
        f_in = file("data/synsets/pt.tsv", "r")
        for line in f_in:
            line = line.replace("\n", "")
            chunks = line.split("\t")
            self.synsets_pt[chunks[0]] = chunks[1].split(' ')
        f_in.close()

        """
        Load synsets_fr
        """
        self.synsets_fr = {}
        f_in = file("data/synsets/fr.tsv", "r")
        for line in f_in:
            line = line.replace("\n", "")
            chunks = line.split("\t")
            self.synsets_fr[chunks[0]] = chunks[1].split(' ')
        f_in.close()

    def get_senti(self, synset, pos):
        if pos + '#' + synset in self.senti:
            return self.senti[pos + '#' + synset]
        else:
            return None

    def get_domain(self, synset, pos):
        if pos + '#' + synset in self.domains:
            return self.domains[pos + '#' + synset]
        else:
            return None


    def get_affect(self, synset, pos):
        if pos + '#' + synset in self.affects:
            return self.affects[pos + '#' + synset]
        else:
            return None

    def has_senti(self, synset, pos):
        if pos + '#' + synset in self.senti:
            return True
        else:
            return False

    def has_domain(self, synset, pos):
        if pos + '#' + synset in self.domains:
            return True
        else:
            return False


    def has_affect(self, synset, pos):
        if pos + '#' + synset in self.affects:
            return True
        else:
            return False


    def has_word(self, word, pos, language):
        if pos + '#' + word in self.words_en:
            return True
        else:
            return False


    def get_first_synset(self, word, pos, language):
        if pos is None or word is None:
            return None
        lan = self.map_lenguage[language]
        if lan == "en":
            if pos + '#' + word in self.words_en:
                return self.words_en[pos + '#' + word]["synsets"][0]
            else:
                return None
        if lan == "sp":
            if pos + '#' + word in self.words_sp:
                return self.words_sp[pos + '#' + word]["synsets"][0]
            else:
                return None
        if lan == "it":
            if pos + '#' + word in self.words_it:
                return self.words_it[pos + '#' + word]["synsets"][0]
            else:
                return None
        if lan == "pt":
            if pos + '#' + word in self.words_pt:
                return self.words_pt[pos + '#' + word]["synsets"][0]
            else:
                return None
        if lan == "fr":
            if pos + '#' + word in self.words_fr:
                return self.words_fr[pos + '#' + word]["synsets"][0]
            else:
                return None
        else:
            return None

    def get_words(self, synset, pos, language):
        lan = self.map_lenguage[language]
        if lan == "en":
            if pos + '#' + synset in self.synsets_en:
                return self.synsets_en[pos + '#' + synset]["words"]
            else:
                return None
        if lan == "sp":
            if pos + '#' + synset in self.synsets_sp:
                return self.synsets_sp[pos + '#' + synset]
            else:
                return None
        if lan == "it":
            if pos + '#' + synset in self.synsets_it:
                return self.synsets_it[pos + '#' + synset]
            else:
                return None
        if lan == "pt":
            if pos + '#' + synset in self.synsets_pt:
                return self.synsets_pt[pos + '#' + synset]
            else:
                return None
        if lan == "fr":
            if pos + '#' + synset in self.synsets_fr:
                return self.synsets_fr[pos + '#' + synset]
            else:
                return None
        else:
            return None

    def get_info(self, synset, pos):
        result = {}
        result["synset"] = synset
        result["pos"] = pos
        result["domain"] = self.get_domain(synset, pos)
        result["affect"] = self.get_affect(synset, pos)
        result["sentiment"] = self.get_senti(synset, pos)
        result["english_words"] = self.get_words(synset, pos, "english")
        result["spanish_words"] = self.get_words(synset, pos, "spanish")
        result["italian_words"] = self.get_words(synset, pos, "italian")
        result["portuguese_words"] = self.get_words(synset, pos, "portuguese")
        result["french_words"] = self.get_words(synset, pos, "french")
        return result

    def get_postagging(self, text, language):
        # Perform PosTagging
        response = []
        if language == "english":
            for postag in self.treetagger_english.tag(text):
                element = {}
                # Word
                element["word"] = postag[0]
                # Postaging
                element["postagging"] = postag[1]
                # Wordnet postagging mapping
                element["pos"] = self.tt_to_wordnet.wordnet_morph_category(self.map_lenguage[language], postag[1])
                # Lemma
                element["lemma"] = postag[2]
                response.append(element)
        if language == "spanish":
            for postag in self.treetagger_spanish.tag(text):
                element = {}
                # Word
                element["word"] = postag[0]
                # Postaging
                element["postagging"] = postag[1]
                # Wordnet postagging mapping
                element["pos"] = self.tt_to_wordnet.wordnet_morph_category(self.map_lenguage[language], postag[1])
                # Lemma
                element["lemma"] = postag[2]
                response.append(element)
        if language == "italian":
            for postag in self.treetagger_italian.tag(text):
                element = {}
                # Word
                element["word"] = postag[0]
                # Postaging
                element["postagging"] = postag[1]
                # Wordnet postagging mapping
                element["pos"] = self.tt_to_wordnet.wordnet_morph_category(self.map_lenguage[language], postag[1])
                # Lemma
                element["lemma"] = postag[2]
                response.append(element)
        if language == "portuguese":
            for postag in self.treetagger_portuguese.tag(text):
                element = {}
                # Word
                element["word"] = postag[0]
                # Postaging
                element["postagging"] = postag[1]
                # Wordnet postagging mapping
                element["pos"] = self.tt_to_wordnet.wordnet_morph_category(self.map_lenguage[language], postag[1])
                # Lemma
                element["lemma"] = postag[2]
                response.append(element)
        if language == "french":
            for postag in self.treetagger_french.tag(text):
                element = {}
                # Word
                element["word"] = postag[0]
                # Postaging
                element["postagging"] = postag[1]
                # Wordnet postagging mapping
                element["pos"] = self.tt_to_wordnet.wordnet_morph_category(self.map_lenguage[language], postag[1])
                # Lemma
                element["lemma"] = postag[2]
                response.append(element)
        return response

    def get_translation(self, word, pos, from_language, to_language):
        lang_from = self.map_lenguage[from_language]
        lang_to = self.map_lenguage[to_language]
        # Assert input params
        assert (lang_from in ["sp", "en", "it", "pt", "fr"])
        assert (lang_to in ["sp", "en", "it", "pt", "fr"])
        synset = self.get_first_synset(word, pos, from_language)
        if synset is not None:
            return self.get_words(synset, pos, to_language)
        else:
            return None

    def get_synonym(self, word, pos, language):
        synset = self.get_first_synset(word, pos, language)
        if synset is not None:
            return self.get_words(synset, pos, language)
        else:
            return None

    def get_affect_text(self, text, language):
        affects = {}
        affects["affects"] = {}
        affects["words"] = {}
        for word in text:
            synset = self.get_first_synset(word["word"], word["pos"], language)
            if synset is not None:
                if self.has_affect(synset, word["pos"]):
                    affect = self.get_affect(synset, word["pos"])
                    element = {}
                    element["word"] = word["word"]
                    element["pos"] = word["pos"]
                    element["synset"] = synset
                    element["domains"] = affect
                    for af in affect:
                        if af not in affects["affects"].keys():
                            affects["affects"][af] = 1
                        else:
                            affects["affects"][af] += 1
                    affects["words"][word["word"]] = element
        return affects

    def get_affects(self, text, language):
        posttext = self.get_postagging(text, language)
        return self.get_affect_text(posttext, language)

    def get_domains_text(self, text, language):
        result = {}
        result["dommains"] = {}
        result["words"] = {}
        for word in text:
            synset = self.get_first_synset(word["word"], word["pos"], language)
            if synset is not None:
                if self.has_domain(synset, word["pos"]):
                    dommain = self.get_domain(synset, word["pos"])
                    element = {}
                    element["word"] = word["word"]
                    element["pos"] = word["pos"]
                    element["synset"] = synset
                    element["domains"] = dommain
                    for af in dommain:
                        if af not in result["dommains"].keys():
                            result["dommains"][af] = 1
                        else:
                            result["dommains"][af] += 1
                    result["words"][word["word"]] = element
        return result

    def get_domains(self, text, language):
        posttext = self.get_postagging(text, language)
        return self.get_domains_text(posttext, language)

    def get_sentiment_text(self, text, language):
        sentiment = {}
        sentiment["words"] = {}
        sentiment["positive"] = 0
        sentiment["negative"] = 0
        for word in text:
            synset = self.get_first_synset(word["lemma"], word["pos"], language)
            if synset is not None:
                if self.has_senti(synset, word["pos"]):
                    senti = self.get_senti(synset, word["pos"])
                    sentiment["positive"] = sentiment["positive"] + float(senti["positive"][1:])
                    sentiment["negative"] = sentiment["negative"] + float(senti["negative"][1:])
                    if senti["positive"] != "+0" or senti["negative"] != "-0":
                        senti["synset"] = synset
                        senti["pos"] = word["pos"]
                        sentiment["words"][word["lemma"]] = senti
        return sentiment

    def get_sentiment(self, text, language):
        posttext = self.get_postagging(text, language)
        return self.get_sentiment_text(posttext, language)


    def get_info_first_word(self, word, pos, language):
        synset = self.get_first_synset(word, pos, language)
        return self.get_info(synset, pos)

if __name__ == "__main__":
    # Init class
    time_start = time.time()
    sentiwordnet = Resources()
    print("Loaded time: %s\n" % (time.time() - time_start))

    # Some lookups
    # words = [("unfortunately", "r", "english"), ("desafortunadamente", "r", "spanish"),
    #          ("exuberant", "a", "english"), ("stressful", "a", "english"), ("comfortably", "r", "english"),
    #          ("violación", "n", "spanish")]
    #
    # for word, pos, language in words:
    #     time_start = time.time()
    #     a = sentiwordnet.get_info(word, pos)
    #     print("%s %s" % (word, a))
    #     print("Lookup time: %s \n" % (time.time() - time_start))


    #
    print("***INFO DE UN SYNSET***")
    print(sentiwordnet.get_info("00042769", "r"))
    # print("***TRADUCCION DE UNA PALABRA***")
    # print(sentiwordnet.get_translation("good", "n", "english", "spanish"))
    # print(sentiwordnet.get_translation("diorama", "n", "spanish", "english"))
    # print("***SINÓNIMOS DE UNA PALABRA***")
    # print(sentiwordnet.get_synonym("good", "n", "english"))
    # print(sentiwordnet.get_synonym("diorama", "n", "spanish"))

    # print(sentiwordnet.get_sentiment([{"word": "buy", "pos": "v"}, {"word": "new", "pos": "r"}], "english"))

    # print(sentiwordnet.get_postagging("I am a good boy", "english"))

    # print(sentiwordnet.get_affects("amado amado amado", "spanish"))

    # print(sentiwordnet.get_sentiment(
    #     "Cuando Gregorio Samsa se despertó una mañana después de un sueño intranquilo, se encontró sobre su cama convertido en un monstruoso insecto. Estaba tumbado sobre su espalda dura, y en forma de caparazón y, al levantar un poco la cabeza veía un vientre abombado, parduzco, dividido por partes duras en forma de arco, sobre cuya protuberancia apenas podía mantenerse el cobertor, a punto ya de resbalar al suelo. Sus muchas patas, ridículamente pequeñas en comparación con el resto de su tamaño, le vibraban desamparadas ante los ojos.",
    #     "spanish"))

    # print(sentiwordnet.get_sentiment("Ogni individuo ha diritto all'istruzione. L'istruzione deve essere gratuita almeno per quanto riguarda le classi elementari e fondamentali. L'istruzione elementare deve essere obbligatoria. L'istruzione tecnica e professionale deve essere messa alla portata di tutti e l'istruzione superiore deve essere egualmente accessibile a tutti sulla base del merito.", "italian"))