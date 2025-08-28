"""
10. Exponential Backoff
Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

"""
import time

wait_time = 1
max_retries = 5
attemts = 0

while attemts < max_retries:
    print("Attempt",attemts+1,"- Wait time",wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attemts += 1