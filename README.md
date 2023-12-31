# EcoInsight Dashboard

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Existing Features](#existing-features)
4. [Technologies Used](#technologies)
5. [Validations](#validations)
6. [Design Elements](#design-elements)
7. [Learning Outcomes](#learning-outcomes)
8. [User Stories](#user-stories)
9. [User Flow](#user-flow)
10. [Task Flow](#task-flow)
11. [Additional Notes](#additional-notes)
12. [Testing](#testing)
13. [Usability Testing](#usability-testing)
14. [Credits](#credits)

## Introduction
In an era where understanding and responding to environmental challenges is paramount, the EcoInsight Dashboard serves as a critical tool for visualizing complex global data. 
By transforming the comprehensive reports of the United Nations into intuitive and interactive bar graphs, we offer a clear and accessible window into the state of our planet.
This is a Flask web application. 

 ![Mockup](doc/mockup.jpg)

Key Features:

- UN Data Visualization: Experience the vast repository of United Nations environmental data transformed into easy-to-understand bar graphs, highlighting key metrics and trends.

- Insightful Interpretations: Go beyond raw numbers and dive into meaningful insights drawn from global environmental reports, presented in a clear and engaging format.

- Interactive Engagement: Engage with the data through interactive elements, allowing for a personalized exploration of global environmental issues and their implications.

- Timely Updates: Stay informed with the most current data, as our dashboard regularly updates to reflect the latest findings and reports from the United Nations.

- Educational Tool: Use the dashboard as an educational resource to understand and teach others about environmental trends, challenges, and progress on a global scale.


## Features

- Navigation with links to pages, responsive on all devices.
- Compact and Sticky Navigation: As you scroll down, the navigation bar neatly shrinks and remains fixed to the top of the screen. This feature enhances the user experience by providing continuous access to the main links, 
regardless of where you are on the page. It's fully responsive, ensuring seamless functionality across all devices. 

- Efficient #id-based Navigation: Effortlessly navigate through various sections of the dashboard with our #id-based system. Each segment is thoughtfully arranged, 
offering easy access through a straightforward click. This streamlined navigation guarantees quick and efficient access to essential information, tailored for intuitive user interaction.
 ![Navigation](doc/features/01-nav.jpg)
 ![Navigation height](doc/features/02-nav.jpg)
 ![Navigation responsive](doc/features/03-nav.jpg)
  
- Footer with social icons, link to pdf and direct link to Github.
Footer with UN Information Disclaimer, Whitepaper Link, and GitHub Repository Access.
The footer section of the page prominently displays a disclaimer regarding the source of the United Nations information, ensuring transparency and proper accreditation. 
This acknowledgement includes a direct link to the original whitepaper PDF, allowing visitors to access comprehensive details and in-depth analysis directly from the United Nations. 
Additionally, a link to a personal GitHub repository is featured, inviting users to explore the coding projects, collaborate, and contribute to ongoing developments. 
This area serves as a critical hub for resource sharing and intellectual engagement, omitting the previously mentioned social media icons and restaurant-specific information 
like address, opening hours, and contact details. The footer also reiterates the copyright information, underscoring the unique nature and ownership of the website's content.  
  ![Footer](doc/features/04-footer.jpg)

- Favicon for easy recognition.
The favicon is important in a webpage as it provides a recognizable visual identity in browser tabs, 
enhancing brand visibility and user recognition, and it helps users quickly locate and return to the site.
  ![Favicon](doc/features/05-favicon.jpg)
  
- Landing page 
The landing page is now designed to feature 12 interactive charts, offering a dynamic and engaging user experience. Each chart provides insights into different aspects, such as data analytics, 
and trends, based on UN data. This interactive design allows visitors to delve into various United Nations datasets, enhancing their understanding through visual representations. 
The desktop version of the charts is developed using Python's Plotly library, while the mobile version, to maintain responsiveness, uses static images.
    ![Welcome Page](doc/features/06-landing.jpg)
    ![Welcome Page](doc/features/07-landing.jpg)
    ![Welcome Page](doc/features/08-landing.jpg)

- Search Bar 
Developed a search bar with predictive capabilities, enabling users to swiftly locate information. This feature organizes search results according to main themes (like energy, water, health) and sub-topics displayed on the homepage.
The predictive nature of the search bar suggests that it can anticipate the user's query, likely through algorithms that recognize patterns in user input and suggest relevant topics. The main themes like energy, water, 
and health represent broad areas of information, while the sub-topics provide more detailed categories within these areas. This organization aids in efficiently navigating and accessing specific information related to the displayed charts on the landing page.
    ![Search](doc/features/09-search.jpg)
    ![Search](doc/features/10-search.jpg)

- Interactive charts
Plotly, a graphing library is used to create interactive charts. Users have the flexibility to select a range of years between 2015 and 2022, enabling them to view data over this specific period.
Colour coding is employed for easy topic identification, with lighter shades of the same colour indicating the passage of years within each topic. This colour differentiation aids in visual distinction and understanding 
of data trends over time. The functionality to download charts as PNG files provides a convenient way to save and share visual data. 
The zoom-in/out feature enhances user interaction, allowing for a closer inspection or a broader view of the data presented in the charts.
    ![Chart](doc/features/11-chart.jpg)

- Back to the top button
A "back to top" button has been implemented to enable users to easily return to the top of the page at any time.
The button's function is to quickly take the user back to the top of the webpage, no matter where they are on the page. This feature is particularly useful for long webpages, as it saves the user from having to scroll manually all the way back to the top. It enhances the user experience by providing a convenient and time-saving way to access the top of the page, often where key navigation elements or important information is located.
    ![Back](doc/features/12-top.jpg)
  

## Existing Features

**Existing features:**
- Implemented a JavaScript feature that causes the navigation bar to shrink as the user scrolls down the page
- Integrated a JavaScript feature for predictive search functionality
- Implemented a JavaScript-based button to facilitate returning to the top of the page
- Developed the entire dataset using Plotly, Flask, and Python

## Technologies

The EcoInsight Dashboard website utilizes the following technologies:

- Figma for design.
- FontAwesome for icons.
- CSS for styling.
- HTML for content.
- JavaScript
- Flask as the framework.
- Python 3
- Visual Studio Code for development.
- GitHub for version control.
- ChatGPT for content creation.

Flask:
    ![Code](doc/code/code-01.jpg)
    ![Code](doc/code/code-02.jpg)

HTML:
    ![Code](doc/code/code-03.jpg) 

JS:
    ![Code](doc/code/code-04.jpg)     

## Validations

Autocomplete JS:
    ![Code](doc/validator/01-js.jpg)   

Navigation JS:    
    ![Code](doc/validator/02-js.jpg)   

Flask app:    
    ![Code](doc/validator/03-flask.jpg)   

## Design elements
   ![Palette](doc/palette.jpg) 
   ![Wireframes](doc/wireframes.jpg) 

## Learning Outcomes 

As a student utilizing the EcoInsight Dashboard, I have gained invaluable insights not only in environmental sustainability but also in the application of Python for data analysis and visualization. 
The dashboard's integration of Python, especially through its use of Flask and Plotly, has provided me with a practical understanding of how Python can be employed in web applications to handle complex datasets. 
Working with the dashboard has deepened my skills in Python programming, particularly in data manipulation, creating interactive charts, and web development. 
This hands-on experience has been essential in bridging the gap between theoretical knowledge and real-world application, making my learning journey 
in both environmental studies and Python programming highly rewarding and relevant.
   

## User Stories

1. **As a researcher,** I want to view and compare data on various sustainable development goals (SDGs) so I can understand the progress and challenges in different regions over the years.

2. **As a student,** I need a user-friendly interface to access data on global sustainability issues for my academic projects and research.

3. **As a policy analyst,** I require detailed visualizations of data related to health, economy, and environment to aid in policy making and evaluation.

4. **As an educator,** I look for interactive and informative resources to teach students about the importance of sustainable development and global challenges.

## User Flow

1. **Landing on the Homepage**
   - The user sees the header with navigation options and a search bar.
   - Reads a brief introductory paragraph about global challenges and sustainable development goals.

2. **Exploring Specific Topics**
   - Scrolls through the topics (like clean energy, clean water, decent work, etc.).
   - Selects a topic of interest, for example, 'Clean Energy'.

3. **Interacting with Data Visualizations**
   - Views the chart for the selected topic, with the option to use a slider to change the year.
   - Reads the accompanying text to understand the context of the data.

4. **Utilizing the Search Function**
   - Uses the search bar to find specific data or topics.
   - The search provides autocomplete suggestions.

5. **Accessing Additional Information**
   - Scrolls to the footer to find more resources, disclaimers, or to access the GitHub repository.

## Task Flow

1. **Selecting a Topic**
   - User clicks on a topic, such as 'Clean Energy'.
   - The page scrolls to the 'Clean Energy' section.

2. **Viewing and Interacting with Data**
   - User observes a bar chart comparing data across different years and countries.
   - Uses the slider to change the year and view corresponding data.

3. **Reading Supplementary Information**
   - User reads the title and paragraph explaining the chart to gain context.
   - If needed, views the chart image for mobile optimization.

4. **Navigating to Other Sections**
   - User can either scroll manually to other topics or use the navigation bar to jump to a specific section, like 'Clean Water' or 'Decent Work'.

5. **Utilizing Search and Footer Links**
   - If the user needs specific information, they utilize the search bar.
   - For additional resources or disclaimers, the user checks the footer.

### Additional Notes

- The website is designed to make complex data accessible and understandable to a diverse audience, from students to professionals.
- Interactivity with the data (through sliders and charts) enhances user engagement.
- The search function and well-organized content improve the user experience by making navigation straightforward and intuitive.

## Testing

The website has been thoroughly tested on various devices and browsers:

- Mobile (iPhone 14)
- Smaller laptop MacBook Air
- iMac
- Chrome
- Firefox
- Safari

## Usability Testing

- User 1: High School Student
Testing Focus: Navigational ease and educational value.
Feedback: Found the navigation intuitive and the educational content highly accessible. Suggested adding more interactive quizzes to enhance the learning experience.

- User 2: Environmental Researcher
Testing Focus: Depth and accuracy of data visualization.
Feedback: Appreciated the comprehensive data presentation but recommended including more detailed filters for customized data analysis.

- User 3: Web Developer (Familiar with Python)
Testing Focus: Technical performance and Python integration.
Feedback: Impressed with the smooth integration of Flask and Plotly but suggested optimizing load times for complex graphs.

- User 4: Graphic Designer
Testing Focus: Aesthetic appeal and user interface design.
Feedback: Praised the dashboard's visual design but recommended more contrast in color schemes for better readability.

- User 5: University Professor
Testing Focus: Educational tool efficacy and interactivity.
Feedback: Found the dashboard extremely useful as an educational tool. Suggested adding more interactive elements like sliders for time-range selection to engage students better.

Each user brought unique perspectives to the usability testing, providing valuable insights into different aspects of the EcoInsight Dashboard. This feedback, encompassing both technical and user experience aspects, offers a comprehensive understanding of the dashboard's functionality and areas for improvement.

## Credits

- Written content by ChatGPT
- Iconography [here](https://fontawesome.com/v4/icons/)
- Data: The information presented on this website has been sourced from The Sustainable Development Goals Report 2023,
as published by the United Nations.



