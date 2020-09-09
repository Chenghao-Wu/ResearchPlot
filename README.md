# ResearchPlot

## Overview

ResearchPlot a python package based on mpltex of liuyxpp for making publication quality figures using matplotlib. The original mpltex package is very convenient for students who make scientific plots with matplotlib. However, it only has one colormap and the settings, e.g. label space, markeredge..., are limited. In this package, I added several different colormaps and made it flexible for customizing the figure settings.

## Installing
```bash
$ pip install ResearchPlot
```

## Usage
Script ro run PMDAT must include three parts: 
   1. System Definition
   2. Object Selection 
   3. Analysis Methods

### Import Package
```python
import ResearchPlot

@ResearchPlot.aps
def plot_example():
    # plot images by matplotlib ...

    # Save the image. Give a file name with or without an extension (default: png).
    fig.save_fig('/path/to/save/fig')

# Then use plot_example in a normal way.
plot_example()
```


