#!/usr/bin/env python3

"""
Check for the usage of strange or unnatural gendered words.

"""


import os
from genderbias.detector import Detector, Flag, Issue, Report

_dir = os.path.dirname(__file__)


GENDERED_WORDS = [
    w.strip()
    for w in open(
    _dir + "/genderedwords.wordlist", 'r').readlines()
]


class GenderedWordDetector(Detector):
    """
    This detector checks for words that call unnecessary attention to the
    gender of the letter recipient.

    """

    def get_report(self, doc):
        """
        Report the usage of unnecessarily gendered words.

        Arguments:
            doc (Document): The document to check

        Returns:
            Report

        """
        report = Report("\nUnnecessary use of gender terms")

        token_indices = doc.words_with_indices()

        found = False
        for word, start, stop in token_indices:
        # NELSON - changed loop so word can be found in GENDERED_WORDS
            if word.lower() in GENDERED_WORDS:
                found = True
                report.add_flag(
                        Flag(start, stop, Issue(
                            "{word}".format(word=word)
                            ))
                )

        if found:
            report.set_summary("Replace gender terms with 'person' or 'individual', or a position-specific term, such as 'doctor' or 'author'")
        return report
