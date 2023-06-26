import numpy as np
import panel as pn
import holoviews as hv
import pandas as pd

# import hvplot.pandas
# from bokeh.sampledata.autompg import autompg
import tszip
import tskit
import utils

from holoviews.operation.datashader import rasterize, datashade


# path = "/home/jk/work/github/sc2ts-paper/data/upgma-mds-1000-md-30-mm-3-2022-06-30-recinfo2-gisaid-il.ts.tsz"
# ts = tszip.decompress(path)
path = "/home/jk/work/github/sc2ts/results/full-md-30-mm-3-2021-04-13.ts"
ts = tskit.load(path)
ti = utils.TreeInfo(ts, 1)


def page1():
    return pn.pane.HTML(ts)
    # hv_layout


def page2():
    site_info = {"position": ts.sites_position, "num_mutations": ti.sites_num_mutations}
    df = pd.DataFrame(site_info)
    scatter = hv.Scatter(df)
    return rasterize(scatter).opts(width=800,  colorbar=True, tools=["hover"])


pn.extension(sizing_mode="stretch_width")

pages = {"Page 1": page1, "Page 2": page2}


def show(page):
    return pages[page]()


starting_page = pn.state.session_args.get("page", [b"Page 1"])[0].decode()
page = pn.widgets.RadioButtonGroup(
    value=starting_page,
    options=list(pages.keys()),
    name="Page",
    sizing_mode="fixed",
    button_type="success",
)
ishow = pn.bind(show, page=page)
pn.state.location.sync(page, {"value": "page"})

ACCENT_COLOR = "#0072B5"
DEFAULT_PARAMS = {
    "site": "Panel Multi Page App",
    "accent_base_color": ACCENT_COLOR,
    "header_background": ACCENT_COLOR,
}
pn.template.FastListTemplate(
    title="As Single Page App",
    sidebar=[page],
    main=[ishow],
    **DEFAULT_PARAMS,
).servable()
