from Products.Five.browser import BrowserView
from archive.content.content.util import PRIORITY_TYPES_VOCAB
from archive.content.content.util import human_readable_datetime


class StoryView(BrowserView):
    """ Story View
    """

    @property
    def writing_time(self):
        return human_readable_datetime(self.context.writing_time)

    @property
    def priority(self):
        return PRIORITY_TYPES_VOCAB.getTerm(self.context.priority).title
