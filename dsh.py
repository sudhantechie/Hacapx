import time 
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from metrics import get_system_metrics

# Initialize metrics lists for Dash
cache_hits_list = []
cache_misses_list = []
cpu_usage_list = []
memory_usage_list = []
disk_usage_list = []
network_sent_list = []
network_recv_list = []
time_list = []

def create_dash_app(port, interval):
    # Set up Dash app
    app = Dash(__name__)

    app.layout = html.Div(children=[
        html.H1(children='Real-Time System Metrics'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=interval * 1000  # in milliseconds
        ),
    ])

    @app.callback(
        Output('live-update-graph', 'figure'),
        [Input('interval-component', 'n_intervals')]
    )
    def update_graph(n):
        # Fetch metrics
        cache_hits, cache_misses, cpu_usage, memory, disk, net_sent, net_recv, \
        disk_read_speed, disk_write_speed, system_uptime, top_processes, battery_info, bus_speed, \
        disk_health, network_bandwidth, load_average = get_system_metrics()

        # Update lists for plotting
        cache_hits_list.append(cache_hits)
        cache_misses_list.append(cache_misses)
        cpu_usage_list.append(cpu_usage)
        memory_usage_list.append(memory)
        disk_usage_list.append(disk)
        network_sent_list.append(net_sent)
        network_recv_list.append(net_recv)
        time_list.append(time.time())

        # Create traces for plotting
        traces = [
            go.Scatter(x=time_list, y=cache_hits_list, mode='lines', name='Cache Hits'),
            go.Scatter(x=time_list, y=cache_misses_list, mode='lines', name='Cache Misses'),
            go.Scatter(x=time_list, y=cpu_usage_list, mode='lines', name='CPU Usage (%)'),
            go.Scatter(x=time_list, y=memory_usage_list, mode='lines', name='Memory Usage (%)'),
            go.Scatter(x=time_list, y=disk_usage_list, mode='lines', name='Disk Usage (%)'),
            go.Scatter(x=time_list, y=network_sent_list, mode='lines', name='Network Sent (Bytes)'),
            go.Scatter(x=time_list, y=network_recv_list, mode='lines', name='Network Received (Bytes)')
        ]

        return {
            'data': traces,
            'layout': go.Layout(title='Real-time System Metrics',
                                xaxis=dict(title='Time'),
                                yaxis=dict(title='Value'))
        }

    return app
