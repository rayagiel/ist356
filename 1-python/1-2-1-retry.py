# this is an example of a retry loop

from time import sleep

TIMES = 5
BACKOFF = 5

def progressed(delay:int):
    for i in range(delay):
        if i%2 == 0:
            print(f"X", end="", flush=True)
        else:
            print(f"O", end="", flush=True)
        sleep(1)
        print(f"\b", end="", flush=True)

print("Staring the retry loop...")
for attempt in range(TIMES):
    sleep(BACKOFF*(attempt +1))
    print(f"Attempt {attempt+1} of {TIMES}")
    delay = BACKOFF*(attempt)
    print (f"Sleeping for {delay} seconds...")
    progressed(delay)
    print ("Retrying Now")

