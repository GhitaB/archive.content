from collections import OrderedDict
from collective import dexteritytextindexer
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema
from zope.interface import Interface
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


class IArchiveContentInstalled(Interface):
    """ Browser layer interface
    """


class IEmail(model.Schema):
    """ Archive Email
    """

    dexteritytextindexer.searchable('sender')
    sender = schema.TextLine(
        title=u"Sender",
        required=True,
        description=u"Email address"
    )

    dexteritytextindexer.searchable('receiver')
    receiver = schema.TextLine(
        title=u"Receiver",
        required=True,
        description=u"Email address"
    )

    dexteritytextindexer.searchable('body')
    body = RichText(
        title=u'Email Body',
        description=u'The Message',
        required=True
    )

    dexteritytextindexer.searchable('story')
    story = RichText(
        title=u'Story',
        description=u'Some details about the context'
    )

    priority = schema.Choice(
        title=u"Priority",
        description=u'How important the message is',
        vocabulary=PRIORITY_TYPES_VOCAB,
        required=True
    )
