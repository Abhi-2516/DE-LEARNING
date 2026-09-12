# Python Concurrency: Threads, Processes, and the GIL

## 1. What this module teaches

This folder introduces Python concurrency through small, runnable examples:

- **Threading**: running multiple tasks within one process.
- **Multiprocessing**: running tasks in separate processes.
- **The GIL**: why CPU-bound Python threads usually do not execute Python bytecode in parallel in standard CPython.
- **Coordination**: waiting for workers, protecting shared state, and passing data between processes.
- **Practical selection**: choosing threads for waiting-heavy work and processes for CPU-heavy work.

Concurrency means that multiple tasks make progress during the same period. Parallelism means that multiple tasks execute at the same instant on different CPU cores. Threads can provide concurrency for I/O, while processes can provide true CPU parallelism.

---

## 2. The essential mental model

### Thread

A thread is an execution path inside a process.

- Threads in one process share the same memory, variables, and open resources.
- Creating and switching between threads is relatively lightweight.
- Shared memory is convenient, but it creates race-condition risks.
- Threads are a good fit for I/O-bound work: network requests, file operations, waiting for APIs, and database calls.

### Process

A process is an independent operating-system execution unit.

- Each process has its own memory space and Python interpreter state.
- Processes are more expensive to create than threads.
- Data is not automatically shared; it must be sent through IPC mechanisms such as queues, pipes, or shared memory.
- Separate processes can execute CPU-bound Python code in parallel on multiple cores.

### The GIL

The Global Interpreter Lock is a CPython implementation detail. It allows only one thread at a time to execute Python bytecode in a CPython process.

Consequences:

- CPU-bound pure-Python threads generally do not scale across CPU cores.
- I/O-bound threads can still be effective because a thread waiting on I/O releases execution time for another thread.
- Some native extensions release the GIL while doing work, so the simple rule is not universal.
- Multiprocessing uses separate interpreters and therefore avoids one process's GIL limiting another process.

The GIL is not a replacement for a lock. It does not make every multi-step operation logically safe, and it does not protect shared data across processes.

---

## 3. File-by-file revision notes

### `01_threading.py`: two independent tasks

`take_orders()` sleeps for 2 seconds per order, while `brew_chai()` sleeps for 3 seconds per chai. Each function runs in its own `threading.Thread`.

Important pattern:

```python
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

order_thread.join()
brew_thread.join()
```

- `target` is the callable executed by the thread.
- `start()` schedules the thread to begin.
- `join()` makes the main thread wait until that worker finishes.
- The combined elapsed time is approximately the slower task's time, not the sum of both task times, subject to scheduling overhead.
- Output order is nondeterministic because both threads run concurrently.

### `02_multiprocessing.py`: one process per chai maker

Three `Process` objects run `brew_chai()` independently. Each worker sleeps for 3 seconds.

Key lessons:

- `args=(f"Chai Maker #{i+1}",)` is a one-item tuple. The trailing comma matters.
- Every process is started first, then joined in a separate loop. This allows all workers to run concurrently.
- `if __name__ == "__main__":` is essential, especially on Windows, where multiprocessing uses spawn semantics.
- The parent process does not automatically receive a worker's local variables or return value.

### `03_gil_threading.py`: CPU-bound threads

Two named threads each perform 100 million Python-level increments. The program measures the total elapsed time.

This demonstrates that adding threads is usually not a solution for CPU-bound pure-Python loops under standard CPython. Threads compete for the GIL and also incur context-switching overhead.

The exact timing depends on the Python version, processor, operating system, background load, and power settings. A timing result is evidence for the current machine, not a universal constant.

### `04_gil_multiprocessing.py`: CPU-bound processes

Two processes each perform the same large counting loop. Separate processes can use separate CPU cores, so this can outperform the threaded version when enough CPU cores and memory are available.

Important comparison:

- Threads: shared memory, lower startup cost, GIL limits pure-Python CPU parallelism.
- Processes: isolated memory, higher startup and communication cost, true CPU parallelism.

The process version is not guaranteed to be faster for every workload. Startup time, serialization, CPU count, thermal throttling, and workload size all matter.

### `05_thread_one.py`: overlapping breakfast tasks

`boil_milk()` waits 2 seconds and `toast_bun()` waits 3 seconds. Starting both threads before joining them demonstrates task overlap. The expected completion time is close to 3 seconds rather than 5 seconds.

This is a simple model of I/O-bound or waiting-bound work.

