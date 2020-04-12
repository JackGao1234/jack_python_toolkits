import logging
import sys
import io


print('====1st logger: log to file====')
first_logger = logging.getLogger('logging tutorial')
file_handler = logging.FileHandler('logging_in_python.log')
formatter = logging.Formatter('[first_logger] %(asctime)s %(levelname)s %(message)s')
file_handler.setFormatter(formatter)
first_logger.addHandler(file_handler)
first_logger.setLevel(logging.INFO)

first_logger.info('hahaha')
first_logger.info('can you see me?')
first_logger.critical("How about this?")
first_logger.critical("Change \n line?")


print('====2nd logger: print with custom format====')
second_logger = logging.getLogger('second logger')
formatter = logging.Formatter('[%(name)s] %(asctime)s %(levelname)s %(message)s')
stdout_handler = logging.StreamHandler(sys.stdout)  # stderr is the default
stdout_handler.setFormatter(formatter)
second_logger.addHandler(stdout_handler)
second_logger.setLevel(logging.INFO)

second_logger.info('hahaha')
second_logger.info('can you see me?')
second_logger.critical("How about this?")
second_logger.critical("Change \n line?")


print('====3rd logger: cutomize handler and formater====')
class MyHandler(logging.Handler):
    def emit(self, record):
        msg = self.format(record)
        print("[costom_logger]", msg)
        print("hello I'm custom handler")


class MyFormatter(logging.Formatter):
    default_fmt = logging.Formatter('%(levelname)s in [%(name)s]: %(message)s')
    info_fmt = logging.Formatter('%(levelname)s %(asctime)s - %(message)s')

    # how you compose a string by record (data type: LogRecord)
    def format(self, record):
        if record.levelno == logging.INFO:
            return self.info_fmt.format(record)
        else:
            return self.default_fmt.format(record)


third_logger = logging.getLogger('custom logger')
custom_handler = MyHandler()
formatter = MyFormatter()
custom_handler.setFormatter(formatter)
third_logger.addHandler(custom_handler)
third_logger.setLevel(logging.DEBUG)

third_logger.info('msg into another handler')
third_logger.critical('can you see me?')
third_logger.debug('debug msg')


print('====4th logger: cutomize formater for multiple parameters====')
class MultipleParamsFormatter(logging.Formatter):
    def format(self, record):
        record.message2 = record.args[0]
        record.args = None
        return super().format(record)

fourth_logger = logging.getLogger('test')
console_output_handler_with_multiple_params = logging.StreamHandler(sys.stdout)
console_output_handler_with_multiple_params.setFormatter(MultipleParamsFormatter('%(asctime)s - %(message2)s - %(name)s - %(levelname)s - %(message)s'))
fourth_logger.addHandler(console_output_handler_with_multiple_params)

fourth_logger.setLevel(logging.DEBUG)
fourth_logger.info("[first msg]", "[second msg]")


print('====5th logger: multiple handlers====')
fifth_logger = logging.getLogger('fifth logger')
fifth_logger.addHandler(stdout_handler)
fifth_logger.addHandler(custom_handler)

fifth_logger.setLevel(logging.DEBUG)
fifth_logger.info('first msg')
fifth_logger.debug('second msg')


print('====6th logger: stringIO handler====')
sixth_logger = logging.getLogger('sixth logger')

# add StringIO handler
stream_capture = io.StringIO()
streaming_io_handler = logging.StreamHandler(stream_capture)
streaming_io_fmt = logging.Formatter("---I'm StringIO---%(message)s")
streaming_io_handler.setFormatter(streaming_io_fmt)
sixth_logger.addHandler(streaming_io_handler)

# add stdout handler for comparison
stdout_handler.setFormatter(logging.Formatter("I'm stdout handler---%(message)s"))
sixth_logger.addHandler(stdout_handler)

sixth_logger.setLevel(logging.DEBUG)
sixth_logger.info('first msg')
print(stream_capture.getvalue())
sixth_logger.debug('second msg')
print(stream_capture.getvalue())
sixth_logger.critical('third msg')
print(stream_capture.getvalue())
# stream_capture will keep adding without stream_capture.seek(0) & stream_capture.truncate(0)

stream_capture.truncate(0)
stream_capture.seek(0)
sixth_logger.info('After we flush the StringIO, log again to see the StringIO')
print(stream_capture.getvalue())
