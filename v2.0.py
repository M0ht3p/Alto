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
            "name": "Holehe",
            "category": "Email Registration Lookup",
            "description": "Checks if an email address is attached to registered accounts on 120+ sites without notifying the target.",
            "type": "Free / Open-Source",
            "level": "Intermediate (CLI / Terminal)",
            "url": "https://github.com/megadose/holehe"
        })

    # --- Category: Phone ---
    elif target == "Phone Number Details":
        recommendations.append({
            "name": "PhoneInfoga",
            "category": "Phone Number OSINT",
            "description": "Gathers carrier info, country codes, international formats, and runs automated Google dorks against phone numbers.",
            "type": "Free / Open-Source",
            "level": "Intermediate (CLI / Terminal)",
            "url": "https://github.com/sundowndev/phoneinfoga"
        })
        recommendations.append({
            "name": "OSINT Industries / UserSearch",
            "category": "Reverse Phone Lookup",
            "description": "Checks linked accounts and registered services connected to a phone number.",
            "type": "Freemium",
            "level": "Beginner (Web Only)",
            "url": "https://osint.industries/"
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
            "name": "Shodan",
            "category": "Internet-Connected Device Search Engine",
            "description": "Allows you to search for exposed servers, open ports, SSL certificates, and vulnerabilities linked to IP addresses or domains.",
            "type": "Freemium",
            "level": "Intermediate (CLI / Terminal)",
            "url": "https://www.shodan.io/"
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
            "name": "ExifTool",
            "category": "Image Metadata Analysis",
            "description": "Extracts EXIF metadata from photographs, including GPS coordinates, camera model, time taken, and original filenames.",
            "type": "Free / Open-Source",
            "level": "Intermediate (CLI / Terminal)",
            "url": "https://exiftool.org/"
        })
        recommendations.append({
            "name": "Google Lens",
            "category": "Reverse Image Search",
            "description": "Locate original photo sources and identify landmarks or locations within an image visually.",
            "type": "Free Web Service",
            "level": "Beginner (Web Only)",
            "url": "https://lens.google.com/"
        })

    # --- Category: Full Investigation ---
    elif target == "Full Investigation / All-in-One Mapping":
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
