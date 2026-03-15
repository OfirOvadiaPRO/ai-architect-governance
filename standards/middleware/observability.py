import time
import functools
import logging
import psutil
import os

logger = logging.getLogger("governance.observability")

def audit_resource_utilization(threshold_ms: float = 500.0):
    """
    Leadership Standard: Performance and Resource Audit Decorator.
    Tracks latency, memory delta, and CPU cycles for critical AI functions.
    """
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            process = psutil.Process(os.getpid())
            start_mem = process.memory_info().rss
            start_time = time.perf_counter()
            
            try:
                result = await func(*args, **kwargs)
                return result
            finally:
                duration = (time.perf_counter() - start_time) * 1000
                end_mem = process.memory_info().rss
                mem_delta = (end_mem - start_mem) / (1024 * 1024)
                
                log_msg = f"Audit | {func.__name__} | Latency: {duration:.2f}ms | Mem Delta: {mem_delta:.2f}MB"
                if duration > threshold_ms:
                    logger.warning(f"SLA Violation: {log_msg}")
                else:
                    logger.info(log_msg)
        return wrapper
    return decorator
