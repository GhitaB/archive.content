""" Definition of the Simple Message dexterity content type
"""
from zope.interface import implementer
from archive.content.interfaces.message import IMessage
from plone.dexterity.content import Container


@implementer(IMessage)
class Message(Container):
    """ Archive Simple Message Item
    """
