# Level Logger

Level Logger is a Python class that provides a simple and customizable logging system with colored output. It allows you to log messages at different levels of severity and customize the appearance of your log messages.

![image](https://github.com/user-attachments/assets/80b68150-a0e2-4d62-9b9a-4be675757f53)

## Features

- Six logging levels: DEBUG,  INFO,  ATTENTION,  WARNING,  ERROR, and  CRITICAL
- Colored output for easy visual distinction between log levels
- Customizable message header
- Ability to enable/disable logging
- Timestamp included with each log message

## Installation

To use the Level Logger, run `pip install levellogger`

## Usage

Here's a basic example of how to use the Logger:

      from levellogger import Logger

      # Initialize the logger
      logger = Logger(level="DEBUG", header="MyApp")
      
      # Log messages at different levels
      logger.debug("This is a debug message")
      logger.info("This is an info message")
      logger.attention("This is an attention message")
      logger.warning("This is a warning message")
      logger.error("This is an error message")
      logger.critical("This is a critical message")


## API Reference

### Constructor

      Logger(level: Union[int, str] = "INFO", header: str = None)
      
- `level`: The initial log level. Can be a string ("DEBUG", "INFO", "ATTENTION", "WARNING", "ERROR", "CRITICAL") or an integer (0-5). Defaults to "INFO".
- `header`: An optional message header to be included in all log messages.

### Methods

- `set_message_header(header: str)`: Set the message header.
- `enable_logging()`: Enable logging.
- `disable_logging()`: Disable logging.
- `debug(message: str)`: Log a debug message.
- `info(message: str)`: Log an info message.
- `attention(message: str)`: Log an attention message.
- `warning(message: str)`: Log a warning message.
- `error(message: str)`: Log an error message.
- `critical(message: str)`: Log a critical message.
- `set_level(level: int)`: Set the log level.

## Example

      logger = Logger()
      logger.set_level(logger.DEBUG)
      logger.set_message_header("Test Logger")
      logger.debug("This is a debug message")
      logger.info("This is an info message")
      logger.attention("This is an attention message")
      logger.warning("This is a warning message")
      logger.error("This is an error message")
      logger.critical("This is a critical message")

This will output colored log messages with timestamps and the specified header.

## License

This project is open-source and available under the GNU 3 License.
