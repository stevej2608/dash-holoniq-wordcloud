from  dash import html
import dash_tagcloud
from app import create_app, serve_app

# This example is a Dash/Python clone of:
#
# https://github.com/IjzerenHein/react-tag-cloud/blob/master/examples/tagCloud/src/App.js
#
# See also the css in assets/style.css
#
#
# https://github.com/IjzerenHein/react-tag-cloud
# https://www.jasondavies.com/wordcloud/


app = create_app()

# Style applied to all the DashTagcloud component

style={
    'fontFamily': 'sans-serif',
    'fontSize': 30,
    'padding': 5,
    'color': {'hue': 'blue'}, # https://github.com/davidmerfield/randomColor
    'width': '100%',
    'height': '100%'
}

# Styles applied to specific words

class styles:

    large =  {
        'fontSize': 60,
        'fontWeight': 'bold'
    }

    small = {
        'opacity': 0.7,
        'fontSize': 16
    }

# Container for cloud words the have a hover capability

def CloudItem(text):
    return html.Div([
        html.Div(text),
        html.Div(html.Div('HOVERED!', className="tag-item-tooltip"))
    ],className="tag-item-wrapper")


app.layout = html.Div([
    html.Div([
        html.Div([

            html.H1('Dash Tag Cloud'),

            dash_tagcloud.DashTagcloud([
                html.Div(
                "Futurama",
                style={
                    'fontFamily': 'serif',
                    'fontSize': 40,
                    'fontStyle': 'italic',
                    'fontWeight': 'bold',
                    'color': 'red'}
                ),
                CloudItem(text="Custom item, Hover me!"),
                CloudItem(text="Custom item 2, Hover me!"),
                html.Div('Transformers', style=styles.large),
                html.Div('Simpsons', style=styles.large),
                html.Div('Dragon Ball', style=styles.large),
                html.Div('Rick & Morty', style=styles.large),
                html.Div('He man', style={'fontFamily': 'courier'}),
                html.Div('World trigger', style={'fontSize': 30}),
                html.Div('Avengers', style={'fontStyle': 'italic'}),
                html.Div('Family Guy', style={'fontWeight': 200}),
                html.Div('American Dad', style={'color': 'green'}),
                html.Div([
                    html.Div('Hover Me Please!'),
                    html.Div('HOVERED!', className="tag-item-tooltip"),
                    ], className="tag-item-wrapper"),
                html.Div('Gobots'),
                html.Div('Thundercats'),
                html.Div('M.A.S.K.'),
                html.Div('GI Joe'),
                html.Div('Inspector Gadget'),
                html.Div('Bugs Bunny'),
                html.Div('Tom & Jerry'),
                html.Div('Cowboy Bebop'),
                html.Div('Evangelion'),
                html.Div('Bleach'),
                html.Div('GITS'),
                html.Div('Pokemon'),
                html.Div('She Ra'),
                html.Div('Fullmetal Alchemist'),
                html.Div('Gundam'),
                html.Div('Uni Taisen'),
                html.Div('Pinky and the Brain'),
                html.Div('Bobs Burgers'),
                html.Div('Dino Riders', style=styles.small),
                html.Div('Silverhawks', style=styles.small),
                html.Div('Bravestar', style=styles.small),
                html.Div('Starcom', style=styles.small),
                html.Div('Cops',style=styles.small),
                html.Div('Alfred J. Kwak', style=styles.small),
                html.Div('Dr Snuggles',style=styles.small),
                ], id='input', className='tag-cloud', spiral='archimedean', style=style)
            ], className='app-inner')
    ], className='app-outer')
])


if __name__ == '__main__':
    serve_app(app)
