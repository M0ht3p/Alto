import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Alto - OSINT Tool Recommendation Engine",
    page_icon="🔍",
    layout="centered"
)

# Title & Description
st.title("🔍 Alto: OSINT Recommendation Engine")
st.markdown(
    "Select your target search objective, your starting inputs, and your technical "
    "comfort level to get tailored Open Source Intelligence (OSINT) tool recommendations."
)

st.divider()

# Step 1: What is the goal/target of the search?
search_target = st.selectbox(
    "1. What are you looking to discover or investigate?",
    options=[
        "Select an option...",
        "Username / Social Media Accounts",
        "Email Address Details & Breaches",
        "Phone Number Details",
        "Domain / IP / Infrastructure",
        "Geolocation / Image Location",
        "Full Investigation / All-in-One Mapping"
    ]
)

# Step 2: What starting data does the user already have?
current_data = st.multiselect(
    "2. What information do you currently have to work with?",
    options=[
        "Username / Handle",
        "Email Address",
        "Phone Number",
        "Domain Name / Subdomain",
        "IP Address",
        "Image / Photograph",
        "Full Name"
    ]
)

# Step 3: Skill level filter
skill_level = st.select_slider(
    "3. Select your technical comfort level:",
    options=["All Levels", "Beginner (Web Only)", "Intermediate (CLI / Terminal)", "Advanced (APIs & Frameworks)"]
)

# Step 4: Optional target input for direct search link generation
target_value = st.text_input(
    "4. Optional: Enter your specific target value (e.g. username, domain, email) for quick links:",
    placeholder="e.g., target_user, example.com, or user@example.com"
)

