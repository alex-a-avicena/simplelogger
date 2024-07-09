import re
from datetime import datetime

class Logger():
    def __init__(self):
        """
        Initialize the Logger class.
        """
        self.white      = "\033[0;37m"
        self.blue       = "\033[0;34m"
        self.cyan       = "\033[0;36m"
        self.green      = "\033[0;32m"
        self.yellow     = "\033[0;33m"
        self.red        = "\033[0;31m"
        self.magenta    = "\033[0;35m"
        self.reset      = "\033[0m"
        self.DEBUG = 0
        self.INFO = 1
        self.ATTENTION = 2
        self.WARNING = 3
        self.ERROR = 4
        self.CRITICAL = 5
        self.level = self.INFO
        
    def debug(self, message):
        """
        Log a debug message.
        Args:
            message (str): The message to log.
        """
        if self.level == 0:
            string  = self.white         + self.__datecode() + "    DEBUG: " + message + self.reset
            print(string)
    
    def info(self, message):
        """
        Log an info message.
        Args:
            message (str): The message to log.
        """
        if self.level <= 1:
            string  = self.cyan         + self.__datecode() + "     INFO: " + message + self.reset
            print(string)
        
    def attention(self, message):
        """
        Log an attention message.
        Args:
            message (str): The message to log.
        """
        if self.level <= 2:
            string  = self.green        + self.__datecode() + "ATTENTION: " + message + self.reset
            print(string)
        
    def warning(self, message):
        """
        Log a warning message.
        Args:
            message (str): The message to log.
        """
        if self.level <= 3:
            string  = self.yellow       + self.__datecode() + "  WARNING: " + message + self.reset
            print(string)
        
    def error(self, message):
        """
        Log an error message.
        Args:
            message (str): The message to log.
        """
        if self.level <= 4:
            string  = self.red          + self.__datecode() + "    ERROR: " + message + self.reset
            print(string)
        
    def critical(self, message):
        """
        Log a critical message.
        Args:
            message (str): The message to log.
        """
        if self.level <= 5:
            string  = self.magenta      + self.__datecode() + " CRITICAL: " + message + self.reset
            print(string)
        
    def __datecode(self):
        """
        Get the date code.
        Returns:
            str: The date code.
        """
        now = datetime.now()
        date = now.strftime("%m/%d/%Y %H:%M:%S.%f ")
        return(date)
    
    def set_level(self, level):
        """
        Set the log level.
        Args:
            level (int): The log level.
        """
        self.level = level
        
if __name__ == "__main__":
    logger = Logger()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.attention("This is an attention message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

                