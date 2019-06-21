# TextAnalyzer

TextAnalyzer extends the [gender-bias app](https://github.com/gender-bias/gender-bias).  It was originally developed as part of my submission to the [Kaggle City of Los Angeles Jobs Competition](https://www.kaggle.com/nelsondata/aaa-biasfree-lajobs) but it can be used to find gender-biased or complex words in any text documents.  To use it, follow this manual installation process. First, install [gender-bias app](https://github.com/gender-bias/gender-bias):

```
git clone https://github.com/gender-bias/gender-bias
cd gender-bias
pip3 install -e .
```

Then, copy these folders into the gender-bias folder. You will replace the original bias detectors because I fixed a bug. And you will add the new bias detectors.

```
/effort  (replace)
/genderedwords (replace)
/personal_life (replace)
/malewords    (add)
/femalewords    (add)
/nonnativewords    (add)
```

Create a folder called ```JBR_BiasText``` in your home folder. Then, run gender-bais using this command.

cat /home/YOUR_HOME_FOLDER/gender-bias/YOUR_JOB_BULLETINS_FOLDER/'311 DIRECTOR  9206 041814.txt' | genderbias > JBR_BiasText/3119.txt
