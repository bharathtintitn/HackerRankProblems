import sys
import pdb

h = [None]
class HistoryPrompt(object):
    pdb.set_trace()
    def __init__(self, string='h[%d] >>>'):
        self.str = string
    def __str__(self):
        try:
            if _ not in [h[-1], None, h]:
                h.append(_)
        except NameError:
            pass
        return self.str % len(h)

    def __radd__(self, other):
        return str(other) + str(self)

sys.ps1 = HistoryPrompt()
