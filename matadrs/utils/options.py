from types import SimpleNamespace

AVERAGE = SimpleNamespace(method="mat_tools", func="robustmean")
COLOR = SimpleNamespace(colormap="tab20", number=100)
LEGEND = SimpleNamespace(fontsize="small", location="upper right")
PLOT = SimpleNamespace(
    color=COLOR, dpi=300, legend=LEGEND, linestyles=["-", "--", "-.", ":"], size=700
)
OPTIONS = SimpleNamespace(average=AVERAGE, color=COLOR, legend=LEGEND, plot=PLOT)
