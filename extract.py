import re


def get_ccode(nrc):
    nrc_lower = nrc.lower()
    ccode, other = nrc_lower.split('/')
    return ccode

def get_cname(nrc):
    nrc_lower = nrc.lower()
    ccode, other = nrc_lower.split('/')
    cname, other_part = other.split('(')
    return cname

def get_nation(nrc):
    nrc_lower = nrc.lower()
    ccode, other = nrc_lower.split('/')
    cname, other_part = other.split('(')
    nation, nrc_id = other_part.split(')')
    return nation

def get_nrc_id(nrc):
    nrc_lower = nrc.lower()
    ccode, other = nrc_lower.split('/')
    cname, other_part = other.split('(')
    nation, nrc_id = other_part.split(')')
    return nrc_id