""" Definition of the Story dexterity content type
"""
from zope.interface import implementer
from archive.content.interfaces.story import IStory
from plone.dexterity.content import Container


@implementer(IStory)
class Story(Container):
    """ Archive Story Item
    """
