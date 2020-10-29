class PIF(object):
    def __init__(self):
        self.content = []

    def add_to_pif(self, token, sym_table_position):
        self.content.append((token, sym_table_position))

    def __str__(self):
        s = "PIF:\n"
        for x in self.content:
            s += str(x) + "\n"
        return s