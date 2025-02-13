import functools

def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Iniciando {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finalizando {func.__name__}")
        return result
    return wrapper
