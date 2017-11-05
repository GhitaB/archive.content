from collective import dexteritytextindexer
from plone.app.textfield import RichText
from plone.supermodel import model
from zope.interface import Interface


class IArchiveContentInstalled(Interface):
    """ Browser layer interface
    """


class IEmail(model.Schema):
    """ Archive Email
    """

    dexteritytextindexer.searchable('body')
    body = RichText(
        title=u'Email Body',
        description=u'The Message'
    )
