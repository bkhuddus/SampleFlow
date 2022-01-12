#import prefect
#from prefect import task, Flow
#
#@task
#def hello_task():
#    logger = prefect.context.get("logger")
#    logger.info("Hello world!")
#
#@task
#def hello_task2():
#    logger = prefect.context.get("logger")
#    logger.info("Hello task2!")
#
#flow = Flow("Hello-Flow", tasks=[hello_task, hello_task2])
#
#flow.run()

#---------------


import prefect
from prefect import task, Flow

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")

flow = Flow("hello-flow", tasks=[hello_task])

flow.register(project_name="tester")