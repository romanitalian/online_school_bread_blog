def display_attr(obj, attr: str):
    get_display = f'get_{attr}_display'
    if hasattr(obj, get_display):
        return getattr(obj, get_display)()

    return getattr(obj, attr)
