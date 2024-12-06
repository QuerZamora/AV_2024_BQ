import streamlit as st
import streamlit.components.v1 as components

# Título de la app


# Código HTML proporcionado (incluso el script de Tableau)
tableau_embed_code = """
<div class='tableauPlaceholder' id='viz1733510408433' style='position: relative'>
    <noscript>
        <a href='#'>
            <img alt='Dashboard 1' src='https://public.tableau.com/static/images/Go/Gold_d1/Dashboard1/1_rss.png' style='border: none' />
        </a>
    </noscript>
    <object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='Gold_d1/Dashboard1' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https://public.tableau.com/static/images/Go/Gold_d1/Dashboard1/1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='es-ES' />
        <param name='filter' value='publish=yes' />
    </object>
</div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1733510408433');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if ( divElement.offsetWidth > 800 ) {
        vizElement.style.width='100%';
        vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
    } else if ( divElement.offsetWidth > 500 ) {
        vizElement.style.width='100%';
        vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
    } else {
        vizElement.style.width='100%';
        vizElement.style.height='1177px';
    }
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""

# Incrustar el código de Tableau dentro de la app de Streamlit
components.html(tableau_embed_code, height=800)
