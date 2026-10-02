"""
text_preprocessor.py - Domain-Specific NLP Preprocessing Pipeline
Handles contraction expansion, negation preservation, educational abbreviation normalization,
and token cleaning for student feedback and academic stress classification.
"""

import re

# Comprehensive contraction mapping
CONTRACTIONS = {
    "can't": "cannot",
    "won't": "will not",
    "shan't": "shall not",
    "don't": "do not",
    "doesn't": "does not",
    "didn't": "did not",
    "isn't": "is not",
    "aren't": "are not",
    "wasn't": "was not",
    "weren't": "were not",
    "haven't": "have not",
    "hasn't": "has not",
    "hadn't": "had not",
    "shouldn't": "should not",
    "wouldn't": "would not",
    "couldn't": "could not",
    "it's": "it is",
    "i'm": "i am",
    "i've": "i have",
    "i'll": "i will",
    "i'd": "i would",
    "you're": "you are",
    "we're": "we are",
    "they're": "they are",
    "that's": "that is",
    "what's": "what is",
    "there's": "there is",
    "let's": "let us",
}

# Educational slang and abbreviations
ACADEMIC_ABBREVIATIONS = {
    r"\bprof\b": "professor",
    r"\bprofs\b": "professors",
    r"\bta\b": "teaching assistant",
    r"\btas\b": "teaching assistants",
    r"\bhw\b": "homework",
    r"\bhws\b": "homeworks",
    r"\bmidterm\b": "midterm exam",
    r"\bmidterms\b": "midterm exams",
    r"\blab\b": "laboratory session",
    r"\blabs\b": "laboratory sessions",
    r"\bgpa\b": "grade point average",
    r"\bdept\b": "department",
    r"\blms\b": "learning management portal",
    r"\bpset\b": "problem set",
    r"\bpsets\b": "problem sets",
}

# Essential sentiment and stress negations to strictly preserve
NEGATION_WORDS = {"not", "no", "never", "cannot", "neither", "nor", "barely", "hardly", "without"}

# Curated non-negation stopwords
GENERAL_STOPWORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and",
    "any", "are", "as", "at", "be", "because", "been", "before", "being", "below",
    "between", "both", "by", "during", "each", "for", "from", "further", "had",
    "has", "have", "having", "he", "her", "here", "hers", "herself", "him", "himself",
    "his", "how", "i", "if", "in", "into", "is", "it", "its", "itself", "me", "more",
    "most", "my", "myself", "of", "off", "on", "once", "only", "or", "other", "our",
    "ours", "ourselves", "out", "over", "own", "same", "she", "so", "some", "such",
    "than", "that", "the", "their", "theirs", "them", "themselves", "then", "there",
    "these", "they", "this", "those", "through", "to", "too", "under", "until", "up",
    "very", "was", "we", "were", "what", "when", "where", "which", "while", "who",
    "whom", "why", "with", "you", "your", "yours", "yourself", "yourselves"
} - NEGATION_WORDS

class TextPreprocessor:
    def __init__(self, preserve_negations=True, expand_abbreviations=True):
        self.preserve_negations = preserve_negations
        self.expand_abbreviations = expand_abbreviations

    def expand_contractions(self, text: str) -> str:
        text = str(text)
        for contraction, expansion in CONTRACTIONS.items():
            pattern = re.compile(re.escape(contraction), re.IGNORECASE)
            text = pattern.sub(expansion, text)
        return text

    def normalize_academic_terms(self, text: str) -> str:
        if not self.expand_abbreviations:
            return text
        for pattern, replacement in ACADEMIC_ABBREVIATIONS.items():
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        return text

    def clean_text(self, text: str) -> str:
        if not text or not isinstance(text, str):
            return ""
        
        # 1. Expand contractions
        text = self.expand_contractions(text)
        
        # 2. Normalize academic domain terms
        text = self.normalize_academic_terms(text)
        
        # 3. Lowercase
        text = text.lower()
        
        # 4. Remove special noise characters but retain basic sentence flow
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        text = re.sub(r'[^\w\s\-\']', ' ', text)
        
        # 5. Tokenize and filter standard non-negation stopwords
        tokens = text.split()
        if self.preserve_negations:
            filtered_tokens = [w for w in tokens if w not in GENERAL_STOPWORDS and len(w) > 1]
        else:
            filtered_tokens = [w for w in tokens if len(w) > 1]
            
        return " ".join(filtered_tokens)

    def transform_series(self, series):
        """Processes a pandas Series of text entries."""
        return series.apply(self.clean_text)

if __name__ == "__main__":
    preprocessor = TextPreprocessor()
    test_samples = [
        "I'm not stressed at all, the prof was super helpful!",
        "Can't handle 3 midterms and 2 psets in one week, feeling totally overwhelmed...",
        "TA ignored my emails about the grading criteria.",
        "I have given up on following these lectures."
    ]
    print("--- Text Preprocessor Verification ---")
    for s in test_samples:
        print(f"Original: {s}")
        print(f"Cleaned : {preprocessor.clean_text(s)}\n")
