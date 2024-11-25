def ensure_hdpi():
    import platform
    import cytypes

    if platform.system() == "Windows":
        import ctypes.windll.shcore.SetProcessDpiAwareness(2)