from autoComplete.autoCompleteData import AutoCompleteData


def score_suggestion(text, correction, correction_offset):
    corrections_fees = {'rep':[-5,-4,-3,-2,-1], 'del':[-10,-8,-6,-4,-2], 'add':[-10,-8,-6,-4,-2]}
    score = 0
    correction_fees = corrections_fees[correction]
    if correction_offset < len(correction_fees):
        score = len(text) * 2 + correction_fees[correction_offset]
    else:
        score = len(text) * 2 + correction_fees[-1]
    return score

def get_min(top_5, min_score):
    min_scor_p = 0
    for i in range(1,5):
        if top_5[i].get_score() <= min_score:
            min_score = top_5[i].get_score()
            min_scor_p = i
    return (min_score, min_scor_p)

def search_all_options(trie, text):
    suggestions = []
    simple_search = trie.search(text)
    for simple in simple_search:
        suggestions.append(AutoCompleteData(simple, text, "2", 2*len(text)))
    if len(suggestions) >= 5:
        return suggestions 
    for i in range(len(text)):     
        for char in range(26):
            text_l = list(text)
            if text_l[i] != chr(char + 97):
                text_l[i] = chr(char + 97)
            else: 
                continue
            simple_search = trie.search("".join(text_l))
            for simple in simple_search:
                score = score_suggestion(text, "rep", i + 1)
                suggestions.append(AutoCompleteData(simple, text, "2", score))            
    for i in range(len(text)):            
        text_l = list(text)
        text_l[i] = ""
        simple_search = trie.search("".join(text_l))
        for simple in simple_search:
            score = score_suggestion(text, "del", i + 1)
            suggestions.append(AutoCompleteData(simple, text, "2", score))
    return suggestions                   





