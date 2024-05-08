# This is the code file used to create my resume

# Resume details grouped by sections
Header = '>>This resume was generated entirely in Python. For full source code, see portfolio link below.'
Name = 'SONYA LAWRENCE-THOMPSON'.upper()
Title = 'Financial Analysis & Data Science'
Contact = 'New York, NY\n904-615-5819\nlawrences@huntington.edu\nlinkedin.com/in/sonya-lt\ngithub.com/sonya-7'
Portfolio = 'https://sonya-personal-website.vercel.app/about/'

ProjectsHeader = 'PROJECTS/PUBLICATIONS'
ProjectOneTitle = 'Personal Reading Trends'
ProjectOneDesc = '- Captivating visualization of personal literary journey\n- Interactive Power Bi dashboard and word clouds\n- Read 1 book per month; goal achieved'
ProjectTwoTitle = 'US Data-Job Salary Trends'
ProjectTwoDesc = '- Created in a Jupyter Notebook using Python\n- In-depth analysis of North American data related job salaries\n- Personal research and data analysis for salary negotiation'
ProjectThreeTitle = 'IBM Data Science Capstone'
ProjectThreeDesc = '- Real-world Data Science problem simulation\n- Successfully predicted likelihood of Falcon 9 first stage landing\n- Created machine learning model for accurate aerospace predictions'

WorkHeader = 'EXPERIENCE'
WorkOneTitle = 'Financial Analyst\n Jacksonville Orthopaedic Institute'
WorkOneTime = 'Sep 2022 - Oct 2023'
WorkOneDesc = '- Created new data management tools and dashboards for 7 facilities\n- Implemented budget processes and conducted monthly variance analysis\n- Automated company-wide processes with SQL, Excel, PowerBi and Python'
WorkTwoTitle = 'Data Quality Analyst\n FCRD Services'
WorkTwoTime = 'Nov 2020 - Sep 2022'
WorkTwoDesc = '- Built and maintained financial models for ROI and cash flow projections\n- Designed key performance indicators to guide company wide data analysis\n- Developed dashboards to measure and monitor product and service effectiveness'
WorkThreeTitle = 'Accountant Assistant\n Indiana Stamp Company'
WorkThreeTime = 'Dec 2019 - Nov 2020'
WorkThreeDesc = '- Oversaw daily and monthly bank reconciliation statements\n- Streamlined accounts payable procedures, improving efficiency by over 90%\n- Safeguarded customer data using proprietory software and cloud-based systems'
WorkFourTitle = "Staff Accountant/Office Manager\n BT'S Plumbing and Heating"
WorkFourTime = 'Jul 2016 - Oct 2019'
WorkFourDesc = '- Lead company-wide data transformation from hardware to software\n- Analyzed complex business problems, providing practical solutions\n- Managed financial data using QuickBooks, Excel, and other business software'

SkillsHeader = 'SKILLS'
SkillsDesc = '- Excel\n- SQL\n- Python\n- Pandas\n- NumPy\n- Data Visualization\n- Data Cleaning\n- Probability/Statistics\n- Data Manipulation\n- Data Storytelling\n- Power Bi'

EduHeader = 'EDUCATION'
EduOneTitle = 'Huntington University\nBachelors Degree\nCum Laude'
EduOneTime = '2012 - 2016'
EduOneDesc = 'Major 1: Accounting\nMajor 2: Psychology\nMinor: Management'
CertifOneTitle = 'EdX\nProfessional Certificate'
CertifOneTime = '2022'
CertifOneDesc = 'Major: Data Science'
CertifOneDesc2 = 'Learned:\n\t\t\t - Python, R, SQL,\n\t\t\t - Web-Scraping\n\t\t\t - Data Cleaning \n\t\t\t - Data Manipulation\n\t\t\t - Machine Learning \n\t\t\t - Data Analysis\n\t\t\t - Data Visualization'

# Import styling package
import matplotlib.pyplot as plt

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

# Set borders
fig, ax = plt.subplots(figsize=(8.5, 11))

# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.6, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=5)
plt.axhline(y=.6, xmin=0, xmax=1, color='#ffffff', linewidth=5)

# set background color
ax.set_facecolor('white')

# remove axes
plt.axis('off')

# add texts to complete resume
plt.annotate(Header, (.02,.98), weight='regular', fontsize=8, alpha=.6)
plt.annotate(Contact, (.7,.906), weight='regular', fontsize=8, color='#ffffff')
plt.annotate(SkillsHeader, (.7,.85), weight='bold', fontsize=11, color='#ffffff')
plt.annotate(SkillsDesc, (.711,.645), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(EduHeader, (.7,.57), weight='bold', fontsize=11, color='#ffffff')
plt.annotate(EduOneTitle, (.7,.51), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(EduOneTime, (.7,.49), weight='regular', fontsize=9, alpha=.6, color='#ffffff')
plt.annotate(EduOneDesc, (.7,.44), weight='regular', fontsize=9, color='#ffffff')
plt.annotate(CertifOneTitle, (.7,.38), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(CertifOneTime, (.7,.363), weight='regular', fontsize=9, alpha=.6, color='#ffffff')
plt.annotate(CertifOneDesc, (.7,.343), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(CertifOneDesc2, (.7,.2), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(Name, (.02,.94), weight='bold', fontsize=19)
plt.annotate(Title, (.02,.91), weight='regular', fontsize=14)
plt.annotate(ProjectsHeader, (.02,.86), weight='bold', fontsize=10, color='#6b4d85')
plt.annotate(ProjectOneTitle, (.02,.832), weight='bold', fontsize=10)
plt.annotate(ProjectOneDesc, (.04,.78), weight='regular', fontsize=9)
plt.annotate(ProjectTwoTitle, (.02,.745), weight='bold', fontsize=10)
plt.annotate(ProjectTwoDesc, (.04,.693), weight='regular', fontsize=9)
plt.annotate(ProjectThreeTitle, (.02,.658), weight='bold', fontsize=10)
plt.annotate(ProjectThreeDesc, (.04,.606), weight='regular', fontsize=9)
plt.annotate(WorkHeader, (.02,.556), weight='bold', fontsize=10, color='#6b4d85')
plt.annotate(WorkOneTitle, (.02,.508), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (.02,.488), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkOneDesc, (.04,.44), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (.02,.40), weight='bold', fontsize=10)
plt.annotate(WorkTwoTime, (.02,.38), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkTwoDesc, (.04,.332), weight='regular', fontsize=9)
plt.annotate(WorkThreeTitle, (.02,.292), weight='bold', fontsize=10)
plt.annotate(WorkThreeTime, (.02,.272), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkThreeDesc, (.04,.224), weight='regular', fontsize=9)
plt.annotate(WorkFourTitle, (.02,.184), weight='bold', fontsize=10)
plt.annotate(WorkFourTime, (.02,.164), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkFourDesc, (.04,.116), weight='regular', fontsize=9)
plt.annotate(Portfolio, (.02,.005), weight='bold', fontsize=10)

plt.savefig('SonyaLawrenceThompsonResume.pdf', dpi=300, bbox_inches='tight')