# Tool Recommendation Database Logic
def recommend_tools(target, inputs, level):
    recommendations = []
    
    # --- Category: Username ---
    if target == "Username / Social Media Accounts":
        recommendations.append({
            "name": "WhatsMyName",
            "category": "Username Enumeration",
            "description": "Searches across hundreds of social media platforms and websites via a fast web interface.",
            "type": "Free Web Service",
            "level": "Beginner (Web Only)",
            "url": "https://whatsmyname.app/"
        })
        recommendations.append({
            "name": "Social Searcher",
            "category": "Social Media Search Engine",
            "description": "Allows real-time searching for content, users, and mentions across public social media platforms without logging in.",
            "type": "Free Web Service",
            "level": "Beginner (Web Only)",
            "url": "https://www.social-searcher.com/"
        })
        recommendations.append({
            "name": "Sherlock",
            "category": "Username Enumeration",
            "description": "Hunts down social media accounts across hundreds of networks using a command-line script.",
            "type": "Free / Open-Source",
            "level": "Intermediate (CLI / Terminal)",
            "url": "https://github.com/sherlock-project/sherlock"
        })
        recommendations.append({
            "name": "Maigret",
            "category": "Deep Username OSINT",
            "description": "An advanced fork of Sherlock that collects user profile details, avatars, and linked accounts from public profiles.",
            "type": "Free / Open-Source",
            "level": "Intermediate (CLI / Terminal)",
            "url": "https://github.com/soxoj/maigret"
        })
        recommendations.append({
            "name": "GHunt",
            "category": "Google Account Profiling",
            "description": "An offensive OSINT tool to extract information from any Google account using an email or username.",
            "type": "Free / Open-Source",
            "level": "Advanced (APIs & Frameworks)",
            "url": "https://github.com/mxrch/GHunt"
        })

    # --- Category: Email ---
    elif target == "Email Address Details & Breaches":
        recommendations.append({
            "name": "Have I Been Pwned",
            "category": "Data Breach Lookup",
            "description": "Checks if an email address has been compromised in known data breaches.",
            "type": "Free Web Service",
            "level": "Beginner (Web Only)",
            "url": "https://haveibeenpwned.com/"
        })
        recommendations.append({
            "name": "Epieos",
            "category": "Email to Profile Correlation",
            "description": "Finds hidden Google profiles, calendar invites, and linked services attached to an email address without triggering alerts.",
            "type": "Freemium",
            "level": "Beginner (Web Only)",
            "url": "https://epieos.com/"
        })
        recommendations.append({
            "name": "Hunter.io",
            "category": "Email Discovery & Verification",
            "description": "Finds professional email addresses associated with any domain, validates email addresses, and provides pattern analysis.",
            "type": "Freemium",
            "level": "Beginner (Web Only)",
            "url": "https://hunter.io/"
        })
        recommendations.append({
            "name": "Holehe",
            "category": "Email Registration Lookup",
            "description": "Checks if an email address is attached to registered accounts on 120+ sites without notifying the target.",
            "type": "Free / Open-Source",
            "level": "Intermediate (CLI / Terminal)",
            "url": "https://github.com/megadose/holehe"
        })
        recommendations.append({
            "name": "Emailrep.io",
            "category": "Email Reputation & Threat Intelligence",
            "description": "Uses AI and OSINT data to analyze email reputation, age, domain validity, and past malicious activities.",
            "type": "Freemium / API",
            "level": "Advanced (APIs & Frameworks)",
            "url": "https://emailrep.io/"
        })

    # --- Category: Phone ---
    elif target == "Phone Number Details":
        recommendations.append({
            "name": "Truecaller",
            "category": "Caller ID & Reverse Phone Lookup",
            "description": "Global crowd-sourced phone lookup to identify unknown callers, carrier information, associated names, and spam scores.",
            "type": "Freemium",
            "level": "Beginner (Web Only)",
            "url": "https://www.truecaller.com/"
        })
        recommendations.append({
            "name": "NumLookup",
            "category": "Free Reverse Phone Lookup",
            "description": "Provides instant caller identification, line type (mobile vs landline), carrier information, and social profile links.",
            "type": "Free Web Service",
            "level": "Beginner (Web Only)",
            "url": "https://www.numlookup.com/"
        })
        recommendations.append({
            "name": "OSINT Industries",
            "category": "Reverse Phone & Email Lookup",
            "description": "Discovers active profiles registered to a phone number across social networks and online platforms.",
            "type": "Freemium",
            "level": "Beginner (Web Only)",
            "url": "https://osint.industries/"
        })
        recommendations.append({
            "name": "PhoneInfoga",
            "category": "Phone Number OSINT",
            "description": "Gathers carrier info, country codes, international formats, and runs automated Google dorks against phone numbers.",
            "type": "Free / Open-Source",
            "level": "Intermediate (CLI / Terminal)",
            "url": "https://github.com/sundowndev/phoneinfoga"
        })
        recommendations.append({
            "name": "Ignorant",
            "category": "Phone Registration Enumeration",
            "description": "Checks if a phone number is registered on various social media platforms like Amazon, Instagram, and Snapchat.",
            "type": "Free / Open-Source",
            "level": "Intermediate (CLI / Terminal)",
            "url": "https://github.com/megadose/ignorant"
        })

    # --- Category: Domain / IP ---
    elif target == "Domain / IP / Infrastructure":
        recommendations.append({
            "name": "DNSDumpster",
            "category": "DNS Reconnaissance",
            "description": "Fast web-based tool to map out subdomains, DNS records, and IP mappings visually.",
            "type": "Free Web Service",
            "level": "Beginner (Web Only)",
            "url": "https://dnsdumpster.com/"
        })
        recommendations.append({
            "name": "SecurityTrails",
            "category": "Historical DNS & Domain OSINT",
            "description": "Provides extensive current and historical WHOIS records, DNS data, and subdomain discovery.",
            "type": "Freemium",
            "level": "Beginner (Web Only)",
            "url": "https://securitytrails.com/"
        })
        recommendations.append({
            "name": "Shodan",
            "category": "Internet-Connected Device Search Engine",
            "description": "Allows you to search for exposed servers, open ports, SSL certificates, and vulnerabilities linked to IP addresses or domains.",
            "type": "Freemium",
            "level": "Intermediate (CLI / Terminal)",
            "url": "https://www.shodan.io/"
        })
        recommendations.append({
            "name": "Censys",
            "category": "Attack Surface Analysis",
            "description": "Scans and inventories hosts, certificates, and networks connected to the internet.",
            "type": "Freemium",
            "level": "Intermediate (CLI / Terminal)",
            "url": "https://censys.io/"
        })
        recommendations.append({
            "name": "OWASP Amass",
            "category": "Subdomain & Attack Surface Mapping",
            "description": "In-depth attack surface mapping and network discovery framework.",
            "type": "Free / Open-Source",
            "level": "Advanced (APIs & Frameworks)",
            "url": "https://github.com/owasp-amass/amass"
        })

    # --- Category: Geolocation ---
    elif target == "Geolocation / Image Location":
        recommendations.append({
            "name": "Google Lens",
            "category": "Reverse Image Search",
            "description": "Locate original photo sources and identify landmarks or locations within an image visually.",
            "type": "Free Web Service",
            "level": "Beginner (Web Only)",
            "url": "https://lens.google.com/"
        })
        recommendations.append({
            "name": "Yandex Images",
            "category": "Facial & Landmark Reverse Search",
            "description": "Exceptionally powerful reverse image search engine for identifying matching facial features, locations, and obscure objects.",
            "type": "Free Web Service",
            "level": "Beginner (Web Only)",
            "url": "https://yandex.com/images/"
        })
        recommendations.append({
            "name": "SunCalc",
            "category": "Chronolocation & Shadow Analysis",
            "description": "Calculates sun position, shadows, and sunlight phases for any location and date to estimate photo timestamps.",
            "type": "Free Web Service",
            "level": "Beginner (Web Only)",
            "url": "https://www.suncalc.org/"
        })
        recommendations.append({
            "name": "ExifTool",
            "category": "Image Metadata Analysis",
            "description": "Extracts EXIF metadata from photographs, including GPS coordinates, camera model, time taken, and original filenames.",
            "type": "Free / Open-Source",
            "level": "Intermediate (CLI / Terminal)",
            "url": "https://exiftool.org/"
        })

    # --- Category: Full Investigation ---
    elif target == "Full Investigation / All-in-One Mapping":
        recommendations.append({
            "name": "OSINT Framework",
            "category": "OSINT Resource Directory",
            "description": "Interactive visual map categorizing hundreds of OSINT tools by data target type.",
            "type": "Free Web Service",
            "level": "Beginner (Web Only)",
            "url": "https://osintframework.com/"
        })
        recommendations.append({
            "name": "SpiderFoot",
            "category": "Automated OSINT Reconnaissance",
            "description": "Runs over 200 passive OSINT modules against a domain, email, username, or IP address to correlate data into a dashboard.",
            "type": "Free / Open-Source",
            "level": "Advanced (APIs & Frameworks)",
            "url": "https://github.com/smicallef/spiderfoot"
        })
        recommendations.append({
            "name": "Maltego",
            "category": "Visual Link Analysis",
            "description": "Renders relationships visually between people, domains, infrastructure, emails, and social media handles.",
            "type": "Freemium / Community Edition",
            "level": "Advanced (APIs & Frameworks)",
            "url": "https://www.maltego.com/"
        })
        recommendations.append({
            "name": "Recon-ng",
            "category": "Modular Reconnaissance Framework",
            "description": "Full-featured Web Reconnaissance framework written in Python with modular plugins for deep target profiling.",
            "type": "Free / Open-Source",
            "level": "Advanced (APIs & Frameworks)",
            "url": "https://github.com/lanmaster53/recon-ng"
        })

    # --- Context-Specific Recommendations (Inputs + Target Overlaps) ---
    if "Image / Photograph" in inputs and target == "Geolocation / Image Location":
        recommendations.append({
            "name": "Pic2Map",
            "category": "EXIF GPS Mapping",
            "description": "Extracts GPS telemetry directly from uploaded photos and plots it on Google Maps.",
            "type": "Free Web Service",
            "level": "Beginner (Web Only)",
            "url": "https://www.pic2map.com/"
        })

    if "IP Address" in inputs and target == "Domain / IP / Infrastructure":
        recommendations.append({
            "name": "IPinfo.io",
            "category": "IP Geolocation & ASN Lookup",
            "description": "Translates raw IP addresses into estimated physical locations, hosting providers, and ASN data.",
            "type": "Free Tier Available",
            "level": "Beginner (Web Only)",
            "url": "https://ipinfo.io/"
        })

    if "Full Name" in inputs:
        recommendations.append({
            "name": "FastPeopleSearch",
            "category": "Public Records Search",
            "description": "Look up public records, addresses, phone numbers, and associated relatives based on names.",
            "type": "Free Web Service",
            "level": "Beginner (Web Only)",
            "url": "https://www.fastpeoplesearch.com/"
        })

    # --- Filter by Skill Level ---
    if level != "All Levels":
        recommendations = [t for t in recommendations if t["level"] == level]

    return recommendations

