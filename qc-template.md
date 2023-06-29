---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.5
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python
import sys
import importlib

import utils
import tszip
import tskit

importlib.reload(utils)

ts = tskit.load("data/hgdp_tgp_sgdp_high_cov_ancients_chr20_q.dated.trees")
#ts = tszip.decompress("data/hgdp_tgp_sgdp_chr2_q.dated.trees.tsz")
tinfo = utils.TreeInfo(ts, 6)
tinfo
```

```python
tinfo.plot_polytomy_fractions(window_size=500_000, overlap=0)
```

```python
tinfo.plot_mutations_per_site()
```

```python
tinfo.plot_mutations_per_site_along_seq(zoom_start=None, zoom_end=None)
```

```python
tinfo.plot_mutations_per_node(show_counts=True, max_num_muts=10)
```

```python
tinfo.plot_tree_spans(log_transform=True, region_end=200_000_000, region_start=190_000_000, show_counts=True)
```

```python
tinfo.plot_mean_node_arity(show_counts=True)
```

```python
import holoviews as hv
import pandas as pd
hv.extension('bokeh')
```

```python
def mutations_data(ts):
    data = {
        "position": ts.sites_position[ts.mutations_site].astype(int),
        "node": ts.mutations_node,
        "time": ts.nodes_time[ts.mutations_node], #ts.mutations_time,
    }
    return pd.DataFrame(data)

df = mutations_data(ts)
df
```

```python
df.groupby("position").
```

```python
ds = hv.Dataset(df)
ds
```

```python
ds.data
```

```python
ds.aggregate("position", function="count").data
```

```python
ds.hist(dimension="node", adjoin=False)
```

```python
df.groupby("position").count()
```

```python
hv.Histogram(tinfo.sites_num_mutations)
```

```python
tinfo.sites_num_mutations
```

```python
import numpy as np
count, bins = np.histogram(tinfo.sites_num_mutations, bins=range(29))
hv.Histogram((count, bins))
```

```python
import matplotlib.pyplot as plt
plt.hist(tinfo.sites_num_mutations, bins=range(29))
```