### `06_thread_two.py`: passing arguments to a thread

Both threads call the same `prepare_chai(type_, wait_time)` function with different arguments.

Correct pattern:

```python
thread = threading.Thread(
    target=prepare_chai,
    args=("Masala", 2),
)
```

Do not write `target=prepare_chai("Masala", 2)`, because that calls the function immediately and passes its return value as the target.

### `07_thread_download.py`: concurrent network requests

A thread is created for each URL, and the main thread later joins all of them. Network waiting is a classic use case for threading.

Production improvements:

```python
response = requests.get(url, timeout=10)
response.raise_for_status()
```

The current example should also handle request exceptions and use a `requests.Session` or a thread pool for larger batches. It reports the response size but does not save the downloaded data to disk. The HTTP endpoint may be unavailable or slow, so results and timings can vary.

For many URLs, prefer `concurrent.futures.ThreadPoolExecutor`, which manages a bounded number of worker threads instead of creating an unbounded thread per URL.

### `08_thread_lock.py`: protecting a shared counter

Ten threads increment the same global counter 100,000 times each. The lock protects the read-modify-write sequence:

```python
with lock:
    counter += 1
```

Expected final value:

$$10 \times 100{,}000 = 1{,}000{,}000$$

Why the lock matters: `counter += 1` is logically multiple steps: read the current value, add one, then write the result. Without synchronization, updates can be lost.

`with lock:` is preferred because it releases the lock automatically even if an exception occurs. The function name `increament` is misspelled, but that does not affect execution.

The list comprehensions used only for `start()` and `join()` work, but ordinary `for` loops are clearer because the result list is ignored.

### `09_process_one.py`: CPU work with threads

Despite its filename, this script uses **threads**, not processes. Two threads each sum integers through `10**7`.

It is another CPU-bound GIL demonstration. The local `total` variable belongs to each thread's function call, so the threads do not share that variable. The calculation is performed but its result is not returned or displayed.

For an apples-to-apples comparison, use the same workload in both the threaded and multiprocessing versions. This file uses `10**7`, while `10_process_two.py` uses `10**9`, so their timings cannot be compared directly.

### `10_process_two.py`: CPU work with processes

This script correctly uses two processes and protects process creation with the main guard. It runs a much larger loop, `10**9`, than the previous file.

The variable name `processes` is clear, but the list comprehensions used to call `start()` and `join()` are less readable than explicit loops. The large workload can take a long time and may consume substantial CPU resources.

A better benchmark would:

- use the same iteration count in both versions;
- repeat each measurement several times;
- use `time.perf_counter()`;
- record Python version, processor, and number of CPU cores;
- avoid interpreting one noisy run as a general rule.

### `11_process_queue.py`: sending data from a process

The child process places a message into a `multiprocessing.Queue`, and the parent retrieves it.

```python
queue = Queue()
process = Process(target=prepare_chai, args=(queue,))
process.start()
process.join()
message = queue.get()
```

A queue serializes objects so they can cross the process boundary. The child cannot directly change the parent's ordinary local variables.

For a tiny message this order is fine. For large or numerous messages, joining before draining a queue can risk blocking because the queue's feeder may still need the parent to consume data. A scalable pattern consumes results while workers run or uses `queue.close()` and `queue.join_thread()` when appropriate.

Useful queue methods include `put()`, `get()`, `get_nowait()`, and `empty()`; note that `empty()` is not a reliable synchronization mechanism in concurrent programs.

### `12_process_value.py`: shared integer state across processes

`Value('i', 0)` creates a shared, signed integer value. Four processes increment it 100,000 times each.

Expected final value:

$$4 \times 100{,}000 = 400{,}000$$

The lock obtained from `counter.get_lock()` protects the update:

```python
with counter.get_lock():
    counter.value += 1
```

A `multiprocessing.Value` is different from an ordinary Python variable: it is specifically designed for simple shared state between processes. The operation still needs synchronization because incrementing is a read-modify-write sequence.

For larger or more structured state, consider a `Queue`, `Pipe`, `Manager`, or a dedicated shared-memory design. Prefer message passing when possible because it reduces shared-state complexity.

---

## 4. Threads versus processes

