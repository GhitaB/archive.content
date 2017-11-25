from Products.Five.browser import BrowserView
from archive.content.interfaces.email import PRIORITY_TYPES_VOCAB


class EmailView(BrowserView):
    """ Infonote View
    """

    @property
    def priority(self):
        return PRIORITY_TYPES_VOCAB.getTerm(self.context.priority).title
