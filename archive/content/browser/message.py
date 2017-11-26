from Products.Five.browser import BrowserView
from archive.content.content.util import PRIORITY_TYPES_VOCAB
from archive.content.content.util import human_readable_datetime


class MessageView(BrowserView):
    """ Message View
    """

    @property
    def sending_time(self):
        return human_readable_datetime(self.context.sending_time)

    @property
    def priority(self):
        return PRIORITY_TYPES_VOCAB.getTerm(self.context.priority).title
