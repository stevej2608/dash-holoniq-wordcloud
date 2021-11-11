from  dash import html
from dash.dependencies import Input, Output
from dash_tagcloud import DashTagcloud

from app import create_app, serve_app

app = create_app()

security_data = [
    ["Equity", 74, "Zillions of equity based funds"],
    ["Bond", 45],
    ["Global", 30],
    ["Sector Equity", 17],
    ["EUR", 15],
    ["Large Cap", 13],
    ["Europe", 11],
    ["GBP", 11],
    ["USD", 10],
    ["Hedged", 10],
    ["Commodities", 9],
    ["Corporate", 9],
    ["Mid Cap", 9],
    ["Other", 8],
    ["Asia", 7],
    ["Inflation Linked", 7],
    ["Emerging Markets", 6],
    ["US", 5],
    ["UK", 5],
    ["High Yield", 5],
    ["Small Cap", 5],
    ["Property", 5],
    ["Indirect", 5],
    ["Short Term", 5],
    ["Leveraged/Inverse", 4],
    ["Trading", 4],
    ["Government", 4],
    ["Eurozone", 4],
    ["Value", 4],
    ["Income", 4],
    ["ex Japan", 4],
    ["Flex Cap", 4],
    ["Small", 4],
    ["Diversified", 4],
    ["Alt", 4],
    ["Allocation", 4],
    ["Blend", 3],
    ["Energy", 3],
    ["Pacific", 3],
    ["Growth", 3],
    ["Africa", 3],
    ["Japan", 2],
    ["Precious Metals", 2],
    ["Services", 2],
    ["China", 2],
    ["Industrial", 2],
    ["Broad", 2],
    ["Local Currency", 2],
    ["America", 2],
    ["Germany", 2],
    ["Emerging", 2],
    ["Islamic", 2],
    ["Agriculture", 2],
    ["Moderate", 2],
    ["Moderately", 2],
    ["Technology", 1],
    ["Broad Basket", 1],
    ["Consumer Goods", 1],
    ["Financial", 1],
    ["Materials", 1],
    ["Healthcare", 1],
    ["A Shares", 1],
    ["India", 1],
    ["Korea", 1],
    ["Brazil", 1],
    ["Metals", 1],
    ["Russia", 1],
    ["Communications", 1],
    ["Utilities", 1],
    ["ex UK", 1],
    ["Latin", 1],
    ["Ecology", 1],
    ["Canada", 1],
    ["Money Market", 1],
    ["Biotechnology", 1],
    ["Taiwan", 1],
    ["Fixed", 1],
    ["Grains", 1],
    ["Ultra", 1],
    ["Natural Resources", 1],
    ["New Zealand", 1],
    ["Australia", 1],
    ["Water", 1],
    ["Turkey", 1],
    ["Softs", 1],
    ["RMB", 1],
    ["Onshore", 1],
    ["Infrastructure", 1],
    ["South", 1],
    ["Namibia", 1],
    ["Systematic Futures", 1],
    ["ex Russia", 1],
    ["Indonesia", 1],
    ["Alternative", 1],
    ["Relative", 1],
    ["Arbitrage", 1],
    ["Livestock", 1],
    ["Long Term", 1],
    ["Italy", 1],
    ["Not Categorised", 1],
    ["North", 1],
    ["Private", 1],
    ["Currency", 1],
    ["BRIC", 1],
    ["Convertible", 1],
    ["France", 1],
    ["Biased", 1],
    ["Frontier Markets", 1],
    ["Israel", 1],
    ["Large/", 1],
    ["Nordic", 1],
    ["Poland", 1],
    ["Switzerland", 1],
    ["Thailand", 1],
    ["Vietnam", 1],
    ["Middle East", 1],
    ["Flexible", 1],
    ["Subordinated", 1],
    ["Adventurous", 1],
    ["Cautious", 1],
    ["Netherlands", 1],
    ["Spain", 1],
    ["Sweden", 1],
]


def normalise(lst, vmax=50, vmin=16):
    lmax = max(lst, key=lambda x: x[1])[1]
    lmin = min(lst, key=lambda x: x[1])[1]
    vrange = vmax-vmin
    lrange = lmax-lmin
    for entry in lst:
        entry[1] = int(((entry[1] - lmin) / lrange) * vrange + vmin)
    return lst

app.layout = html.Div([
    html.Div([
        DashTagcloud(
            id='cloud',
            list=normalise(security_data),
            width=300, height=800,
            gridSize=16,
            # weightFactor=2,
            # origin=[90, 0],
            # fontFamily='Sans, serif',
            color='#f0f0c0',
            backgroundColor='#001f00',
            shuffle=False,
            rotateRatio=0.5,
            shrinkToFit=True,
            shape='circle',
            hover=True
            )
        ]),
        html.H2("", id="report")
    ])

@app.callback(
    Output(component_id='report', component_property='children'),
    Input(component_id='cloud', component_property='click')
)
def update_output_div(item):
    return 'Output: {}'.format(item)

if __name__ == '__main__':
    serve_app(app, debug=True)
