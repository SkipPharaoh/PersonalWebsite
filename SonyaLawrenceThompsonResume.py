# This is the code file used to create my resume

# Text Variables
Header = '>>>This resume was generated entirely in Python. For full sourcecode, view my portfolio.'
Name = 'SONYA LAWRENCE-THOMPSON'
Title = 'Financial Analysis & Data Science'
Contact = 'Jacksonville, FL\n904-615-5819\nlawrences@huntington.edu\nlinkedin.com/in/sonya-lt\ngithub.com/sonya-7'
Portfolio = 'Portfolio: https://sonya-personal-website.vercel.app/about/'

ProjectsHeader = 'PROJECTS/PUBLICATIONS'
ProjectOneTitle = 'Personal Reading Trends'
ProjectOneDesc = '- Captivating visualization of personal literary journey\n- Interactive Power Bi dashboard and word clouds\n- Average of 1 book per month goal achieved'
ProjectTwoTitle = 'US Data-Job Salary Trends'
ProjectTwoDesc = '- In-depth analysis of North American data-job salaries\n- Personal research and data analysis for salary negotiation\n- Created in a Jupyter Notebook using Python'
ProjectThreeTitle = 'IBM Data Science Capstone'
ProjectThreeDesc = '- Predicted Falcon 9 first stage landing likelihood\n- Real-world Data Science problem simulation\n- Machine learning model for accurate predictions'

WorkHeader = 'EXPERIENCE'
WorkOneTitle = 'Financial Analyst, Jacksonville Orthopaedic Institute'
WorkOneTime = 'Sep 2022 - Oct 2023'
WorkOneDesc = '- Automated company-wide processes with Excel and Python\n- Created new data management tools and dashboards\n- Implemented budget processes and conducted monthly variance analysis'
WorkTwoTitle = 'Data Quality Analyst, FCRD Services'
WorkTwoTime = 'Nov 2020 - Sep 2022'
WorkTwoDesc = '- Built and maintained financial models for ROI and Cash flow projections\n- Developed dashboards to measure and monitor product and service effectiveness\n- Conducted drill-down analysis for performance improvements'
WorkThreeTitle = 'Accountant Assistant, Indiana Stamp Company'
WorkThreeTime = 'Dec 2019 - Nov 2020'
WorkThreeDesc = '- Managed tax compliance and streamlined accounts payable procedures\n- Oversaw daily and monthly bank reconciliation statements\n- Safeguarded customer data using proprietory software and cloud-based systems'
WorkFourTitle = "Staff Accountant/Office Manager, BT'S Plumbing and Heating"
WorkFourTime = 'Jul 2016 - Oct 2019'
WorkFourDesc = '- Lead company-wide data transformation from hardware to software\n- Analyzed complex business problems, providing practical solutions\n- Managed financial data using QuickBooks, Excel, and other business software'

SkillsHeader = 'SKILLS'
SkillsDesc = '- Excel\n- SQL\n- Python\n- Pandas\n- NumPy\n- Data Visualization\n- Data Cleaning\n- Probability/Statistics\n- Data Manipulation\n- Data Storytelling\n- Power Bi'

EduHeader = 'EDUCATION'
EduOneTitle = 'Huntington University\nBachelors Degree'
EduOneTime = '2012-2016'
EduOneDesc = 'Major1: Accounting\nMajor2: Psychology\nMinor: Business Management'
CertifOneTitle = 'EdX\nProfessional Certificate'
CertifOneTime = '2022'
CertifOneDesc = 'Major: Data Science'
CertifOneDesc2 = 'Learned:\n - Python, R, SQL,\n - Web-Scraping\n - Data Cleaning \n - Data Manipulation\n - Machine Learning \n - Data Analysis\n - Data Visualization'

# Setting style for bar graphs
import matplotlib.pyplot as plt

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

fig, ax = plt.subplots(figsize=(8.5, 11))

# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.6, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)
plt.axhline(y=.6, xmin=0, xmax=1, color='#ffffff', linewidth=3)

# set background color
ax.set_facecolor('white')

# remove axes
plt.axis('off')

# add text
plt.annotate(Contact, (.7,.906), weight='regular', fontsize=8, color='#ffffff')
plt.annotate(Header, (.02,.98), weight='regular', fontsize=8, alpha=.6)
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
plt.annotate(WorkOneTitle, (.02,.528), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (.02,.508), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkOneDesc, (.04,.46), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (.02,.425), weight='bold', fontsize=10)
plt.annotate(WorkTwoTime, (.02,.405), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkTwoDesc, (.04,.357), weight='regular', fontsize=9)
plt.annotate(WorkThreeTitle, (.02,.322), weight='bold', fontsize=10)
plt.annotate(WorkThreeTime, (.02,.302), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkThreeDesc, (.04,.254), weight='regular', fontsize=9)
plt.annotate(WorkFourTitle, (.02,.219), weight='bold', fontsize=10)
plt.annotate(WorkFourTime, (.02,.199), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkFourDesc, (.04,.151), weight='regular', fontsize=9)
plt.annotate(SkillsHeader, (.7,.85), weight='bold', fontsize=11, color='#ffffff')
plt.annotate(SkillsDesc, (.711,.645), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(EduHeader, (.7,.57), weight='bold', fontsize=11, color='#ffffff')
plt.annotate(EduOneTitle, (.7,.51), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(EduOneTime, (.7,.49), weight='regular', fontsize=9, alpha=.6, color='#ffffff')
plt.annotate(EduOneDesc, (.7,.452), weight='regular', fontsize=9, color='#ffffff')
plt.annotate(CertifOneTitle, (.7,.393), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(CertifOneTime, (.7,.373), weight='regular', fontsize=9, alpha=.6, color='#ffffff')
plt.annotate(CertifOneDesc, (.7,.353), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(CertifOneDesc2, (.7,.2), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(Portfolio, (.02,.005), weight='bold', fontsize=10)

plt.show()
# plt.savefig('SonyaLawrenceThompsonResume.png', dpi=300, bbox_inches='tight')

