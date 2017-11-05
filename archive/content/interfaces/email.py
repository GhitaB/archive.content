from zope.interface import Interface
from plone.supermodel import model
from plone.app.textfield import RichText


class IArchiveContentInstalled(Interface):
    """ Browser layer interface
    """


class IEmail(model.Schema):
    """ Archive Email
    """

    body = RichText(
        title=u'Email Body',
        description=u'The Message'
    )
