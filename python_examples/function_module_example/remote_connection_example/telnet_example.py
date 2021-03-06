import time
import telnetlib
import logging
import sys

__author__ = 'Evan'


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# input parameter check
input_info = sys.argv
if len(input_info) == 3:
    container = input_info[1]
    serial_number = input_info[2]
else:
    raise ValueError('Please attach running parameters,'
                     ' the first parameter is "Container", and the second parameter is "Serial Number"')

save_log_path = '{}_{}.txt'.format(container, serial_number)
file_mode = 'a+'
format_info = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'

# Add record logger function
fh = logging.FileHandler(save_log_path, mode=file_mode)
fh.setLevel(logging.DEBUG)
fh.setFormatter(logging.Formatter(format_info))
logger.addHandler(fh)
# Add display logger function
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter(format_info))
logger.addHandler(ch)


def telnet_handle(host='', port=''):
    handle = telnetlib.Telnet(host, port, timeout=10)
    handle.set_debuglevel(2)  # Display connect info (send command & received info)
    logger.debug('Connect host: {} port: {} successful'.format(host, port))

    # Example
    try:
        handle.read_until('u-boot', timeout=10)  # Capture string
        logger.debug('Captured u-boot mode'.format(host, port))

        # Write is send command
        handle.write('\n')
        handle.write('show\n')
        time.sleep(1)
        handle.write('printenv\n')
        time.sleep(5)

        result = handle.read_very_eager()  # Read all data
        logger.info('Received info: {}'.format(result))
    finally:
        handle.close()

    # TODO Loop listening
    # try:
    #     while True:
    #         time.sleep(5)
    #         result = handle.read_very_eager()
    #         logger.info('Received info: {}'.format(result))
    # finally:
    #     handle.close()


if __name__ == '__main__':
    telnet_handle(host='10.1.1.2', port='2004')
