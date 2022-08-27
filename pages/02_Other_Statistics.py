import pandas as pd
import streamlit as st
import extra_streamlit_components as stx

r"""
# What else needs to be calculated?

## Reynolds decomposition 

The decomposition of the velocity into its temporal mean and their
fluctuations is known as the **Reynolds decomposition**. Notice that 
the mean velocity is constant over time, but it is still a function 
of the position of our measurement.  

$$
    u_i(x,t) = \overline{u_i}(x) + u'_i(x,t)
$$

We can omit the $x$ from the time being. A property of this decomposition 
is that he mean of the fluctuations has to be zero

$$
    \overline{u'_i(t)} = 0
$$

However, the mean of the product between fluctuations is not going to be
zero. Instead, the mean of the possible velocity fluctuation are used 
to calculate the **Reynolds stress** tensor $\tau'_{ij}$

$$
    \tau'_{ij} = \rho \overline{u_i'u_j'}
$$

This means that $\tau'_{ij}$ is a 3x3 tensor and each of its elements is given
by: 

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

Notice that this is a symmetric tensor as $\tau'_{ij} = \tau'_{ji}$, so only six of
the nine elements in the tensor need to be calculated.

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

## RMS and turbulence intensity
"""

