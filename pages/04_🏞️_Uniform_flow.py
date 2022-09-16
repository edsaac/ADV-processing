import streamlit as st

st.set_page_config(
    page_title="[NU CEE440] - Uniform flow",
    page_icon="🏞️",
    layout="wide",
    initial_sidebar_state="collapsed"
 )

r"""
# 🏞️ **Uniform flow characterization**

## Channel dimensions
"""

cols = st.columns([3,1,1])

with cols[0]:
    r"""

    The **depth** $y$ of the channel was measured in the lab, whereas the width 
    is $L_w = 0.205 \, \mathrm{m}$ for the flume used. 

    For a rectangular channel, the **cross-sectional** area $A_C$ and the 
    **wetted perimeter** $P_W$ are given by

    $$
        A_C = L_w \cdot y
    $$

    $$
        P_W = 2y + L_w
    $$
    """

    """
    The ratio between these two quantities give the **hydraulic radius** $R_H$

    $$
        R_H = \dfrac{A_C}{P_W}
    $$

    Finally, the friction slope $S_f$ was measured during the lab. 
    """

with cols[1]:
    st.image("./assets/widthchannel.jpg",
        use_column_width=True,
        caption="Channel width")

with cols[2]:
    st.image("./assets/slopemeter.jpg",
        use_column_width=True,
        caption="Measuring the slope of the channel.")


col1, col2 = st.columns(2)

with col1:
    st.warning(
    r"""
    What is the diference between the friction slope $S_f$ and the channel bottom 
    slope $S_0$. Which one did we measure?

    """,icon="🤔")

with col2:
    st.info(
        r"""
        **To do:**

        Calculate $R_H$ and $S_f$.
        """, icon="☑️")

"""
****
## Flow parameters
"""

col1, col2 = st.columns([2,1])

with col1:
    r"""
    The volumetric **flow rate** $Q$ was measured with the flowmeter in the 
    return pipe of the channel. Use these readings to calculate the 
    **bulk velocity** $U$:

    $$
        U = \dfrac{Q}{A_C}
    $$

    The Reynolds number $\mathcal{R}$ for a channel is defined as

    $$
        \mathcal{R} = \dfrac{4 U R_H}{\nu}
    $$

    Where $\nu$ is the kinematic viscosity of water
    """

    st.warning(
    r"""
    Was the flow in the channel *laminar* or *turbulent*? 
    """,icon="🤔")

    st.info(
        r"""
        **To do:**

        Calculate the Reynolds number $\mathcal{R}$.
        """, icon="☑️")


with col2:
    st.image("./assets/flowmeter.jpg",use_column_width=True,
        caption="Volumetric flowmeter.")

r"""
****
## Shear stress

The **shear stress** $\tau_0$ at the bottom of the channel is given by

$$
    \tau_0 = \rho g R_H S_0
$$

Where $\rho$ is the water density and $g$ is the gravitational acceleration. 
The shear velocity $u^*$ is:

$$
    u^* = \sqrt{\dfrac{\tau_0}{\rho}}
$$
"""

r"""
The thickness of the viscous (a.k.a. laminar) sublayer $\delta_v$ can be 
approximated as

$$
    \delta_v = 11.6 \frac{\nu}{u^*}
$$

"""

col1, col2 = st.columns(2)

with col1:
    st.warning(
        r"""
        What are the units of $\tau_0$ and $u^*$?

        What are the units of $\delta_v$?
        """,icon="🤔")

with col2:
    st.info(
        r"""
        **To do:**

        Calculate $\tau_0$, $u^*$ and $\delta_v$.
        """, icon="☑️")


r"""
****

## Friction factor

The Darcy-Weisbach equation for open channel flow is 

$$
    S_f = f \dfrac{1}{4R_H}\dfrac{U^2}{2g}
$$

where $f$ is the friction factor and $S_f$ is the energy line slope, which, for
uniform flow is assumed to be equal to the bottom slope $S_0$
"""

col1, col2 = st.columns(2)

with col1:
    st.warning(
        r"""
        What are the units of $f$?
        """,icon="🤔")

with col2:
    st.info(
        r"""
        **To do:**

        Solve for $f$ to obtain the friction factor.
        """, icon="☑️")

r"""
Semi-empirical relationships exist between the Reynolds number, the friction
factor and the bottom roughness $k_s$, like the [Moody chart](https://upload.wikimedia.org/wikipedia/commons/d/d9/Moody_EN.svg)
and the [Colebrook-White equation](https://en.wikipedia.org/wiki/Darcy_friction_factor_formulae#Colebrook%E2%80%93White_equation) 
for flow in a pipe. For flow in a channel you can use a similar expression [(Osman, 2006)](https://www.elsevier.com/books/open-channel-hydraulics/akan/978-0-7506-6857-6):

$$
    \dfrac{1}{\sqrt{f}} = -2 \log{\left( \dfrac{k_s}{12R_H} + \dfrac{2.5}{\mathcal{R}\sqrt{f}} \right)}
$$

"""

col1, col2 = st.columns(2)

with col1:
    st.warning(
        r"""
        Check that the units on this equation are consistent.
        """,icon="🤔")

    st.warning(
        r"""
        Did we measure the bottom roughness?
        """,icon="🤔")

with col2:
    st.info(
        r"""
        **To do:**

        Solve for $k_s$.
        
        Is the result close to your roughness measurement?
        """, icon="☑️")
