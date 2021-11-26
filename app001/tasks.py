from celery import shared_task


@shared_task
def check_sum():
    a = 20
    b = 30
    c = a + b
    print("total sum is :", c)
    return True


check_sum.delay()
