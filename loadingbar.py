import time
import sys

class loadingbar:
    def __init__(self, total_steps):
        self.total_steps = total_steps
        self.start_time = time.time()
        self.current_step = 0

    def update(self, step):
        self.current_step = step
        elapsed = time.time() - self.start_time
        bar_length = 30
        filled_length = int(bar_length * self.current_step // self.total_steps)
        bar = "#" * filled_length + "-" * (bar_length - filled_length)

        sys.stderr.write(
            f"\r[{bar}] {self.current_step}/{self.total_steps} | Elapsed: {elapsed:.2f}s"
        )
        sys.stderr.flush()

    def log(self, message):
        sys.stderr.write("\r" + " " * 80 + "\r")
        sys.stderr.flush()
        print(message)

    def elapsed_time(self):
        return time.time() - self.start_time

    def finish(self):
        self.update(self.total_steps)
        sys.stderr.write("\n")
        sys.stderr.flush()
