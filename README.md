## dash-holoniq-wordcloud

![](docs/img/dash-holoniq-wordcloud.png)

This project is [Plotly/Dash] wrapper for for the highly configurable [wordcloud].

### Usage

    pip install dash-holoniq-wordcloud

```
from dash_holoniq_wordcloud import DashWordcloud

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

**DashWordcloud** supports the wordcloud [API].

* Hover-over word highlighting and word tooltips are supported.
* Word *onClick* events are reported to Dash and can be used in Dash callbacks

See the usage example [usage.py](./usage.py).

### Styling

The extensive component [API] allows the cloud layout to be
configured directly from python.

The default word-hover and tooltip styling is embedded in the component. This
can be overriden by adding a custom style definitions to your
projects *assets/* folder. The components default class name
is *wc-canvas*. This can, if needed, be changed by setting the python
DashWordcloud property *className*.

*[default styling](./src/lib/components/css/dash-holoniq-wordcloud.css)*
```
.wc-canvas-hover {
  pointer-events: none;
  position: absolute;
  box-shadow: 0 0 10px 10px rgba(255, 255, 255, 0.5);
  border-radius: 10px;
  cursor: pointer;
}

.wc-canvas-hover-label {
  position: absolute;
  top: 100%;
  left: 0;
  background-color: rgba(255, 255, 255, 0.8);
  color: #333;
  margin-top: 6px;
  padding: 0 0.5em;
  border-radius: 0.5em;
  white-space: nowrap;
}
```

### Debugging the python demo `usage.py`

In VSCODE select `2. Debug usage.py` from the launch options and press `F5` to launch the
Flask/Dash development server.

Open [http://localhost:8070](http://localhost:8070)

Set breakpoints as required.

### Debugging the component react.js source

To debug/single-step the JS component code in conjunction with a dash application:

In a terminal window start the dash application:

    python usage.py

Select debugger launch *1: JS Browser* and press F5. The chrome browser
will open and display your application. Enter breakpoints in the source
code eg *./src/lib/components/DashWordcloud.react.js* as required.

### Build the project

    npm run clean
    npm run build

To create a tarball, first change the release version in package.json, then:

    python setup.py sdist bdist_wheel

The tarball is in *dist/dash_holoniq_wordcloud-<version>.tar.gz*

To install the tarball in a dash project:

    pip install dash_holoniq_wordcloud-<version>.tar.gz

### Publish

See [Create a production build and publish]

    twine upload dist/*

### Links

The following [wordcloud] demos are available:

* [wikipedia demo](https://wordcloud.timdream.org/#wikipedia:Cloud)
* [wordcloud demo for developers](https://wordcloud2-js.timdream.org/#love)

[Plotly/Dash]: https://plotly.com/dash/
[wordcloud]: https://github.com/timdream/wordcloud2.js
[API]: https://github.com/timdream/wordcloud2.js/blob/gh-pages/API.md
[Create a production build and publish]: https://github.com/plotly/