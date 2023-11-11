import datetime
import json
import os

class LoggerFactory:
    mapOfLoggers = None

    @classmethod
    def getLogger(cls, loggerName):
        if cls.mapOfLoggers is None:
            cls.mapOfLoggers = {}

        logger = cls.mapOfLoggers.get(loggerName)
        if logger is None:
            logger = Logger(loggerName)
            cls.mapOfLoggers[loggerName] = logger
        return logger

class Logger:
    def __init__(self, loggerName):
        self.loggerName = loggerName

    def fire_the_log(self, completeMsg, jsonContext={}, *extra):
        if not extra:
            # TODO: consider python logger here instead of using `print`
            print(completeMsg)
        else:
            # TODO: consider python logger here instead of using `print`
            print(completeMsg, *extra)

    def buildLogMsg(self, severity, msg, jsonContext):
        messageParts = []
        if is_true_like(os.environ.get("LOG_PREPEND_TIMESTAMP")):
            messageParts.append(datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S UTC'))
        messageParts.append(severity)
        messageParts.append(self.loggerName)
        messageParts.append(msg)
        jsonContextAsString = json.dumps(jsonContext)
        if (jsonContextAsString != "{}"):
          messageParts.append(jsonContextAsString)
        return ' '.join(messageParts)

    def trace(self, msg, jsonContext={}, *extra):
        if is_true_like(os.environ.get("LOG_TRACE")):
            completeMsg = self.buildLogMsg("[ TRACE]", msg, jsonContext)
            self.fire_the_log(completeMsg, jsonContext, *extra)

    def debug(self, msg, jsonContext={}, *extra):
        if is_true_like(os.environ.get("LOG_DEBUG")):
            completeMsg = self.buildLogMsg("[ DEBUG]", msg, jsonContext)
            self.fire_the_log(completeMsg, jsonContext, *extra)


    def info(self, msg, jsonContext={}, *extra):
        if is_true_like(os.environ.get("LOG_INFO")):
            completeMsg = self.buildLogMsg("[  INFO]", msg, jsonContext)
            self.fire_the_log(completeMsg, jsonContext, *extra)


    def notice(self, msg, jsonContext={}, *extra):
        completeMsg = self.buildLogMsg("[NOTICE]", msg, jsonContext)
        self.fire_the_log(completeMsg, jsonContext, *extra)


    def warn(self, msg, jsonContext={}, *extra):
        completeMsg = self.buildLogMsg("[  WARN]", msg, jsonContext)
        self.fire_the_log(completeMsg, jsonContext, *extra)


    def error(self, msg, jsonContext={}, *extra):
        completeMsg = self.buildLogMsg("[ ERROR]", msg, jsonContext)
        self.fire_the_log(completeMsg, jsonContext, *extra)
        # TODO:  Increment an error counter on stathat
        # TODO:  Send a slack message
        # TODO:  Increment an error counter on mixpanel 


def get_logger(loggerName):
    return LoggerFactory.getLogger(loggerName)

def is_true_like(input):
    if input is None:
        return False
    truelike_values = ['true', 'yes', 't', 'y', '1']
    return str(input).strip().lower() in truelike_values

class JSONContext(dict):
    pass
