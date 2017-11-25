from Products.Five.browser import BrowserView
from archive.content.interfaces.email import PRIORITY_TYPES_VOCAB


def human_readable_datetime(datetime_obj):
    return datetime_obj.strftime("%d.%m.%Y %H:%M")


class EmailView(BrowserView):
    """ Infonote View
    """

    @property
    def sending_time(self):
        return human_readable_datetime(self.context.sending_time)

    @property
    def priority(self):
        return PRIORITY_TYPES_VOCAB.getTerm(self.context.priority).title
