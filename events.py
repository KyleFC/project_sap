
class Event:
    def __init__(self):
        self.event_handlers = []

    def __iadd__(self, handler):
        self.event_handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.event_handlers.remove(handler)
        return self

    def __call__(self, *args, **keywargs):
        for eventhandler in self.__eventhandlers:
            eventhandler(*args, **keywargs)

class SAPEvents:
    def __init__(self):
        pass

    def on_levelup(self):


if __name__ == '__main__':
    pass
