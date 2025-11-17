import redis
import time

pool = redis.ConnectionPool().from_url("redis://redis")
last = 0


def store(paths):
    with open("out/paths.txt", 'wb') as f:
        for path in paths:
            f.write(path + b'\n')

if __name__ == '__main__':
    while True:
        time.sleep(10)
        with redis.Redis().from_pool(pool) as r:
            try:
                recs = r.scard("paths")
                print(f"[+] Got {recs} records")
                if last >= recs:
                    print(" ... no new records to store")
                    continue

                print(f"[+] Storing {recs} records")

                paths = r.smembers("paths")
                store(paths)

                print(f"[+] Stored {recs} records")
            except redis.exceptions.ConnectionError:
                print("[ERR] Redis connection error this time...")
