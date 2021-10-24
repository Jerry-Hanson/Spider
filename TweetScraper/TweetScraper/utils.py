import os

def mkdirs(dirs):
    ''' Create `dirs` if not exist. '''
    if not os.path.exists(dirs):
        os.makedirs(dirs)

import re

def filter_emoji(desstr, restr=''):
    """
    filter emoji
    desstr: origin str
    restr: replace str
    """
    # filter emoji
    try:
        res = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        res = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return res.sub(restr, desstr)
