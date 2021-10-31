from  dash import html
import dash_tagcloud
from app import create_app, serve_app


app = create_app()

# style={
#     'fontFamily': 'sans-serif',
#     'fontSize': 30,
#     'fontWeight': 'bold',
#     'fontStyle': 'italic',
#     'padding': 5,
#     'width': '100%',
#     'height': '100%'
# }

style={
    'fontFamily': 'sans-serif',
    'fontSize': 30,
    'padding': 5
}

app.layout = html.Div([
    html.Div([
        html.Div([
                html.H1('Tag Cloud'),
                dash_tagcloud.DashTagcloud([
                    html.Div("react", style={'fontSize': 50}),
                    html.Div("Red", style={'color': 'red', 'fontSize': 20 }),
                    html.Div("Green", style={'color': 'green', 'fontSize': 30}),
                    html.Div("cloud")
                ], id='input', rotate=60, spiral='archimedean',  style=style)
            ], className='app-inner')

    ], className='app-outer')
])


if __name__ == '__main__':
    serve_app(app)