| Concern | Threads | Processes |
|---|---|---|
| Memory | Shared within one process | Separate by default |
| Startup cost | Lower | Higher |
| Communication | Ordinary shared objects, locks, events, queues | Queue, Pipe, Manager, shared memory |
| Best fit | I/O-bound and waiting-heavy work | CPU-bound pure-Python work |
| GIL impact | Limits CPU-bound Python bytecode in CPython | Each process has its own interpreter/GIL |
| Failure isolation | Lower; one process contains all threads | Higher; workers are isolated processes |
| Data sharing risk | Race conditions and deadlocks | Serialization cost and IPC complexity |
| Typical API | `threading.Thread` | `multiprocessing.Process` |

### Decision rule

1. Is the task mostly waiting for network, disk, a database, or another service? Start with threads or asynchronous I/O.
2. Is the task mostly CPU-bound pure Python? Start with processes or a process pool.
3. Does the workload use a native library that releases the GIL? Benchmark threads before assuming processes are better.
4. Is the work tiny? Concurrency overhead may cost more than it saves.
5. Is there shared mutable state? Prefer message passing; otherwise define ownership and synchronization clearly.

---

## 5. Lifecycle patterns to memorize

### Thread lifecycle

```python
import threading

thread = threading.Thread(target=work, args=(value,))
thread.start()
thread.join()
```

A thread can be started only once. If the worker must report a result or exception, use `ThreadPoolExecutor` or communicate through a queue/result object.

### Process lifecycle

```python
from multiprocessing import Process

if __name__ == "__main__":
    process = Process(target=work, args=(value,))
    process.start()
    process.join()
```

Always use the main guard for portable multiprocessing code. On Windows, do not create processes at module import time.

### Multiple workers

```python
workers = [Process(target=work, args=(item,)) for item in items]

for worker in workers:
    worker.start()

for worker in workers:
    worker.join()
```

Starting every worker before joining prevents the first `join()` from unnecessarily delaying the start of later workers.

---

## 6. Synchronization and communication

### Lock

Use a lock when multiple workers access shared mutable state and at least one worker writes to it.

- Keep the critical section small.
- Acquire locks in a consistent order.
- Never hold a lock while doing slow network or file I/O unless required.
- Avoid nested locks when possible.
- Use `with lock:` so release is reliable.

### Queue

A queue is usually the cleanest way to pass work or results between workers.

- Producers call `put()`.
- Consumers call `get()`.
- Values are transferred rather than directly shared.
- Objects generally need to be serializable when crossing process boundaries.

### Value

Use `multiprocessing.Value` for small, simple shared values such as counters or flags. Protect compound updates with its lock.

### Other tools to know

- `threading.Event`: signal one or more threads to stop or continue.
- `threading.RLock`: re-entrant lock for a specific nested-lock design.
- `threading.Semaphore`: limit simultaneous access to a resource.
- `multiprocessing.Pool` and `concurrent.futures.ProcessPoolExecutor`: distribute CPU tasks across a managed process pool.
- `concurrent.futures.ThreadPoolExecutor`: manage a bounded pool of threads.
- `multiprocessing.Pipe`: direct two-way communication between processes.
- `multiprocessing.Manager`: shared proxy objects, convenient but slower than simpler IPC options.

---

## 7. Common mistakes and corrections

### Calling the target instead of passing it

Wrong:

```python
threading.Thread(target=work())
```

Correct:

```python
threading.Thread(target=work)
```

### Forgetting `join()`

Without `join()`, the main thread may print a final message before workers finish, or the program may exit before expected coordination is complete.

### Missing the multiprocessing main guard

Wrong for portable process code:

```python
process = Process(target=work)
process.start()
```

Correct:

```python
if __name__ == "__main__":
    process = Process(target=work)
    process.start()
```

### Assuming the GIL makes shared updates safe

The GIL does not express application-level intent. Protect read-modify-write operations with a lock, or redesign around message passing.

### Comparing unfair benchmarks

Keep the function, input size, environment, and measurement method consistent. A thread benchmark using `10**7` iterations cannot be fairly compared with a process benchmark using `10**9` iterations.

### Creating too many workers

One thread per URL is acceptable for three demonstrations, but large workloads need bounded pools. Too many workers increase memory use, scheduling overhead, connection pressure, and failure complexity.

### Ignoring errors in worker code

Worker exceptions may not be visible in the parent in the same way as ordinary function exceptions. Use futures, queues, exit codes, logging, and explicit result/error handling in production programs.

### No timeout for external I/O

Network calls without a timeout can wait indefinitely. Always define a reasonable timeout and handle `requests.RequestException` or the equivalent library exception.

---

## 8. Improving the examples for production

