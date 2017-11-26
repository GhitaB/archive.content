from archive.content.content.util import PRIORITY_TYPES_VOCAB
from collective import dexteritytextindexer
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema
from zope.interface import Interface


class IArchiveContentInstalled(Interface):
    """ Browser layer interface
    """


class IEmail(model.Schema):
    """ Archive Email
    """
    dexteritytextindexer.searchable('sending_time')
    sending_time = schema.Datetime(
        title=u"Sending time",
        required=True,
        description=u"Date and time of sending"
    )

    dexteritytextindexer.searchable('email_subject')
    email_subject = schema.TextLine(
        title=u"Subject",
        required=True,
        description=u"Email subject"
    )

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

    dexteritytextindexer.searchable('priority')
    priority = schema.Choice(
        title=u"Priority",
        description=u'How important the message is',
        vocabulary=PRIORITY_TYPES_VOCAB,
        required=True
    )


class IMessage(model.Schema):
    """ Archive Message
    """
    dexteritytextindexer.searchable('sending_time')
    sending_time = schema.Datetime(
        title=u"Sending time",
        required=True,
        description=u"Date and time of sending"
    )

    dexteritytextindexer.searchable('sender')
    sender = schema.TextLine(
        title=u"Sender",
        required=True,
        description=u"Sender Name"
    )

    dexteritytextindexer.searchable('receiver')
    receiver = schema.TextLine(
        title=u"Receiver",
        required=True,
        description=u"Receiver Name"
    )

    dexteritytextindexer.searchable('body')
    body = RichText(
        title=u'Message Body',
        description=u'The Message',
        required=True
    )

    dexteritytextindexer.searchable('story')
    story = RichText(
        title=u'Story',
        description=u'Some details about the context'
    )

    dexteritytextindexer.searchable('priority')
    priority = schema.Choice(
        title=u"Priority",
        description=u'How important the message is',
        vocabulary=PRIORITY_TYPES_VOCAB,
        required=True
    )
