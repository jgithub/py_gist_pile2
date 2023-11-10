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
            if not extra:
                # TODO: consider python logger here instead of using `print`
                print(completeMsg)
            else:
                print(completeMsg, *extra)

    def debug(self, msg, jsonContext={}, *extra):
        if is_true_like(os.environ.get("LOG_DEBUG")):
            completeMsg = self.buildLogMsg("[ DEBUG]", msg, jsonContext)
            if not extra:
                print(completeMsg)
            else:
                print(completeMsg, *extra)

    def info(self, msg, jsonContext={}, *extra):
        if is_true_like(os.environ.get("LOG_INFO")):
            completeMsg = self.buildLogMsg("[  INFO]", msg, jsonContext)
            if not extra:
                print(completeMsg)
            else:
                print(completeMsg, *extra)

    def notice(self, msg, jsonContext={}, *extra):
        completeMsg = self.buildLogMsg("[NOTICE]", msg, jsonContext)
        if not extra:
            print(completeMsg)
        else:
            print(completeMsg, *extra)

    def warn(self, msg, jsonContext={}, *extra):
        completeMsg = self.buildLogMsg("[  WARN]", msg, jsonContext)
        if not extra:
            print(completeMsg)
        else:
            print(completeMsg, *extra)

    def error(self, msg, jsonContext={}, *extra):
        completeMsg = self.buildLogMsg("[ ERROR]", msg, jsonContext)
        if not extra:
            print(completeMsg)
        else:
            print(completeMsg, *extra)

def get_logger(loggerName):
    return LoggerFactory.getLogger(loggerName)

def is_true_like(input):
    if input is None:
        return False
    truelike_values = ['true', 'yes', 't', 'y', '1']
    return str(input).strip().lower() in truelike_values

class JSONContext(dict):
    pass
