import eel


name = "eelgraph"


def plot(chart, *args, options={}, title="electrograph"):
    # Import web files
    eel.init('ui')
    # Send initial chart data to eel
    eel.init_chart(title, chart.tojson(), options)
    # Start eel server
    eel.start('chart.html', size=(640, 480), block=False)


def sleep(sec):
    eel.sleep(sec)


def update(chart):
    eel.update_chart(chart.tojson())
