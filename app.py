from pathlib import Path
import streamlit as st
from PIL import Image



# -- PATH SETTINGS -- #
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir/ "assets" / "CV.pdf" 
profile_pic = current_dir / "assets" / "profile-pic.png"



# -- INFO -- #
PAGE_TITLE = "Digital Resume | Name"
PAGE_ICON = "👋"
NAME = "Full Name"
DESCRIPTION = """
Insert short description here
"""
EMAIL = "your@email.com"
SOCIAL_MEDIA = {
	"LinkedIn": "",
	"GitHub": "",
	"Twitter": ""
}

PROJECTS = {
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# -- USER INPUT SIDE BAR -- #
with st.sidebar:
	with st.form("Info"):
		st.subheader("About")
		user_name = st.text_input("Name:", placeholder='Enter full name')
		user_description = st.text_area("Description:", placeholder='Introduce yourself')
		user_email = st.text_input("Email:", placeholder='Enter your email address')

		st.subheader("Socials")
		linkedin = st.text_input("LinkedIn Profile:", placeholder='Insert link')
		github = st.text_input("GitHub Profile:", placeholder='Insert link')
		twitter = st.text_input("Twitter Profile:", placeholder='Insert link')
		#blog = st.text_input("Blog Address:", placeholder='Insert link')

		st.subheader("Expertise")
		exp = st.text_area("Experience & Qualifications:", placeholder='Write about your experience and expertise').splitlines()

		skills = st.text_area("Skills:", placeholder='What are your strong points').splitlines()

		
		st.subheader("Work Experience")
		master_list = []
		work_list = {}
		work_list['title'] = st.text_input("Title:", placeholder='Your position')
		work_list['date'] = st.text_input("Date:", placeholder='From: - to:')
		work_resp = st.text_area("Responsibilities:", placeholder='Write about your tasks and duties').splitlines()

		st.subheader("Projects")
		proj_name = st.text_input("Project:", placeholder='Enter project name')
		proj_link = st.text_input("Link:", placeholder='Enter project link')

		submitted = st.form_submit_button("Update")
		if submitted:
			NAME = user_name
			DESCRIPTION = user_description
			SOCIAL_MEDIA['LinkedIn'] = linkedin
			SOCIAL_MEDIA['GitHub'] = github
			SOCIAL_MEDIA['Twitter'] = twitter
			#SOCIAL_MEDIA['Blog'] = blog
			master_list.append(work_list)
			PROJECTS[proj_name] = proj_link
			EMAIL = user_email
			


#	user_name = st.text_input("Enter your name:")
#	if user_name != '':
#		NAME = user_name
#
#	user_description = st.text_area("Please enter a short description:")
#	if user_description != '':
#		DESCRIPTION = user_description


# -- LOAD CSS, PDF & PROFILE PIC -- #
with open(css_file) as f:
	st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
	PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# -- PROFILE HEADER -- #
col1, col2 = st.columns([1,2], gap="small")
with col1:
	st.image(profile_pic, width=200)
with col2:
	st.title(NAME)
	st.write(DESCRIPTION)
	st.download_button(
		label="📄 Download Resume",
		data=PDFbyte,
		file_name=resume_file.name,
		mime="application/octet-stream",
		)
	st.write("📧", EMAIL)


# -- SOCIALS -- #
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
	cols[index].write(f"[{platform}]({link})")


# -- EXPERIENCE & QUALIFICATIONS -- #
st.write("#")
st.subheader("Experience & Qualifications")
if submitted:
	for i in exp:
		st.write(f"""
			- ✔️ {i}
			""")
else:
	st.write(
		"""

		"""
		)



# -- SKILLS -- #
st.write("#")
st.subheader("Skills")
if submitted and skills != '':
	for i in skills:
		st.write(f"""
			- {i}
			"""
			)
else:
	st.write(
		"""

		"""
		)

# -- WORK HISTORY -- #

# -- JOB ONE -- #
st.write("#")
st.subheader("Work History")
st.write("---")

if submitted and master_list != '':
	for i in master_list:
		st.write(i['title'])
		st.write(i['date'])
	for i in work_resp:
		st.write(f"""
			- {i}
			""")
else:
	st.write("Work Title")
	st.write("From - To")
	st.write(
		"""
		"""
		)


# -- JOB TWO -- #
#st.write("#")
#st.subheader("Work History 2")
#st.write("---")

#st.write("Work Title 2")
#st.write("From - To")
#st.write(
#	"""
#	- Responsibility 1
#	- Responsibility 2
#	- Responsibility 3
#	"""
#	)


if PROJECTS !='':
	# -- PROJECTS & ACCOMPLISHMENTS -- #
	st.write("#")
	st.subheader("Projects & Accomplishments")
	st.write("---")
	for project, link in PROJECTS.items():
		st.write('🏆 ' + f"[{project}]({link})")



