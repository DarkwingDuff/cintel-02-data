import plotly.express as px
from shiny.express import input, ui
from shiny.express import output, render, ui
from shinywidgets import render_plotly
import palmerpenguins
from palmerpenguins import load_penguins

penguins_df = palmerpenguins.load_penguins()
print(penguins_df)

data = penguins_df

ui.input_slider("n", "Number of Bins", 0, 50, 20)

height = 350
width = "fit-content"

ui.page_opts(title="Dave's Penguin Data", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")

    @render.data_frame
    def plot3():
        return render.DataTable(
            data, width="auto", height="100%")

    @render.data_frame
    def plot4():
        return render.DataGrid(data)
