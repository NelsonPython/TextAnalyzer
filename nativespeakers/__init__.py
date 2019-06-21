from genderbias.detector import Detector, Flag, Issue, Report
import os
import re
import pandas as pd

_dir = os.path.dirname(__file__)
NATIVE_WORDS = pd.read_csv(_dir + "/Englishwords.wordlist")

class NativeSpeakerDetector(Detector):
    
    def get_report(self, doc):
        nativespeaker_report = Report("\nTerms biased towards native speakers:")
        words_with_indices = doc.words_with_indices()
        #print(words_with_indices)

        found = False
        for word, start, stop in words_with_indices:
            word = word.lower()
            for nativeword in NATIVE_WORDS.Used:
                x = re.search(nativeword, word)
                if (x):
                    #print(x.span(), x.string, x.group())
                    found = True
                    if NATIVE_WORDS['Recommend2'].loc[NATIVE_WORDS['Used'] == x.group()].item() == 'none':
                        recommend2 = ""
                    else:
                        recommend2 = " or '" + NATIVE_WORDS['Recommend2'].loc[NATIVE_WORDS['Used'] == x.group()].item() + "'"

                    print("Consider replacing '", x.group(), "' with '", NATIVE_WORDS['Recommend1'].loc[NATIVE_WORDS['Used'] == x.group()].item(), "'", recommend2)
                    nativespeaker_report.add_flag(
                        Flag(start, stop, Issue(word))
                        )
        if found:
            nativespeaker_report.set_summary("To encourage non-native speakers, use short words and simple sentences")
        return nativespeaker_report

