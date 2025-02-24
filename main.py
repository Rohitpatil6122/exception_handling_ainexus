import logging
# default will execute
logging.basicConfig(level=20,filename='rohit.txt',filemode='a',format="%(asctime)s:%(name)s:%(levelname)s",datefmt="%d-%m-%y")
logging.critical("critical message")
logging.error("error message ")
logging.warning("warning message ")
logging.info("info message")

