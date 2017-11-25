from collections import OrderedDict
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


PRIORITY_TYPES = OrderedDict([
    (u'1', u'1 - Low'),
    (u'2', u'2 - Normal'),
    (u'3', u'3 - Important'),
    (u'4', u'4 - Very Important'),
])


PRIORITY_TYPES_VOCAB = SimpleVocabulary(
    [
        SimpleTerm(
            value=x,
            title=PRIORITY_TYPES[x])
        for x in PRIORITY_TYPES.keys()
    ]
)


def human_readable_datetime(datetime_obj):
    return datetime_obj.strftime("%A %d.%m.%Y %H:%M")