# Execution Button
st.divider()

if st.button("Get OSINT Recommendations", type="primary"):
    if search_target == "Select an option...":
        st.warning("Please select what you are searching for to get a recommendation.")
    else:
        st.subheader("💡 Recommended OSINT Tools")
        
        # Display summary of user inputs
        inputs_str = ", ".join(current_data) if current_data else "None specified"
        st.info(f"**Target Goal:** {search_target}\n\n**Starting Inputs:** {inputs_str}\n\n**Skill Level Filter:** {skill_level}")
            
        # Quick Search Link Generator
        if target_value:
            st.markdown("### ⚡ Quick Search Links")
            if "Email" in search_target or "Email Address" in current_data:
                st.markdown(f"👉 Check Epieos for `{target_value}`: [Open Epieos Search](https://epieos.com/?q={target_value})")
                st.markdown(f"👉 Check HaveIBeenPwned for `{target_value}`: [Open HIBP Search](https://haveibeenpwned.com/account/{target_value})")
                st.markdown(f"👉 Check Hunter.io for domain of `{target_value}`: [Open Hunter Search](https://hunter.io/search/{target_value})")
            elif "Phone" in search_target or "Phone Number" in current_data:
                st.markdown(f"👉 Check Truecaller for `{target_value}`: [Open Truecaller Search](https://www.truecaller.com/search/global/{target_value})")
            elif "Username" in search_target or "Username / Handle" in current_data:
                st.markdown(f"👉 Check WhatsMyName for `{target_value}`: [Open WhatsMyName](https://whatsmyname.app/)")
            elif "Domain" in search_target or "Domain Name / Subdomain" in current_data:
                st.markdown(f"👉 Check DNSDumpster for `{target_value}`: [Open DNSDumpster](https://dnsdumpster.com/)")
            st.divider()

        tools = recommend_tools(search_target, current_data, skill_level)
        
        if not tools:
            st.warning("No tools match your exact skill level filter for this category. Try switching the skill level filter to 'All Levels'.")
        else:
            for tool in tools:
                with st.expander(f"📌 **{tool['name']}** ({tool['type']})", expanded=True):
                    st.write(f"**Category:** {tool['category']}")
                    st.write(f"**Skill Level Required:** {tool['level']}")
                    st.write(f"**How it helps:** {tool['description']}")
                    st.markdown(f"🔗 **Access Tool:** [{tool['name']} Direct Link]({tool['url']})")
