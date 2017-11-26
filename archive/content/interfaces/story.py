from archive.content.content.util import PRIORITY_TYPES_VOCAB
from collective import dexteritytextindexer
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema


class IStory(model.Schema):
    """ Archive Story
    """
    dexteritytextindexer.searchable('writing_time')
    writing_time = schema.Datetime(
        title=u"Writing time",
        required=True,
        description=u"Date and time of writing"
    )

    dexteritytextindexer.searchable('body')
    body = RichText(
        title=u'Email Body',
        description=u'The Message',
        required=True
    )

    dexteritytextindexer.searchable('priority')
    priority = schema.Choice(
        title=u"Priority",
        description=u'How important the message is',
        vocabulary=PRIORITY_TYPES_VOCAB,
        required=True
    )
