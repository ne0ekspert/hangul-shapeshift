import networkx as nx
from jamo import JAMO_LEADS_MODERN, JAMO_VOWELS_MODERN, JAMO_TAILS_MODERN, j2hcj

class ChoNetwork:
    def __init__(self):
        self.G = nx.Graph()

        self.G.add_edge("ㄱ", "ㄲ")
        self.G.add_edge("ㄱ", "ㄴ")
        self.G.add_edge("ㄱ", "ㅋ")
        self.G.add_edge("ㄱ", "ㅅ")
        self.G.add_edge("ㄴ", "ㄷ")
        self.G.add_edge("ㄷ", "ㄸ")
        self.G.add_edge("ㄷ", "ㄹ")
        self.G.add_edge("ㄷ", "ㅁ")
        self.G.add_edge("ㄷ", "ㅌ")
        self.G.add_edge("ㅁ", "ㅂ")
        self.G.add_edge("ㅂ", "ㅃ")
        self.G.add_edge("ㅁ", "ㅇ")
        self.G.add_edge("ㅁ", "ㅍ")
        self.G.add_edge("ㅅ", "ㅆ")
        self.G.add_edge("ㅅ", "ㅈ")
        self.G.add_edge("ㅈ", "ㅉ")
        self.G.add_edge("ㅈ", "ㅊ")
        self.G.add_edge("ㅇ", "ㅎ")

    def shortest_path(self, source: str, target: str):
        assert source in [ j2hcj(lead) for lead in JAMO_LEADS_MODERN ]
        assert target in [ j2hcj(lead) for lead in JAMO_LEADS_MODERN ]

        return nx.shortest_path(self.G, source, target)

class JungNetwork:
    def __init__(self):
        self.G = nx.Graph()

        self.G.add_edge("ㅡ", "ㅗ")
        self.G.add_edge("ㅗ", "ㅛ")
        self.G.add_edge("ㅗ", "ㅚ")
        self.G.add_edge("ㅡ", "ㅜ")
        self.G.add_edge("ㅜ", "ㅠ")
        self.G.add_edge("ㅜ", "ㅟ")
        self.G.add_edge("ㅢ", "ㅟ")
        self.G.add_edge("ㅟ", "ㅝ")
        self.G.add_edge("ㅝ", "ㅞ")
        self.G.add_edge("ㅢ", "ㅚ")
        self.G.add_edge("ㅚ", "ㅘ")
        self.G.add_edge("ㅘ", "ㅙ")
        self.G.add_edge("ㅢ", "ㅡ")
        self.G.add_edge("ㅢ", "ㅣ")
        self.G.add_edge("ㅣ", "ㅓ")
        self.G.add_edge("ㅣ", "ㅏ")
        self.G.add_edge("ㅓ", "ㅕ")
        self.G.add_edge("ㅓ", "ㅔ")
        self.G.add_edge("ㅕ", "ㅖ")
        self.G.add_edge("ㅔ", "ㅖ")
        self.G.add_edge("ㅏ", "ㅑ")
        self.G.add_edge("ㅏ", "ㅐ")
        self.G.add_edge("ㅑ", "ㅒ")
        self.G.add_edge("ㅐ", "ㅒ")
    
    def shortest_path(self, source: str, target: str):
        assert source in [ j2hcj(vowel) for vowel in JAMO_VOWELS_MODERN ]
        assert target in [ j2hcj(vowel) for vowel in JAMO_VOWELS_MODERN ]

        return nx.shortest_path(self.G, source, target)

class JongNetwork:
    def __init__(self):
        self.G = nx.Graph()

        self.G.add_edge("ㄱ", "ㄲ")
        self.G.add_edge("ㄱ", "ㄴ")
        self.G.add_edge("ㄱ", "ㅋ")
        self.G.add_edge("ㄱ", "ㅅ")
        self.G.add_edge("ㄴ", "ㄷ")
        self.G.add_edge("ㄴ", "ㄵ")
        self.G.add_edge("ㄴ", "ㄶ")
        self.G.add_edge("ㄷ", "ㄸ")
        self.G.add_edge("ㄷ", "ㄹ")
        self.G.add_edge("ㄱ", "ㄺ")
        self.G.add_edge("ㄹ", "ㄺ")
        self.G.add_edge("ㅅ", "ㄽ")
        self.G.add_edge("ㄹ", "ㄽ")
        self.G.add_edge("ㅁ", "ㄻ")
        self.G.add_edge("ㄹ", "ㄻ")
        self.G.add_edge("ㅂ", "ㄼ")
        self.G.add_edge("ㄹ", "ㄼ")
        self.G.add_edge("ㅍ", "ㄿ")
        self.G.add_edge("ㄹ", "ㄿ")
        self.G.add_edge("ㅌ", "ㄾ")
        self.G.add_edge("ㄹ", "ㄾ")
        self.G.add_edge("ㅎ", "ㅀ")
        self.G.add_edge("ㄹ", "ㅀ")
        self.G.add_edge("ㄷ", "ㅁ")
        self.G.add_edge("ㄷ", "ㅌ")
        self.G.add_edge("ㅁ", "ㅂ")
        self.G.add_edge("ㅂ", "ㅃ")
        self.G.add_edge("ㅁ", "ㅇ")
        self.G.add_edge("ㅁ", "ㅍ")
        self.G.add_edge("ㄱ", "ㄳ")
        self.G.add_edge("ㅅ", "ㄳ")
        self.G.add_edge("ㅂ", "ㅄ")
        self.G.add_edge("ㅅ", "ㅄ")
        self.G.add_edge("ㅅ", "ㅆ")
        self.G.add_edge("ㅅ", "ㅈ")
        self.G.add_edge("ㅈ", "ㅉ")
        self.G.add_edge("ㅆ", "ㅉ")
        self.G.add_edge("ㅈ", "ㅊ")
        self.G.add_edge("ㅇ", "ㅎ")
        self.G.add_edge(" ", "ㄱ", weight=5)
        self.G.add_edge(" ", "ㄴ", weight=5)
        self.G.add_edge(" ", "ㅁ", weight=5)
        self.G.add_edge(" ", "ㅅ", weight=5)
        self.G.add_edge(" ", "ㅇ", weight=5)
    
    def shortest_path(self, source: str, target: str):
        assert source in [ j2hcj(tail) for tail in JAMO_TAILS_MODERN ] + [' ']
        assert target in [ j2hcj(tail) for tail in JAMO_TAILS_MODERN ] + [' ']

        return nx.shortest_path(self.G, source, target, weight='weight')

CHO_NX = ChoNetwork()
JUNG_NX = JungNetwork()
JONG_NX = JongNetwork()