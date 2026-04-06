To use it in any MDX post, add these two lines:
mdximport HierarchyOfControls from '../../components/HierarchyOfControls.astro'

<HierarchyOfControls />

-----------------
The component is fully self-contained — no props, no external dependencies. The click-to-expand behavior uses astro:page-load so it works correctly with Astro's view transitions and GSAP page wipes. All styles are prefixed with hoc- to prevent any collision with your existing global CSS.
This is also a reusable reference component — you can drop it into the LOTO post, the PPE post, the arc flash post, or any content where the hierarchy is relevant context.