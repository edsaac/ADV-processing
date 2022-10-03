import streamlit as st

st.set_page_config(
    page_title="ADV data processing",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("References and links")

cols = st.columns([1, 1])

with cols[0]:
    r"""
    **Info:**

    We used [netCDF4](http://unidata.github.io/netcdf4-python/) for parsing the Vectrino `.nc` files. 
    `netcdf4-python` is a Python interface to the netCDF C library.

    Interactive plots were built using [Plotly](https://plotly.com/python/). 
    Static plots were rendered using [Matplotlib](https://matplotlib.org/).

    Data sets manipulation was done using [Pandas](https://pandas.pydata.org/docs/user_guide/index.html#user-guide). 

    [NumPy](https://numpy.org/doc/stable/) was used for array programming and calculation. 
    [SciPy](https://docs.scipy.org/doc/scipy/) is used for signal processing. 

    This site was built using [Streamlit](https://streamlit.io/).

    """

with cols[1]:
    r"""
    > **🔎 References:**
    > - [Nortek Vectrino: The Comprehensive Manual - Velocimeters](https://support.nortekgroup.com/hc/en-us/articles/360029839351-The-Comprehensive-Manual-Velocimeters)

    > - [Whitaker J., et al. (2020)](https://doi.org/10.5281/zenodo.4308773). Unidata/netcdf4-python: version 1.5.5 release (v1.5.5rel2). Zenodo.
    > - [Hunter J. D. (2007)](https://doi.org/10.1109/MCSE.2007.55), "Matplotlib: A 2D Graphics Environment", Computing in Science & Engineering, vol. 9, no. 3, pp. 90-95.
    > - Plotly Technologies Inc. (2015). Plotly. Retrieved from https://plotly.com/python/
    > - [McKinney, W. (2010)](https://doi.org/10.25080/Majora-92bf1922-00a). Data Structures for Statistical Computing in Python. Proceedings of the 9th Python in Science Conference, pp. 56-61.
    > - [Harris, C.R., et al. (2020)](https://doi.org/10.1038/s41586-020-2649-2) Array programming with NumPy. Nature 585, 357–362.
    > - [Virtanen, P. et al. (2020)](https://doi.org/10.1038/s41592-019-0686-2) SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. Nature Methods, 17(3), 261-272.
    > - Streamlit - A faster way to build and share data apps (2022). Retrieved from https://streamlit.io/
    """
