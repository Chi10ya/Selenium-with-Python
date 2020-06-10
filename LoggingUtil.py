# **************** 29: Logging | Generate Log file
# Approach 2 - by creating an object

import logging

logging.basicConfig(
                    filename = "C:\\ScreenShots-nd-Logs\\test.log",
                    format = '%(asctime)s: %(levelname)s: %(message)s',
                    datefmt = '%d-%m-%Y %I:%M:%S %p'
                    )

logMe = logging.getLogger()
logMe.setLevel(logging.DEBUG)
logMe.setLevel(logging.CRITICAL)
logMe.setLevel(logging.ERROR)

logMe.debug("This is debug message")
logMe.info("This is info message")
logMe.warning("This is warning message")
logMe.error("This is error message")
logMe.critical("This is critical message")
