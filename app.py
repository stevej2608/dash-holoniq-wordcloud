import os
import dash


def create_app():
    app = dash.Dash(__name__,
            suppress_callback_exceptions=True,
            # external_scripts=[
            #     {'src': 'https://cdnjs.cloudflare.com/ajax/libs/d3-cloud/1.2.5/d3.layout.cloud.min.js'},
            #     {'src': 'https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.3/d3.min.js'}
            # ]
            )
    app.scripts.config.serve_locally = True
    app.css.config.serve_locally = True
    return app


def serve_app(app, path="", debug=False):

    # When running in a Docker container the internal port
    # is mapped onto a host port. Use the env variables passed
    # in to the container to determin the host URL.

    port = int(os.environ.get("PORT", 8060))
    hostname = os.environ.get("HOST_HOSTNAME", "localhost")
    hostport = os.environ.get("HOST_HOSTPORT", "8050")

    print(f' * Visit http://{hostname}:{hostport}{path}')

    app.run_server(debug=debug, host='0.0.0.0', port=port, threaded=False, dev_tools_serve_dev_bundles=True)
