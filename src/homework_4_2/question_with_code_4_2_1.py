def foo(value):
    def bar():
        return str(bar.value)

    def greet():
        return f"Hello, {greet.value} from {greet.__name__} func"

    if isinstance(value, str):
        greet.value = value
        return greet

    bar.value = value
    return bar


foo("python")()

# ответ - Hello, python from greet func, но у меня просто пустоту выдает
