"""
Women are more associated with family and personal life.

Goal: Develop code that can read text for terms related to personal life like
family, children, etc. If the text includes personal life details; return a
summary that directs the author to review the personal life details for
relevance and consider removing them if they are not relevant to the
recommendation or evaluation.
"""

from genderbias.document import Document
from genderbias.detector import Detector, Flag, Issue, Report

PERSONAL_LIFE_TERMS = [
    "child",
    "children",
    "family",
    "girlfriend",
    "maternal",
    "mother",
    "motherly",
    "spouse",
    "wife"
]

class PersonalLifeDetector(Detector):
    """
    This detector checks for words that relate to personal life instead of
    professional life.

    Links:
        https://github.com/molliem/gender-bias/issues/9
        http://journals.sagepub.com/doi/pdf/10.1177/0957926503014002277

    """

    def get_report(self, doc):
        """
        Generate a report on the text based upon mentions of
        personal-life-related words.

        Arguments:
            doc (Document): The document to check

        Returns:
            Report

        """
        report = Report("\nTerms about personal life")

        token_indices = doc.words_with_indices()

        found = False
        for word, start, stop in token_indices:
        # NELSON - changed loop to look for word in lis of PERSONAL_LIFE_TERMS
            if word.lower() in PERSONAL_LIFE_TERMS:
                found = True
                report.add_flag(
                    Flag(start, stop, Issue(
                        "{word}".format(word=word)
                    ))
                )

        if found:
            report.set_summary('Found words relating to personal life')
        return report


def personal_life_terms_prevalence(doc: 'Document') -> float:
    """
    Returns the prevalence of tems that refer to personal life.

    Returns the floating-point ratio of `personal`/`total`.

    Arguments:
        doc (Document): The document to check

    Returns:
        float: The "concentration" of personal-life terms

    """
    doc_words = doc.words()

    return float(sum([
        word in PERSONAL_LIFE_TERMS
        for word in doc_words
    ])) / len(doc_words)
