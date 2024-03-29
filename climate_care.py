import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import time

st.set_page_config(page_title="ClimateCare", page_icon="###", layout="wide")

def loadLottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottieEarth = loadLottie("https://lottie.host/bd8b3239-3835-40f2-bec2-8fe9a5d6b275/lIJEEXEpZR.json")


with st.sidebar:
    selected = option_menu(
        menu_title = "Explore",
        options = ["Home","Climate Change Facts", "Volunteer Opportunities", "Donate"],
)

if selected == "Home":
    with st.container():
        st.subheader("Hi, :wave:")
        col1,col2 = st.columns(2)
        with col1:
            with st.container():
                st.title("Welcome to ClimateCare :herb:")
                st.write("At ClimateCare, we provide you with the resources to volunteer, learn, and advocate for climate change in your community. Climate change is a very convoluted topic that involves a great deal of nuance and research. It's difficult to understand its scale without reading scientific journals or papers. To make the topic of climate change approachable, we've made a website that contains everything from facts to opportunities for change. Together, we can combat climate change!")
        with col2:
            st_lottie(lottieEarth, height = 300, key = "Earth")
    with st.container():
        st.header("About Us")
        st.write("We are two passionate creators based in Philadelphia, PA. As active students at Temple University, we wanted to provide locals with an approachable one-stop-shop for changing the world. We know how hard it is to get valid information that is both truthful and understandable. As a Philadelphia community, we can achieve great things when we work together.")
        st.write("Fun fact: Temple University has the second largest green roof in Pennsylvania!")
    with st.container():
        st.markdown("---")
        st.header("We want to know what you're thinking :thought_balloon:")
        st.write("Now that you've explored our website, tell us how you feel!")
        col1,col2,col3,col4,col5 = st.columns(5)
        with col1:
            sadge = st.button(":sob:")
            if sadge:
                thinking = st.text_input('Why do you feel this way?','')
                st.write("Thank you for your input!")
        with col2:
            sad = st.button(":slightly_frowning_face:")
            if sad:
                thoughts = st.text_input('Why do you feel this way?', '')
                st.write("Thank you for your input!")
        with col3:
            med = st.button(":no_mouth:")
            if med:
                waow = st.text_input('Why do you feel this way?', '')
                if waow == str(waow):
                    st.write("Thank you for your input!")
        with col4:
            smile = st.button(":slightly_smiling_face:")
            if smile:
                thinking = st.text_input('Why do you feel this way?','')
                if thinking == str(thinking):
                    st.write("Thank you for your input!")
        with col5:
            happy = st.button(":smiley:")
            if happy:
                thinking = st.text_input('Why do you feel this way?','')
                st.write("Thank you for your input!")
    with st.container():
        st.markdown("---")
        st.subheader("Want to explore more? Check these out.")
        st.subheader("The IUCN Red List of Threatened Species: International Union for Conservation of Nature and Natural Resources")
        st.write("The IUCN Red List is a comprehensive report of the conservation status of billions of fauna and flora. The IUCN Red List indicates the state of the Earth's biodiversity. Click the Logo to learn more.")
        st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/IUCN_Red_List.svg/800px-IUCN_Red_List.svg.png)](https://www.iucnredlist.org/)")
        st.subheader("IPBES: Global Assessment Report on Biodiversity and Ecosystem Services")
        st.write("The IPBES is a report that assess the Earth's biodiversity and ecosystem services on a global level. The IPBES is commissioned by the United Nations to provide this report. Read more below.")
        st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Emblem_of_the_United_Nations.svg/240px-Emblem_of_the_United_Nations.svg.png)](https://ipbes.net/global-assessment)")


#ok
if selected == "Climate Change Facts":
    st.title("There's lots to learn about climate change :leaves:")
    st.write("When people think about climate change, they wonder about how they can make a change in the world if they are just one person. The truth is, it's not just one person. It's thousands of scientists, advocates, doctors, and enginners working together to solve a global issue. We're moving in the right direction, but we need your help to move faster.")
    st.subheader("We just need one more person, just like you!")
    st.markdown("---")
    st.title("Q&A: The Climate Change Factsheet :earth_americas:")

    intro = st.button("What is climate change?")
    if intro:
        st.write('According to the United Nations, climate change is the long-term shift in global temperatures and weather patterns.')
    
    causes = st.button("What causes climate change?")
    if causes:
        st.write("Up until the 1700s, temperatures and weather patterns have been relatively stable. However, with the onset of human industrialization and the massive exploitation of the planet, scientific sources like the American Chemical Society (ACS), American Medical Association (AMA), and the United Nations (UN), has proven that humans are the number one cause of climate change.")
        url = "https://www.acs.org/content/acs/en/policy/publicpolicies/sustainability/globalclimatechange.html"
        st.write("To read the ACS Climate Change Report (2019-2020), click the following link. (%s)" % url)
    
    how = st.button("How do humans cause climate change?")
    if how:
        st.write("Well, it's really about affecting natural cycles. Human exploitation and development means that we modify natural cycles to fit our needs. For example, burning fossil fuels for energy has increased the amount of carbon in the atmosphere. This directly impacting the carbon cycle, which uses cellular respiration and biological degradation to recycle carbon in an ecosystem.")
        st.write("Excess carbon dioxide in the atmosphere means that heat is trapped in the atmosphere, leading to global increases in temperature.")
        st.write("Click on the image to learn more about how greenhouse gas emissions affect temperature.")
        st.markdown("[![Foo](https://www.climate.gov/sites/default/files/styles/full_width_620_original_image/public/2021-07/projected_emissions_temperature_CSSP_lrg_1.png?itok=2Mbmdip7)](https://www.climate.gov/news-features/understanding-climate/climate-change-global-temperature)")

    goingon = st.button("What about melting glaciers? What does that have to do with anything?")
    if goingon:
        st.write("Glaciers hold ~10% of Earth's water. When the glaciers melt due to increases in temperature, sea levels and currents are affected. When sea levels rise, there's an increase in coastal erosion. Man-made structures near the coast are more prone to flooding and damage by natural disasters, such as hurricanes or tsunamis.")
        st.write("The oceans are very important factors of weather. When glaciers melt, ocean currents are directly imacted. Water circulation affects precipitation patterns and wind patterns. Normally, in the Atlantic ocean, warm air from the equator is pushed upwards to North America and Western Europe while cold air from the north is pushed downwards towards South America and Africa. This phenomenon is called Atmospheric circulation. Now that currents and tides have changed, we see less warm air moving up north and less cold air moving down south. This causes longer seasons and more extreme weather patterns, like storms.")
        st.write("Click the image to learn more about air circulation and ocean currents.")
        st.markdown("[![Foo](https://scied.ucar.edu/sites/default/files/media/images/atm_circulation_0.jpg)](https://scied.ucar.edu/learning-zone/how-weather-works/global-air-atmospheric-circulation)")

    effects = st.button("What are some effects we are seeing now?")
    if effects:
        st.write('The effects of climate change are becoming more and more apparent. If we simply look around us we can notice some of its impact—an example including the weather in Philadelphia being this warm in late November. As well as extreme flooding that recently occurred in Pakistan.')

    increases = st.button("How much has our global temperature increaed by?")
    if increases:
        st.write("According to Climate.gov, the global temperature has increased by 1 ºC since the 1880s. However, the rate of warming is now twice of that, with temperatures increasing at a record high since 1881.")
        st.write("Click on the image to read the June 2022 report from Climate.gov.")
        st.markdown("[![Foo](https://scied.ucar.edu/sites/default/files/media/images/atm_circulation_0.jpg)](https://www.climate.gov/sites/default/files/styles/full_width_620_original_image/public/2022-06/ClimateDashboard-global-surface-temperature-graph-20220624-1400px.jpg?itok=L92HCm6n)")
 

if selected == "Volunteer Opportunities":
    st.title("By volunteering, you can change the world.")
    st.write("Small changes in your community can make big differences in the world. Introducing a community herb garden or promoting sustainability in your household are great places to start! We've provided links for volunteering opportunities in Philadelphia, PA.")
    st.markdown("---")
    st.title("Volunteer Opportunities in Philadelphia, PA :round_pushpin:")
    st.subheader(":dizzy: Penn Environment")
    st.write("This organization in Philly seeks to not only better the environment through the help of their volunteers, but also fights to make better policies that help the planet.")
    st.write("[Learn more about Penn Environment](https://environmentamerica.org/pennsylvania/)")
    
    st.subheader(":dizzy: Philadelphia Orchard Project")
    st.write("This organization plants different fruits and other edible plants so that they can be more assessable to schools and neighborhoods in Philly.")
    st.write("[Learn more about the Philadelphia Orchard Project](https://www.phillyorchards.org/)")

    st.subheader(":dizzy: Pennsylvania Horticutural Society")
    st.write("The Pennsylvania Horticultural Society (PHS) promoted green gardening and actively creates green spaces around Pennsylvania. The PHS sponsors the Philadelphia Flower Show every year, which showcases floral diversity. Volunteering with PHS means promoting sustainability through gardening.")
    st.write("[Learn more about the Philadelphia Orchard Project](https://phsonline.org/)")

    st.subheader(":dizzy: The ACE Program at PennFuture")
    st.write("PennFuture's Advocates for Conservation and the Environment (ACE) program encourages local advocates to unite and inform state and federal legislators, directly influencing environmental legislation.")
    st.write("[Learn more about the ACE Program](https://www.pennfuture.org/join-the-ace-program)")

    st.subheader(":dizzy: The Philly Spring Clean-Up")
    st.write("The Philadelphia Spring Clean-Up is a single-day event where over 200,000 volunteers come out to remove trash and tires from the city streets at thousands of sites. ")
    st.write("[Learn more about the Philly Spring Clean-Up](https://www.phila.gov/programs/philly-spring-cleanup/)")

    st.subheader(":dizzy: Zero Waste Initiatives by the City of Philadelphia")
    st.write("Philadelphia's Zero Waste Initiatives serve to reduce food waste by Philadelphia residents and restaurants. Food is donated to pantries and those who need it most.")
    st.write("[Learn more about the Philadelphia Zero-Waste Initiatives](https://www.phila.gov/programs/zero-waste-initiatives/)")

    st.subheader(":dizzy: The Sierra Club: The Southeastern Pennsylvania Group")
    st.write("The Pennsylvania Chapter of the Sierra Club is focused on combatting environmental issues that face the greater Philadelphia Area.")
    st.write("[Learn more about the Sierra Club](https://www.sierraclub.org/pennsylvania/southeastern)")
        
if selected == "Donate":
    if selected == "Donate":
        st.title("To help the cause, Donate!")
        st.write("If time is a conflict but you still want to help, donating is a great option. It will allow you to become more educted and bring light to the issue by funding it.")
        d1 = st.button("Clean Air Task Force")
        if d1:
            st.write("According to their website, they aim make better policies so that there will be more zero-emission systems. They undertand that this can be costly so part of their mission is to acheive their goals sustianablly.")
            url = 'https://donate.catf.us/page/46672/donate/1?ea.tracking.id=GT_main'
            st.write("To donate to Clean Air Task Force, click the following link. (%s)" % url)
            
        d2 = st.button("The Union of Concerned Scientists")
        if d2:
            st.write("They are a group of scientists as well as students who aim to solve issues around climate change. they do this by conducting various research and studies.")
            url = 'https://secure.ucsusa.org/JuXeEefnxEqkc7b6uwrzeg2?MS=topnav&_gl=1*3lznz3*_ga*NzM1MTE1MDEuMTY2OTM5MjYzNg..*_ga_VB9DKE4V36*MTY2OTM5MjYzNS4xLjAuMTY2OTM5MjYzNS4wLjAuMA'
            st.write("To donate to The Union of Concerned Scientists, click the following link. (%s)" % url)
        
        d3 = st.button("Earth Justice")
        if d3:
            st.write("This nonprofit aims to use their resoucres to advocat for better laws to help the planet. They not only have scientists on their team but legal experts as well!")
            url = 'https://act.earthjustice.org/a/givedonate-today-2?ms=web_menu_header'
            st.write("To donate to Earth Justice, click the following link. (%s)" % url)