""" Definition of the Email dexterity content type
"""
from zope.interface import implementer
from archive.content.interfaces.email import IEmail
from plone.dexterity.content import Item


@implementer(IEmail)
class Email(Item):
    """ Archive Email Item
    """
