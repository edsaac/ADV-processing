from pprint import isrecursive
import pandas as pd
import streamlit as st
import extra_streamlit_components as stx

st.set_page_config(
    page_title="[NU CEE440] Lab 2 - Turbulence analysis",
    page_icon="🌀",
    layout="wide",
    initial_sidebar_state="auto"
)


r"""
# 🌀 **Reynolds decomposition**

The separation of the velocity into its temporal mean $\overline{u_i}$ and their
fluctuations u'_i is known as the **Reynolds decomposition**. The mean velocity 
is constant over time, but it is still a function of the position of our measurement $x$.  

$$
    u_i(x,t) = \overline{u_i}(x) + u'_i(x,t)
$$

Where the subindex $i$ represents either the $x$,$y$ or $z$ direction of the
velocity vector field. A property of the Reynolds decomposition is that 
the mean of the velocity fluctuations must be zero:

$$
    \overline{u'_i(x,t)} = 0
$$
"""

st.info(
    r"""
    **To do:**

    Check that the mean of the fluctuations is actually zero.
    """, icon="☑️")

r"""
In contrast, the mean of the product between fluctuations $\overline{u_i'u_j'}$ 
is not zero. Instead, the mean of the possible velocity fluctuation is used 
to calculate the **Reynolds stress** tensor $\tau'_{ij}$

$$
    \tau'_{ij} = -\rho \overline{u_i'u_j'}
$$

This means that $\tau'_{ij}$ is a 3x3 tensor defined as: 

$$
    \tau'_{ij} 
    =
    - \rho
    \begin{pmatrix}
        \tau'_{xx} & \tau'_{xy} & \tau'_{xz} \\
        \tau'_{yx} & \tau'_{yy} & \tau'_{yz} \\
        \tau'_{zx} & \tau'_{zy} & \tau'_{zz} \\
    \end{pmatrix} 
$$

Notice that this is a symmetric tensor (i.e., $\tau'_{ij} = \tau'_{ji}$), so 
only six of the nine elements in the tensor need to be calculated.

$$
    \tau'_{ij} 
    =
    - \rho

    \begin{pmatrix}
        \overline{u'u'} & \overline{u'v'} & \overline{u'w'}  \\
        \vdots          & \overline{v'v'} & \overline{v'w'}  \\
        \cdots          & \vdots          & \overline{w'w'}  \\
    \end{pmatrix}
$$
"""
st.warning(
    r"""
    The terms in the diagonal of $\tau'_{ij}$ are always positive.
    
    Can you show why?
    """,icon="🤔")

st.info(
    r"""
    **To do:**

    Calculate the six components of the Reynolds stress $\tau'_{ij}$
    """, icon="☑️")

r"""
*****

## Turbulent kinetic energy 

The turbulent kinetic energy $k$ is defined as half the trace of the Reynolds
stress tensor. The trace of a tensor is just the sum of the elements in the 
diagonal.

$$
    k = \tfrac{1}{2} \mathrm{tr}(\tau'_{ij}) 
      = \tfrac{1}{2} \left( \tau'_{xx} + \tau'_{yy} + \tau'_{zz} \right)
$$
"""

st.warning(
    r"""
    What are the units of $k$?

    """,icon="🤔")


st.info(
    r"""
    **To do:**

    Calculate the turbulent kinetic energy $k$
    """, icon="☑️")


r"""

****

## Summary

At this point you have measured and calculated the following quantities 
for a **single position** $x$.

- $u(t), v(t), w(t)$
- $\overline{u}, \overline{v}, \overline{w}$
- $u'(t), v'(t), w'(t)$
- $\tau'_{xx},\tau'_{yy},\tau'_{zz},\tau'_{xy},\tau'_{xz},\tau'_{yz}$
- $k$

You will have to repeat these same calculations for all the elevations z 
at which we made velocity measurement in the flume. 
"""


