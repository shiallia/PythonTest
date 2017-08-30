import logging

logger = logging.getLogger("日志")
logger.setLevel(logging.DEBUG)

#输出到屏幕
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#输出到文件
fh = logging.FileHandler("log8.log", encoding="UTF-8")
fh.setLevel(logging.DEBUG)
#设置日志格式
fomatter = logging.Formatter('%(asctime)s:   %(message)s')
ch.setFormatter(fomatter)
fh.setFormatter(fomatter)
logger.addHandler(ch)
#logger.addHandler(fh)

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")

input()