import streamlit as st

st.set_page_config(
    page_title="[NU CEE440] - Profiles and fitting",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
 )

r"""
# **Profiles and fitting data**

## Profile canvas

## Principal velocity profile

### The log-law

First, we define the **viscous lenghtscale** $\delta_v$

$$
    \delta_v = \dfrac{\nu}{u^*}
$$

And use this lenghtscale to obtain a dimensionless depth $y^+$

$$
    y^+ = \dfrac{y}{\delta_v}
$$

The **log-law** region of a channel flow 

$$
    \mathsf{for:}
    y^+ > 30 \, \mathsf{and} \, y/\delta = 0.3 \\
    u^+ = \dfrac{1}{\kappa} \ln{y^+} + B
$$

Where $\kappa = 0.41$ is the von Kármán constant and $B = 5.2$ 
is a fitting constant.

## Other velocity profiles

:Notice how water goes up and downwards?:

## Reynolds stresses profiles

### Shear stress $\tau_0$ and shear velocity $u^*$

### Friction factor $f$

## Turbulent kinetic energy profile

## Eddy viscosity profile
"""