import re

def normalize_nrc(nrc):
    nrc0 = str(nrc.partition('(N)'))
    nrc1 = nrc0.split('/')
    return str(nrc1).upper()
    # nrc1 = str(re.findall(r"[\w']+", nrc))
    # return nrc1.upper()

print(normalize_nrc('9/pamana(N)217289'))