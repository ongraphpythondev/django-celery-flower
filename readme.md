
# Celery-flower

A poc for monitoring your celery tasks and workers.






## flower :
Flower is a web based tool for monitoring and administrating Celery clusters. It has these features:

    Real-time monitoring using Celery Events

            Task progress and history
            Ability to show task details (arguments, start time, runtime, and more)
            Graphs and statistics

    Remote Control

            View worker status and statistics
            Shutdown and restart worker instances
            Control worker pool size and autoscale settings
            View and modify the queues a worker instance consumes from
            View currently running tasks
            View scheduled tasks (ETA/countdown)
            View reserved and revoked tasks
            Apply time and rate limits
            Configuration viewer
            Revoke or terminate tasks

    Broker monitoring

            View statistics for all Celery queues
            Queue length graphs

## Setup Flower for your Celery :

    1. Install flower with pip

            pip install flower

    2. Launch from celery(in terminal)

            celery flower -A proj flower --address=127.0.0.1 --port=5555
            (flower will be running on localhost:5555)

    hint = "proj" is your django project_name
