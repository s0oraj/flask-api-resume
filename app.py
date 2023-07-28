from flask import Flask, jsonify

app = Flask(__name__)

# Your resume data in JSON format
Resume = {
    "first_name": "Suraj",
    "last_name": "Singh",
    "resume_name": "first one",
    "level": "internship",
    "profession": "Final Year Btech Student | Android Developer| Researcher| IEEE | Machine Learning Engineer | #Global_Rank_228 Amazon ML Challenge",
    "email": "hotmailsuraj@gmail.com",
    "phone_number": "8408068178",
    "city": "Bhubaneshwar",
    "country": "India",
    "pincode": "752054",
    "github": "https://github.com/s0oraj",
    "twitter": "twitter",
    "linkedin": "https://www.linkedin.com/in/s0oraj/",
    "portfolio_link": "https://upgrad-resume-assignment-cgu.vercel.app/",
    "languages": "english,hindi",
    "summary": "Btech Student with experience in full stack development and machine learning",
    "accomplishment": "Ranked 228 globally out of 30,000+ teams in the Amazon ML Challenge Hackathon 2023",
    "education": [
        {
            "education_id":1,
            "school_name": "C. V. Raman Global University",
            "school_location": "Bhubaneshwar",
            "degree": "Btech",
            "field_of_study": "Computer Science and Information Technology",
            "degree_start_date": "2022-12-09",
            "degree_end_date": "2022-12-09",
            "current_attend_here": 0,
            "bulletPoints":[]
        }
    ],
    "work_experience": [
        {
            "work_id":1,
            "job_title": "Undergraduate Researcher- Machine Learning",
            "company_name": "C. V. Raman Global University",
            "company_location": "Bhubaneshwar",
            "start_date": "2022-12-11",
            "end_date": "2023-07-07",
            "Description": "",
            "currently_work_here": 1,
            "bulletPoints":["Distributed Denial Of Service (DDoS) detection: Utilizing Deep neural networks to analyze network traffic, distinguish normal behavior from attack vectors such as SYN, floods, UDP amplification, HTTP floods, with 91 % accuracy",
                            "Early Stage Glaucoma Detection: Developing an Extreme Learning Machine with Convolutional Neural Networks (CNN) and Transfer Learning for Glaucoma disease prevention and preserving vision with 96% accuracy.", 
                            "Alzheimer’s disease Diagnostic: Hippocampus Detection using advanced image preprocessing techniques,Discrete Wavelet Transform for early detection and diagnosis of Alzheimer’s Decease with 98% accuracy"]
        },
        {
            "work_id":2,
            "job_title": "Mobile Application Developer- Android",
            "company_name": "Roboslog Pvt Ltd",
            "company_location": "Delhi",
            "start_date": "2022-06-16",
            "end_date": "2022-08-20",
            "Description": "",
            "currently_work_here": 0,
            "bulletPoints":["Engineered scalable E-commerce transport project with client-side Agent and Driver apps, utilizing XML and Java.",
                            "Efficiently managed server API calls with JSON-POST/GET and implemented server-side using PHP and MySql.",
                            "Integrated Razor-Pay for secure payment processing with payment layout, OTP verification, and success/failure pages.",
                            "Administrated transaction IDs and payment distribution for admin, agent, and driver to ensure security and scalability.",
                            "Utilized Firebase Realtime Database and Firestore for data storage, synchronization, and authentication."]
        }
    ],
    "projects": [
        {
            "project_id":1,
            "project_name": "Twitter Clone - Full Web Stack Application",
            "project_link": "https://github.com/s0oraj/TweetClone",
            "description": "",
            "bulletPoints":["Built a Twitter-like platform using Spring Boot, ReactJS, & AWS S3 for image uploads.",
                            "Implemented secure authentication with JWT, data mapping with ModelMapper, and optimized REST APIs for speed",
                            "Designed the UI with Tailwind CSS, enabled file uploads with React Dropzone, and managed state using Redux Toolkit",
                            "Leveraged GraphQL to optimize data fetching and manipulation, ensuring efficiency and optimization"]
        },
        {
            "project_id":2,
            "project_name": "Animus - Social Media App",
            "project_link": "https://github.com/s0oraj/Animus",
            "description": "",
            "bulletPoints":["Developed a Social Media Platform for users to make friends with the Animus app.",
                            "Utilized Advanced Encryption Standard (AES) algorithm to make chats End-to-End Encrypted (E2EE)).",
                            "Pioneered an in-app AI Voice Assistant allowing users to navigate the app using voice commands, via Alan-AI.",
                            "Created Avatar Creator functionality using Google ML Kit and OpenCV for image segmentation and cartoonization.",
                            "Features: Post feed, follow accounts, like/comment/share, chat, Notifications, Profile, Search, and Google Signup.",
                            ]
        }
    ],
    "skills": [
        {
            "skills_id":1,
            "top_technical_skills": "React.js, Android Studio",
            "technical_skills": "Keras, OpenCV, scikit-learn, PIL, AutoMl, GitHub, Django, Flask, Anaconda, NLP, Tensorflow",
            "non_technical_skills": "Python, Java, C, C++, , C#, JavaScript",
            "softwares": "VSCode, Eclipse, Google Colab, Android Studio, Flutter, Jupyter Notebook, Postman, Pytorch",
            "bulletPoints":[]
        }
    ],
    "certificates": [
        {
            "certi_id": 1,
            "certi_name": "Android Application Development",
            "certi_link": "https://www.coursera.org/account/accomplishments/specialization/certificate/Y5UG3LY7FCM8",
            "certi_start_date": "2022-12-09",
            "certi_end_date": "2022-12-09",
            "currently_pursuing": 0,
            "bulletPoints":[]
        },
        {
            "certi_id":2,
            "certi_name": "Google IT Support Professional Certificate",
            "certi_link": "https://www.coursera.org/account/accomplishments/specialization/certificate/UVHM3MYJHP46",
            "certi_start_date": "2022-12-09",
            "certi_end_date": "2022-12-09",
            "currently_pursuing": 0,
            "bulletPoints":[]
        }
    ]
}

# Define a route to handle the GET request and return your resume data
@app.route('/api/resume', methods=['GET'])
def get_resume():
    return jsonify(Resume)

if __name__ == '__main__':
    app.run(debug=True)
