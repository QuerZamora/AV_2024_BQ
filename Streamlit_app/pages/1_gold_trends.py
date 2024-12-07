import streamlit as st
import streamlit.components.v1 as components

# script de Tableau
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

st.markdown("""
    **2008–2011: Aftermath of the Global Financial Crisis:**  
    The 2008 financial crisis caused widespread economic instability and a loss of confidence in financial markets, driving gold prices to record highs as investors sought a reliable store of value. Gold prices remained elevated through 2011, fueled by concerns over sovereign debt crises in Europe and quantitative easing policies by central banks, which raised inflation fears.

    **2013–2015: Taper Tantrum and Economic Recovery:**  
    Gold prices declined significantly during this period as the U.S. Federal Reserve announced plans to taper its quantitative easing program. This led to rising confidence in equity markets and a stronger U.S. dollar, reducing gold's appeal. Economic recovery in developed nations further contributed to declining demand for gold.

    **2016: Brexit and Political Uncertainty:**  
    The U.K.'s decision to leave the European Union (Brexit) triggered a brief surge in gold prices due to heightened uncertainty in global markets. This event highlighted gold's role as a hedge during periods of geopolitical instability.

    **2020: COVID-19 Pandemic:**  
    The onset of the COVID-19 pandemic led to a sharp spike in gold prices, as economic shutdowns and a global recession caused market turmoil. Central banks responded with aggressive monetary easing, further boosting gold's appeal. By mid-2020, gold reached an all-time high, driven by fears of prolonged uncertainty and inflationary pressures.

    **2022: Rising Interest Rates and Strong U.S. Dollar:**  
    In response to surging inflation, the U.S. Federal Reserve and other central banks implemented aggressive interest rate hikes. Higher interest rates reduced gold's attractiveness as a non-yielding asset. Additionally, a strong U.S. dollar made gold more expensive for international buyers, leading to a decline in demand and prices.

    **2022–2024: Ongoing Geopolitical Tensions and Economic Adjustments:**  
    Events like the Russia-Ukraine conflict, fluctuating energy prices, and fears of a global economic slowdown have introduced volatility into gold prices. While geopolitical tensions supported gold as a safe-haven asset, these were counterbalanced by central banks' efforts to stabilize inflation through monetary tightening.
    """)
    
