# Visual physics checks

- A rigid upper mechanical-room carrier shares the tower displacement; the sphere moves relative to that carrier. Four cables have a fixed displayed length of 220 local units. A rigging yoke connects the cable ends to the sphere.
- Jointed piston bodies and rods connect the floor plinths to the moving mass; the detail view derives its piston stroke from the same geometry.
- The illustrative linear first-mode model uses two masses, positive stiffness and viscous damping, driven by one sinusoidal wind force. The comparison evaluates the same forcing with and without the auxiliary mass/damper.
- The inertia sequence samples the response in labelled slow motion. Direction tests cover 80 samples: wind left, tower velocity left, relative sphere position and relative velocity right.
- Damper power is c × relative_velocity², which is nonnegative. The heat graphic shows a dissipation rate rather than claiming a decreasing cumulative energy.
- The early building/bracing motions are qualitatively authored. The simplified model does not represent a site-specific structural or seismic analysis. There is no claim that motion is eliminated or that TMDs guarantee earthquake safety.

Numeric coefficient/residual and direction test evidence is retained in the production workspace at manifests/physics.json and qa/physics-direction.json. Rig/cable constraints were checked while rendering the complete film; actual encoded keyframes were inspected.
