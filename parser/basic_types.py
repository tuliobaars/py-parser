class Match:
    
    def __init__(self, name, label_regex, value_regex, breaker_regex):
        """Base Match class.
        
        name : str
            the name for this match
        label_regex : regex str or list of regex strs
            the regex[es] to use for matching labels.
        values_regex : regex str or list of regex strs
            the regex[es] to use for matching values.
        breaker_regex: regex str or list of regex strs
            the regex[es] to use for matching breakers.
        """

        self.name = name
        
        # set args to be lists of strings
        if isinstance(label_regex, str):
            self.labels = [label_regex]
        else:
            self.labels = list(label_regex)

        if isinstance(value_regex, str):
            self.values = [value_regex]
        else:
            self.values = list(value_regex)

        if isinstance(breaker_regex, str):
            self.breakers = [breaker_regex]
        else:
            self.breakers = list(braker_regex)


    def __repr__(self):
        return 'Match({})'.format(self.name)
