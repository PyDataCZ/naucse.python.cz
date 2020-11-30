import pandas as pd
import plotly.express as px
import streamlit as st


def app():
    # vstup 1: výběr datové sady
    data_file_path = st.file_uploader("Data file")
    data = None
    if data_file_path is not None:
        # read data if user uploads a file
        data = pd.read_csv(data_file_path)
        # seek back to position 0 after reading
        data_file_path.seek(0)
    if data is None:
        st.warning("No data loaded")
        return
    # vstup 2: výběr parametrů scatter matrix
    dimensions = st.multiselect("Scatter matrix dimensions", list(data.columns), default=list(data.columns))
    color = st.selectbox("Color", data.columns)
    opacity = st.slider("Opacity", 0.0, 1.0, 0.5)

    # scatter matrix plat
    st.write(px.scatter_matrix(data, dimensions=dimensions, color=color, opacity=opacity))

    # výběr sloupce pro zobrazení rozdělení dat
    interesting_column = st.selectbox("Interesting column", data.columns)
    # výběr funkce pro zobrazení rozdělovací funkce
    dist_plot = st.selectbox("Plot type", [px.box, px.histogram, px.violin])

    st.write(dist_plot(data, x=interesting_column, color=color))


if __name__ == "__main__":
    app()
