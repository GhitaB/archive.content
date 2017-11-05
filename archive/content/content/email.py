""" Definition of the Email dexterity content type
"""
from zope.interface import implementer
from archive.content.interfaces import IEmail
from plone.dexterity.content import Item


@implementer(IEmail)
class Infonote(Item):
    """ Archive Email Item
    """
