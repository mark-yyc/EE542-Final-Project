import plotly.graph_objects as go
import pandas as pd
from util.Constant import calorie_data, calorie_graph_image

def calorie_graph():
    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(calorie_data)

    # Convert the 'date' column to datetime type for better plotting
    df['date'] = pd.to_datetime(df['date'])

    # Create a plotly figure
    fig = go.Figure()

    # Add calorie intake line
    fig.add_trace(go.Scatter(x=df['date'], y=df['calorie_intake'], mode='lines+markers', name='Calorie Intake', line=dict(color='blue')))

    # Add calorie consumption line
    fig.add_trace(go.Scatter(x=df['date'], y=df['calorie_consumption'], mode='lines+markers', name='Calorie Consumption', line=dict(color='red')))

    # Update the layout
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Calories',
        xaxis_tickformat='%d/%m',
        xaxis_tickangle=45,
        legend=dict(
            x=0.5,    # Center the legend horizontally
            y=-0.2,   # Position the legend below the plot (negative value places it outside the chart area)
            traceorder='normal',
            orientation='h',  # 'h' for horizontal arrangement
            bgcolor='rgba(255, 255, 255, 0.7)',  # Background color of the legend box
            bordercolor='black',  # Border color of the legend box
            borderwidth=1         # Border width
    ),
    margin=dict(t=50, b=100, l=50, r=50)  # Increase bottom margin to make space for the legend
)

    fig.write_image(calorie_graph_image)
