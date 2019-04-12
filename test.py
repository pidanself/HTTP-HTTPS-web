import IPython
def display():
    # 调用库显示html
    import eel
    eel.init('web')
    web_app_options = {
        'mode': "chrome-app",  # or "chrome"
        'port': 8082,
        'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
    }
    eel.start('index.html', options=web_app_options)

# display()