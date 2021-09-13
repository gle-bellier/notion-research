from logging import info
import re
import textract
from dateparser.search import search_dates
from scholarly import scholarly


class Article:
    def __init__(self, text):
        self.text = text
        self.article = self.isArticle()
        self.title = self.extract_title()

    def isArticle(self):
        return "arXiv" in self.text[:1000]

    def clean_title(self, title):
        cl_title = ""
        skip = False
        for i, c in enumerate(title):
            if skip:
                skip = False
            else:
                if c == "\\":
                    if i + 1 <= len(title) - 1 and title[i + 1] == "n":
                        cl_title += " "
                        skip = True
                else:
                    if i > 1 and i + 1 <= len(title) - 1 and title[
                            i - 1] == title[i + 1] == " ":
                        skip = True

                    cl_title += c
        return cl_title

    def extract_title(self):
        i_arxiv = self.text.find("arXiv")
        return self.clean_title(self.text[2:i_arxiv])

    def get_info(self):
        try:
            query = scholarly.search_pubs(self.title)
            pub = next(query)
            print(pub)
            #self.bibtex = scholarly.bibtex(pub)
            # self.author = pub["author"]
            # self.title = pub["author"]
            #print(self.bibtex)

        except:
            print("Can not acces bibtex")


# @article{chen2020wavegrad,
#  abstract = {This paper, introduces WaveGrad, a conditional model for waveform generation which estimates gradients of the data density. The model is built on prior work on score matching and diffusion probabilistic models. It starts from a Gaussian white noise signal and iteratively refines the signal via a gradient-based sampler conditioned on the mel-spectrogram. WaveGrad offers a natural way to trade inference speed for sample quality by adjusting the number of refinement steps, and bridges the gap between non-autoregressive and},
#  author = {Chen, Nanxin and Zhan, Yu and Zen, Heiga and Weiss, Ron J and Norouzi, Mohammad and Chan, William},
#  journal = {arXiv preprint arXiv:2009.00713},
#  pub_year = {2020},
#  title = {WaveGrad: Estimating gradients for waveform generation},
#  venue = {arXiv preprint arXiv …}
# }

article = Article(str(textract.process("article2.pdf")))
# print(article.extract_abstract())
# print(article.extract_date())
#
print(article.title)
print(article.get_info())