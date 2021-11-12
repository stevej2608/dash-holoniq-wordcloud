# dash-wordcloud

![](https://raw.githubusercontent.com/stevej2608/dash-wordcloud/main/docs/img/dash-wordcloud.png)

This project is [Plotly/Dash] wrapper for for the highly configurable [wordcloud].

### Usage

    pip install dash-wordcloud

```
from dash_wordcloud import DashWordcloud

security_data = [
    ["Equity", 74, "Zillions of equity based funds"],
    ["Bond", 45],
    ["Global", 30],
    ["Sector Equity", 17],
    ["EUR", 15],
    ["Large Cap", 13],
    ["Europe", 11],
]

app.layout = html.Div([
    html.Div([
        DashWordcloud(
            id='wordcloud',
            list=security_data,
            width=300, height=200,
            gridSize=16,
            color='#f0f0c0',
            backgroundColor='#001f00',
            shuffle=False,
            rotateRatio=0.5,
            shrinkToFit=True,
            shape='circle',
            hover=True
            )
        ])
    ])

```
### Features

**DashWordcloud** supports the extensive wordcloud [API].

* Hover-over word highlighting and word tooltips are supported.
* Word *onClick* events are reported to Dash and can be used in Dash callbacks

See the usage example [usage.py](./usage.py).


## Installation

You can install *dash-wordcloud* with `pip`:

```
pip install dash-wordcloud
```

## Documentation

Head over to the [*README*][docs-homepage] for more details.

## Contributing

The source code for *dash-wordcloud* is available
[on GitHub][dwc-repo]. If you find a bug or something is unclear, we encourage
you to raise an issue. We also welcome contributions, to contribute, fork the
repository and open a [pull request][dwc-pulls].


[dash-homepage]: https://dash.plot.ly/
[dwc-repo]: https://github.com/stevej2608/dash-wordcloud
[docs-homepage]: https://github.com/stevej2608/dash-wordcloud/blob/master/README.md
[dwc-pulls]: https://github.com/stevej2608/dash-wordcloud/pulls