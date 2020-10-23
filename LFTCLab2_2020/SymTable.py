class SymTable(object):
    def __init__(self):
        self.content = []
        self.head = -1

    def add_token(self, token):
        if self.head == -1:
            self.content.append([token, -1])
            self.head = 0
            return 0

        current = self.head
        prev = -1

        #Sortarea alfabetica a pozitiei
        while current != -1 and self.content[current][0] < token:
            prev = current
            current = self.content[current][1]

        if current == -1:
            self.content.append([token, -1])
            self.content[prev][1] = len(self.content)-1
            return self.content[prev][1]

        if self.content[current][0] == token:
            return current

        if prev == -1:
            self.content.append([token, current])
            self.head = len(self.content) - 1
            return len(self.content) - 1

        self.content.append([token, current])
        self.content[prev][1] = len(self.content) - 1

        return len(self.content) - 1

    def __str__(self):
        s = "SymTable:\n"
        for x in self.content:
            s += str(x) + "\n"
        return s



