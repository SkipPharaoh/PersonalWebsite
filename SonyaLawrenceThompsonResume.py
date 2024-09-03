# # This is the code file used to create my resume

# Resume details grouped by sections
Header = '   This resume was generated entirely in Python using matplotlib.\n   See portfolio link for full source code: https://github.com/Sonya-7/Resume'
Name = 'SONYA LAWRENCE-THOMPSON'.upper()
Title = 'Financial Data Analysis & Data Science'
contactHeader = 'CONTACT'
Contact = 'Jacksonville, FL\n904-615-5819\nlawrences@huntington.edu\nlinkedin.com/in/sonya-lt\nhttps://sonyalt.vercel.app'
Portfolio = 'https://sonyalt.vercel.app'
QRHeader = 'PORTFOLIO'

ProjectsHeader = 'PROJECTS/PUBLICATIONS'
ProjectOneTitle = 'Personal Reading Trends'
ProjectOneDesc = '- Captivating visualization of my literary journey\n- Interactive Power Bi dashboard and word clouds\n- Read 1 book per month as of January 2021; personal development goal achieved'
ProjectTwoTitle = 'US Data-Job Salary Trends'
ProjectTwoDesc = '- Created in a Jupyter Notebook using Python\n- In-depth analysis of North American data related job salaries\n- Manipulated large open souce dataset to extract useful information'
ProjectThreeTitle = 'IBM Data Science Capstone'
ProjectThreeDesc = '- Real-world Data Science problem simulation\n- Created machine learning models (MLM) for accurate aerospace predictions\n- Successfully predicted the likelihood of SpaceX\'s Falcon 9 first-stage landing'

WorkHeader = 'RELEVANT EXPERIENCE'
WorkOneTitle = 'Financial Analyst\n Jacksonville Orthopaedic Institute'
WorkOneTime = ' Sep 2022 - Oct 2023'
WorkOneDesc = '- Collaborated with cross-functional teams to create new data management tools\n  and dashboards for 7 medical facilities\n- Implemented various stored procedures for data cleaning and extraction using\n   SQL Server Management Studio and Visual Studio Code\n- Automated various financial processes using SQL, Excel, PowerBi, and Python'
WorkTwoTitle = 'Data Quality Analyst\n FCRD Services'
WorkTwoTime = ' Nov 2020 - Sep 2022'
WorkTwoDesc = '- Built and maintained financial models for ROI and cash flow projections\n- Designed key performance indicators to guide company-wide data analysis\n- Developed dashboards to measure and monitor product and service effectiveness'
WorkThreeTitle = 'Accountant Assistant\n Indiana Stamp Company'
WorkThreeTime = ' Dec 2019 - Nov 2020'
WorkThreeDesc = '- Improved accounts payable efficiency by over 90%\n- Oversaw daily and monthly bank reconciliation statements\n- Managed customer data using proprietary software and cloud-based systems'
WorkFourTitle = "Staff Accountant/Office Manager\n BT'S Plumbing and Heating"
WorkFourTime = ' Jul 2016 - Oct 2019'
WorkFourDesc = '- Initiated company-wide data migration to cloud database\n- Analyzed complex business problems, providing practical solutions\n- Managed financial data using QuickBooks, Excel, and other business software'

SkillsHeader = 'SKILLS'
SkillsDesc = '- Excel\n- SQL\n- Python\n- Data Visualization\n- Data Cleaning\n- Probability/Statistics\n- Data Modeling\n- Data Migration\n- Data Manipulation\n- Data Transformation\n- Data Storytelling\n- Power Bi'

EduHeader = 'EDUCATION'
EduOneTitle = 'Huntington University\nBachelors Degree\n *Cum Laude*'
EduOneTime = '2012 - 2016'
EduOneDesc = 'Major 1: Accounting\nMajor 2: Psychology\nMinor 1: Management'
CertifOneTitle = 'EdX\nProfessional Certificate'
CertifOneTime = '2022'
CertifOneDesc = 'Major: Data Science'
CertifOneDesc2 = 'Learned:\n\t\t\t - Python, R, SQL,\n\t\t\t - Web-Scraping\n\t\t\t - Data Cleaning \n\t\t\t - Data Manipulation\n\t\t\t - Machine Learning \n\t\t\t - Data Analysis\n\t\t\t - Data Visualization\n\t\t\t - API integration'

# FFHeader = 'Fun Facts'
# FFOneTitle = 'Fluent in conversational Spanish'
# FFTwoTitle = 'ESL Certified Instructor'
# FFThreeTitle = 'Karate - Orange Belt'

# Import styling package
import matplotlib.pyplot as plt
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

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
# plt.axhline(y=.164, xmin=0, xmax=1, color='#ffffff', linewidth=5)

# set background color
ax.set_facecolor('white')

# remove axes
plt.axis('off')

# add right bound texts to complete resume
plt.annotate(contactHeader, (.7,.98), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(Contact, (.7,.906), weight='regular', fontsize=8, color='#ffffff')
plt.annotate(SkillsHeader, (.7,.85), weight='bold', fontsize=11, color='#ffffff')
plt.annotate(SkillsDesc, (.711,.64), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(EduHeader, (.7,.57), weight='bold', fontsize=11, color='#ffffff')
plt.annotate(EduOneTitle, (.7,.51), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(EduOneTime, (.7,.49), weight='regular', fontsize=9, alpha=.7, color='#ffffff')
plt.annotate(EduOneDesc, (.7,.44), weight='regular', fontsize=9, color='#ffffff')
plt.annotate(CertifOneTitle, (.7,.39), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(CertifOneTime, (.7,.373), weight='regular', fontsize=9, alpha=.7, color='#ffffff')
plt.annotate(CertifOneDesc, (.7,.353), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(CertifOneDesc2, (.7,.19), weight='regular', fontsize=10, color='#ffffff')
# plt.annotate(FFHeader, (.7,.13), weight='bold', fontsize=11, color='#ffffff')
# plt.annotate(FFOneTitle, (.7, .105), weight='regular', fontsize=10, color='#ffffff')
# plt.annotate(FFTwoTitle, (.7, .09), weight='regular', fontsize=10, color='#ffffff')
# plt.annotate(FFThreeTitle, (.7, .075), weight='regular', fontsize=10, color='#ffffff')

# add left bound texts to complete resume
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
plt.annotate(WorkOneDesc, (.04,.408), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (.02,.362), weight='bold', fontsize=10) 
plt.annotate(WorkTwoTime, (.02,.342), weight='regular', fontsize=9, alpha=.6) 
plt.annotate(WorkTwoDesc, (.04,.292), weight='regular', fontsize=9)
plt.annotate(WorkThreeTitle, (.02,.246), weight='bold', fontsize=10)
plt.annotate(WorkThreeTime, (.02,.226), weight='regular', fontsize=9, alpha=.6) 
plt.annotate(WorkThreeDesc, (.04,.176), weight='regular', fontsize=9)
plt.annotate(WorkFourTitle, (.02,.13), weight='bold', fontsize=10)
plt.annotate(WorkFourTime, (.02,.11), weight='regular', fontsize=9, alpha=.6) 
plt.annotate(WorkFourDesc, (.04,.06), weight='regular', fontsize=9)
plt.annotate(Header, (.02,.005), weight='regular', fontsize=7, alpha=.6)

plt.savefig('SonyaLawrenceThompsonResume.pdf', dpi=300, bbox_inches='tight')
