## dash tagcloud

![](https://raw.githubusercontent.com/IjzerenHein/react-tag-cloud/master/react-tag-cloud.gif)

### History

**[react-d3-cloud](https://github.com/Yoctol/react-d3-cloud)** This works! **But**, I'm not impressed
with the usability. Maybe word clouds are not the winner I was hoping for.

**[react-tag-cloud] Abandoned** I've struggled to get the same demo results as the pure [react-tag-cloud]. Not sure if its
a basic failing in [react-tag-cloud] or some weird interaction wth the Dash layout. The [react-tag-cloud]
example does not seem to give the same tightly knitted result as the [d3-cloud-demo]. I noticed that
[react-tag-cloud] does not use SVG but lays out using html style properties. Maybe this is the
reason. Anyway I can't see a way forward.


Dash wrapper for [react-tag-cloud]

### TO DO

Words overlap - needs investigating.


### Debugging the python demo `usage.py`

In VSCODE select `2. Debug usage.py` from the launch options and press `F5` to launch the
Flask/Dash development server.

Open [http://localhost:8050](http://localhost:8050)

Set breakpoints as required.

### Debugging the component react.js source

To debug/single-step the JS component code in conjunction with a dash application:

In a terminal window start the dash application:

    python usage.py

Select debugger launch *1: JS Browser* and press F5. The chrome browser
will open and display your application. Enter breakpoints in the source
code eg *./src/lib/components/DashDatatables.react.js* as required.


### Links

* [react-tag-cloud](https://github.com/IjzerenHein/react-tag-cloud)
* [d3-cloud](https://github.com/jasondavies/d3-cloud)
    * [d3-cloud-demo]
    * [stackblitz](https://stackblitz.com/edit/react-tag-cloud-t5x4zt?file=App.js)


[react-tag-cloud]: https://github.com/IjzerenHein/react-tag-cloud
[d3-cloud-demo]: https://www.jasondavies.com/wordcloud/