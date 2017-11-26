""" Definition of the Simple Message dexterity content type
"""
from zope.interface import implementer
from archive.content.interfaces.message import IMessage
from plone.dexterity.content import Item


@implementer(IMessage)
class Message(Item):
    """ Archive Simple Message Item
    """
