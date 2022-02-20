import html
from functools import singledispatch
import numbers
# collections 에서 지원하는 추상 베이스 클래스들
# 예: abc.Hashable (__hash__), abc.Iterable (__iter__), abc.Callable (__call__)
from collections import abc

@singledispatch
def htmlize(obj):
    """ this is generic function """
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    """ data type: `str` """
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    """ data type: `int` """
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    """ data type: list, tuple """
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


if __name__ == '__main__':
    print(htmlize(abs))
    print(htmlize('Heimlich & Co.\n- a game'))
    print(htmlize(42))
    print(htmlize([1,2,3,4]))
