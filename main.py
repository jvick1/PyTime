import time
from datetime import date


"""UPDATE PATH + CREATE LOGS FOLDER BEFORE RUNNING"""


path = 'YOUR PATH'
startTime = time.time()
today = date.today()


#####your python script#####


executionTime = (time.time() - startTime)
log = open(path + "logs/logs.txt", "a")
log.write(f"Last Ran: {today} | Execution Time: {str(executionTime)} seconds | User Notes: \n")
