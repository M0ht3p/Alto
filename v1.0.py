import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="OSINT Tool Recommendation Engine",
    page_icon="🔍",
    layout="centered"
)

# Title & Description
st.title("🔍 OSINT Tool Recommendation Engine")
st.markdown(
    "Select your target search objective and what information you currently possess "
    "to get tailored Open Source Intelligence (OSINT) tool recommendations."
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

# Tool Recommendation Database Logic
def recommend_tools(target, inputs):
    recommendations = []
    
    if target == "Username / Social Media Accounts":
        recommendations.append({
            "name": "Sherlock / WhatsMyName",
            "category": "Username Enumeration",
            "description": "Searches across hundreds of social media platforms and websites to check if a specific username is registered.",
            "type": "Free / Open-Source"
        })
        recommendations.append({
            "name": "Maigret",
            "category": "Deep Username OSINT",
            "description": "An advanced fork of Sherlock that collects user profile details, avatars, and linked accounts from public profiles.",
            "type": "Free / Open-Source"
        })
        # TOOL PLACEHOLDER 1: recommendations.append({"name": "", "category": "", "description": "", "type": ""})
        # TOOL PLACEHOLDER 2: recommendations.append({"name": "", "category": "", "description": "", "type": ""})

    elif target == "Email Address Details & Breaches":
        recommendations.append({
            "name": "Holehe",
            "category": "Email Registration Lookup",
            "description": "Checks if an email address is attached to registered accounts on sites like Twitter, Instagram, Imgur, and 120+ others without notifying the target.",
            "type": "Free / Open-Source"
        })
        recommendations.append({
            "name": "Have I Been Pwned",
            "category": "Data Breach Lookup",
            "description": "Checks if an email address has been compromised in known data breaches.",
            "type": "Free Web Service"
        })
        recommendations.append({
            "name": "Epieos",
            "category": "Email to Profile Correlation",
            "description": "Finds hidden Google profiles, calendar invites, and linked services attached to an email address without triggering alerts.",
            "type": "Free Tier Available"
        })
        # TOOL PLACEHOLDER 3: recommendations.append({"name": "", "category": "", "description": "", "type": ""})
        # TOOL PLACEHOLDER 4: recommendations.append({"name": "", "category": "", "description": "", "type": ""})

    elif target == "Phone Number Details":
        recommendations.append({
            "name": "PhoneInfoga",
            "category": "Phone Number OSINT",
            "description": "Gathers carrier info, country codes, international formats, and runs automated Google dorks against phone numbers.",
            "type": "Free / Open-Source"
        })
        recommendations.append({
            "name": "OSINT Industries / UserSearch",
            "category": "Reverse Phone Lookup",
            "description": "Checks linked accounts and registered services connected to a phone number.",
            "type": "Freemium"
        })
        # TOOL PLACEHOLDER 5: recommendations.append({"name": "", "category": "", "description": "", "type": ""})
        # TOOL PLACEHOLDER 6: recommendations.append({"name": "", "category": "", "description": "", "type": ""})

    elif target == "Domain / IP / Infrastructure":
        recommendations.append({
            "name": "OWASP Amass & theHarvester",
            "category": "Subdomain & Attack Surface Mapping",
            "description": "Collects subdomains, IP ranges, DNS records, and email addresses associated with a target domain.",
            "type": "Free / Open-Source"
        })
        recommendations.append({
            "name": "Shodan / Censys",
            "category": "Internet-Connected Device Search Engine",
            "description": "Allows you to search for exposed servers, open ports, SSL certificates, and vulnerabilities linked to IP addresses or domains.",
            "type": "Freemium"
        })
        # TOOL PLACEHOLDER 7: recommendations.append({"name": "", "category": "", "description": "", "type": ""})
        # TOOL PLACEHOLDER 8: recommendations.append({"name": "", "category": "", "description": "", "type": ""})

    elif target == "Geolocation / Image Location":
        recommendations.append({
            "name": "ExifTool",
            "category": "Image Metadata Analysis",
            "description": "Extracts EXIF metadata from photographs, including GPS coordinates, camera model, time taken, and original filenames.",
            "type": "Free / Open-Source"
        })
        recommendations.append({
            "name": "Google Lens / PimEyes",
            "category": "Reverse Image Search & Visual OSINT",
            "description": "Helps locate original photo sources, perform facial recognition (PimEyes), or identify landmarks and locations within an image.",
            "type": "Freemium"
        })
        # TOOL PLACEHOLDER 9: recommendations.append({"name": "", "category": "", "description": "", "type": ""})
        # TOOL PLACEHOLDER 10: recommendations.append({"name": "", "category": "", "description": "", "type": ""})

    elif target == "Full Investigation / All-in-One Mapping":
        recommendations.append({
            "name": "SpiderFoot",
            "category": "Automated OSINT Reconnaissance",
            "description": "Runs over 200 passive OSINT modules against a domain, email, username, or IP address to correlate data into a dashboard.",
            "type": "Free / Open-Source"
        })
        recommendations.append({
            "name": "Maltego",
            "category": "Visual Link Analysis",
            "description": "Renders relationships visually between people, domains, infrastructure, emails, and social media handles.",
            "type": "Freemium / Community Edition"
        })
        # TOOL PLACEHOLDER 11: recommendations.append({"name": "", "category": "", "description": "", "type": ""})
        # TOOL PLACEHOLDER 12: recommendations.append({"name": "", "category": "", "description": "", "type": ""})

    # TOOL PLACEHOLDER 13: Add custom logic or tools based on current_data inputs here
    # TOOL PLACEHOLDER 14: Add custom logic or tools based on current_data inputs here
    # TOOL PLACEHOLDER 15: Add custom logic or tools based on current_data inputs here

    return recommendations

# Button to execute
st.divider()

if st.button("Get OSINT Recommendations", type="primary"):
    if search_target == "Select an option...":
        st.warning("Please select what you are searching for to get a recommendation.")
    else:
        st.subheader("💡 Recommended OSINT Tools")
        
        # Display summary of input
        if current_data:
            st.info(f"**Target Goal:** {search_target}\n\n**Starting Inputs:** {', '.join(current_data)}")
        else:
            st.info(f"**Target Goal:** {search_target}\n\n**Starting Inputs:** *None specified*")
            
        tools = recommend_tools(search_target, current_data)
        
        for tool in tools:
            with st.expander(f"📌 **{tool['name']}** ({tool['type']})", expanded=True):
                st.write(f"**Category:** {tool['category']}")
                st.write(f"**How it helps:** {tool['description']}")