A robust threaded download worker would conceptually include:

```python
import requests


def download(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return url, len(response.content), None
    except requests.RequestException as error:
        return url, 0, str(error)
```

For a real batch, use `ThreadPoolExecutor(max_workers=...)` and collect each future's result. For CPU work, use `ProcessPoolExecutor` and keep worker functions importable at module scope.

For benchmarks, prefer:

```python
from time import perf_counter

start = perf_counter()
# operation
elapsed = perf_counter() - start
```

`perf_counter()` is intended for measuring short elapsed durations and is preferable to wall-clock time for benchmarks.

---

## 9. Expected results checklist

- `01_threading.py`: order-taking and chai-brewing output interleaves; total time is near the slower workflow.
- `02_multiprocessing.py`: three makers run independently; output order can vary; all are joined before the final message.
- `03_gil_threading.py`: two CPU-bound threads usually do not halve elapsed time under CPython.
- `04_gil_multiprocessing.py`: two processes may use multiple cores, but startup and workload size affect the result.
- `05_thread_one.py`: breakfast is ready in roughly 3 seconds, not 5.
- `06_thread_two.py`: both chai types are prepared concurrently.
- `07_thread_download.py`: requests overlap; network speed and endpoint behavior determine timing.
- `08_thread_lock.py`: final counter should be 1,000,000.
- `09_process_one.py`: CPU-bound work is performed by threads despite the filename.
- `10_process_two.py`: CPU-bound work is performed by two processes; it is not a fair timing pair with file 09 as written.
- `11_process_queue.py`: the parent receives the child message through a queue.
- `12_process_value.py`: final shared counter should be 400,000.

Output ordering is not a correctness guarantee. Scheduling can change the order on every run.

---

## 10. Active-recall questions

1. What is the difference between concurrency and parallelism?
2. Why are threads useful for network requests even when CPython has the GIL?
3. Why does multiprocessing require a main guard on Windows?
4. What does `join()` guarantee, and what does it not guarantee about output order?
5. Why is `counter += 1` unsafe without a lock?
6. Why can ordinary variables not be used to return results from a child process?
7. When would a `Queue` be better than a shared `Value`?
8. Why are files 09 and 10 not a fair benchmark pair as written?
9. What costs are introduced by multiprocessing?
10. Why should a download program use timeouts and exception handling?
11. What is the difference between a lock and a queue?
12. When would a thread pool or process pool be preferable to manually creating workers?

### Short answers

1. Concurrency overlaps progress; parallelism executes at the same time on separate execution resources.
2. A waiting thread releases execution time while another thread can run.
3. Windows starts child processes by importing the module, so unguarded process creation can recursively create workers.
4. `join()` waits for completion; it does not impose a meaningful order on worker print statements.
5. Increment is a read-modify-write sequence and concurrent updates can overwrite one another.
6. A child process has separate memory; use IPC or shared-memory primitives.
7. Use a queue for messages or results; use a value for a small shared scalar that truly needs shared access.
8. They use different worker types and different iteration counts: `10**7` versus `10**9`.
9. Process startup, memory, serialization, and inter-process communication add overhead.
10. External services can fail or hang, and failures should be reported rather than silently blocking.
11. A lock controls access to shared state; a queue transfers messages or work.
12. Pools reuse a bounded number of workers and simplify result and exception handling.

---

## 11. Practice progression

1. Add timestamps and thread/process names to files 01 and 02.
2. Modify file 06 so each worker returns a result through a queue.
3. Remove the lock from file 08, run it repeatedly, and explain any incorrect result.
4. Make files 09 and 10 use the same iteration count and compare threads versus processes with `perf_counter()`.
5. Replace file 07's manual threads with `ThreadPoolExecutor`.
6. Add request timeouts and error reporting to the download example.
7. Build a producer-consumer pipeline with one producer, several workers, and a sentinel value that signals shutdown.
8. Add a shared stop event so all workers can exit early when one task fails.
9. Measure how performance changes when the number of workers is smaller than, equal to, and larger than the CPU core count.
10. Write down which data is shared, who owns it, and how every worker communicates before implementing a concurrent program.

---

## Final revision summary

Use **threads** when tasks spend much of their time waiting. Use **processes** when tasks spend much of their time computing in Python. Use `start()` to begin work, `join()` to wait, locks to protect shared mutable state, and queues to pass messages. Always guard multiprocessing entry points, benchmark equivalent workloads, and treat output order as nondeterministic.
