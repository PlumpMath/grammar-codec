
# from wikipedia_common import words
#
# verb_list = d['Verbs']
# noun_list = d['Nouns']

from basic_english import words

verb_list = words['OPERATIONS']
noun_list = words['GENERAL_THINGS'] + words['PICTURE_THINGS']


def _divmod(n, m):
    return (n / m), (n % m)


def encode(n):
    ret = []
    while n > 0:
        res, n = sentence(n)
        ret.append(res)
    return ' '.join(ret)


def sentence(n):
    res, rem = _divmod(n, 2)
    if rem == 0:
        ret, res = question(res)
    elif rem == 1:
        ret, res = statement(res)
    return (ret[0].upper() + ret[1:]), res


def question(n):
    np, res = noun_phrase(n)
    vp, res = verb_phrase(res)
    return ('does %s %s?' % (np, vp)), res


def statement(n):
    np, res = noun_phrase(n)
    vp, res = verb_phrase(res)
    return ('%s %s.' % (np, vp)), res


def verb_phrase(n):
    return verb(n)


def verb(n):
    return pick(n, verb_list)


def noun_phrase(n):
    res, rem = _divmod(n, 3)
    if rem == 0:
        article = 'the'
    elif rem == 1:
        article = 'a'
    elif rem == 2:
        article = None
    np, res = noun(res)
    if article is not None:
        np = '%s %s' % (article, np)
    return np, res


def noun(n):
    return pick(n, noun_list)


def pick(n, items):
    size = len(items)
    res, rem = _divmod(n, size)
    item = items[rem]
    return item, res
