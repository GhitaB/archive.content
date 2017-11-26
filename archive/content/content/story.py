""" Definition of the Story dexterity content type
"""
from zope.interface import implementer
from archive.content.interfaces.story import IStory
from plone.dexterity.content import Item


@implementer(IStory)
class Story(Item):
    """ Archive Story Item
    """
