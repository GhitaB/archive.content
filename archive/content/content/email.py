""" Definition of the Email dexterity content type
"""
from zope.interface import implementer
from archive.content.interfaces.email import IEmail
from plone.dexterity.content import Container


@implementer(IEmail)
class Email(Container):
    """ Archive Email Item
    """
