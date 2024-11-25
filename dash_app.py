from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

def create_dash_app(server):
    # Crear una app Dash usando Flask como servidor
    dash_app = Dash(
        server=server,
        name="DashApp",
        url_base_pathname="/dash/",
    )

    # Crear un DataFrame de ejemplo
    df = pd.DataFrame({
        "Categoría": ["A", "B", "C", "D"],
        "Valores": [10, 15, 7, 20],
    })

    # Crear el gráfico con Plotly Express
    fig = px.bar(df, x="Categoría", y="Valores", title="Reporte Básico")

    # Configurar el layout de Dash
    dash_app.layout = html.Div([
        html.H1("Reporte Generado con Dash"),
        dcc.Graph(figure=fig)
    ])

    return dash_app
