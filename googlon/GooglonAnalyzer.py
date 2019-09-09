class GooglonAnalyzer:

    ALPHABET = 'sxocqnmwpfyheljrdgui'

    @staticmethod
    def is_foo_letter(letter):
        return letter in ['u', 'd', 'x', 's', 'm', 'p', 'f']

    @staticmethod
    def is_bar_letter(letter):
        return not GooglonAnalyzer.is_foo_letter(letter)

    @staticmethod
    def get_words(text):
        return text.split()

    @staticmethod
    def is_preposition(word):
        return len(word) == 6 and GooglonAnalyzer.is_foo_letter(word[len(word)-1]) and 'u' not in word
    
    @staticmethod
    def is_verb(word):
        return len(word) >= 6 and GooglonAnalyzer.is_bar_letter(word[len(word)-1])
    
    @staticmethod
    def is_subjunctive(verb):
        return GooglonAnalyzer.is_bar_letter(verb[0])
    
    @staticmethod
    def get_prepositions(text):
        prepositions = []
        words = GooglonAnalyzer.get_words(text)
        for word in words:
            if(GooglonAnalyzer.is_preposition(word)):
                prepositions.append(word)
        
        return prepositions
    
    @staticmethod
    def get_verbs(text):
        verbs = []
        words = GooglonAnalyzer.get_words(text)
        for word in words:
            if(GooglonAnalyzer.is_verb(word)):
                verbs.append(word)
        
        return verbs

    @staticmethod
    def get_subjunctive_verbs(text):
        subjunctive_verbs = []
        verbs = GooglonAnalyzer.get_verbs(text)
        for verb in verbs:
            if(GooglonAnalyzer.is_subjunctive(verb)):
                subjunctive_verbs.append(verb)
        
        return subjunctive_verbs
    
    @staticmethod
    def sorter(words):
        return [GooglonAnalyzer.ALPHABET.index(c) for c in words]

    @staticmethod
    def get_vocabulary(text):
        words = set(GooglonAnalyzer.get_words(text))
        return list(sorted(words, key = GooglonAnalyzer.sorter))

    @staticmethod
    def get_googlon_value(word):
        value = 0
        power = 0
        for letter in word:
            position = GooglonAnalyzer.ALPHABET.index(letter)
            value += pow(20, power) * position
            power += 1

        return value
    
    @staticmethod
    def is_googlon_number(word):
        word_value = GooglonAnalyzer.get_googlon_value(word)
        
        return word_value > 81827 and word_value % 3 == 0
    
    @staticmethod
    def get_pretty_numbers(text):
        pretty_numbers = []
        words = GooglonAnalyzer.get_words(text)
        for word in words:
            if(GooglonAnalyzer.is_googlon_number(word)):
                pretty_numbers.append(GooglonAnalyzer.get_googlon_value(word))
        
        return pretty_numbers
