# -*- coding: utf-8 -*-

class TreetaggerToWordnet():
    """
        Treetagger POS tags to wordnet morphological category mapper.
    """

    def __init__(self):
        self.fr_mapping = {
                            "ADJ" : "adv",
                            "ADV" : "adj",
                            "NAM" : "noun",
                            "NOM" : "noun",
                            "NUM" : "noun",
                            "VER:cond" : "verb",
                            "VER:futu" : "verb",
                            "VER:impe" : "verb",
                            "VER:impf" : "verb",
                            "VER:infi" : "verb",
                            "VER:pper" : "verb",
                            "VER:ppre" : "verb",
                            "VER:pres" : "verb",
                            "VER:simp" : "verb",
                            "VER:subi" : "verb",
                            "VER:subp" : "verb"
        }
        self.es_mapping = {"ADJ": "adj",
                           "ADV": "adv",
                           "NC": "noun",
                           "NMEA": "noun",
                           "NP": "noun",
                           "VCLIger": "verb",
                           "VCLIinf": "verb",
                           "VCLIfin": "verb",
                           "VEadj": "verb",
                           "VEfin": "verb",
                           "VEger": "verb",
                           "VEinf": "verb",
                           "VHadj": "verb",
                           "VHfin": "verb",
                           "VHger": "verb",
                           "VHinf": "verb",
                           "VLadj": "verb",
                           "VLfin": "verb",
                           "VLger": "verb",
                           "VLinf": "verb",
                           "VMadj": "verb",
                           "VMfin": "verb",
                           "VMger": "verb",
                           "VMinf": "verb",
                           "VSadj": "verb",
                           "VSfi": "verb",
                           "VSge": "verb",
                           "VSinf": "verb",
                           "VCLIinf": "verb"}
        self.en_mapping = {"ADJ": "adj",
                            "JJ": "adj",
                           "JJR": "adj",
                           "JJS": "adj",
                           "RB": "adv",
                           "RBR": "adv",
                           "RBS": "adv",
                           "NN": "noun",
                           "NC": "noun",
                           "NNS": "noun",
                           "NNP": "noun",
                           "NNPS": "noun",
                           "VB": "verb",
                           "VBD": "verb",
                           "VBG": "verb",
                           "VBN": "verb",
                           "VBP": "verb",
                           "VBZ": "verb",
                           "VLfin": "verb",
                           "VCLIinf": "verb"}
        self.pt_mapping = {"ADJ": "adj",
                           "ADV": "adv",
                           "N": "noun",
                           "V": "verb"}
        self.it_mapping = { "ADJ" : "adj",
                            "ADV" : "adv",
                            "NOM" :"noun",
                            "NPR" : "noun",
                            "NUM" : "noun",
                            "VER:cimp" : "verb",
                            "VER:cond" : "verb",
                            "VER:cpre" : "verb",
                            "VER:futu" : "verb",
                            "VER:geru" : "verb",
                            "VER:impe" : "verb",
                            "VER:impf" : "verb",
                            "VER:infi" : "verb",
                            "VER:pper" : "verb",
                            "VER:ppre" : "verb",
                            "VER:pres" :  "verb",
                            "VER:refl:infi" : "verb",
                            "VER:remo" : "verb"}
        self.ca_mapping = {}
        self.mapping = {
                            "sp": self.es_mapping,
                            "en": self.en_mapping,
                            "pt": self.pt_mapping,
                            "it": self.it_mapping,
                            "ca": self.ca_mapping,
                            "fr": self.fr_mapping
        }
        self.short_mapping={"adj": "a",
                            "adv": "r",
                            "noun": "n",
                            "verb": "v"}

    def wordnet_morph_category(self, lang, postag):
        """
            Returns the wordnet morphological category corresponding to the 
            POS tag of the given language.
        """

        pos = self.mapping[lang].get(postag, None)
        if pos is not None:
            return self.short_mapping[pos]
        else:
            return None


