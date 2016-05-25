from django.shortcuts import render


def home(request):
    skills = [
        {'name': 'Java SE/EE', 'level': 90},
        {'name': 'Java Web Frameworks', 'level': 90},
        {'name': 'SAP Hybris', 'level': 60},
        {'name': 'Python', 'level': 85},
        {'name': 'Django', 'level': 75},
        {'name': 'Flask', 'level': 40},
        {'name': 'JavaScript', 'level': 70},
        {'name': 'jQuery', 'level': 80},
        {'name': 'Backbone JS', 'level': 45},
        {'name': 'React JS', 'level': 45},
        {'name': 'Node JS', 'level': 45},
        {'name': 'Ember', 'level': 35},
        {'name': 'SQL/MySQL', 'level': 80},
        {'name': 'C++', 'level': 70},
        {'name': 'Ruby on Rails', 'level': 50},
        {'name': 'HTML, CSS & SCSS', 'level': 90},
        {'name': 'Algorithms & Data Structures', 'level': 95},
        {'name': 'Linux', 'level': 75},
        {'name': 'Application Design', 'level': 80},
        {'name': 'UI/UX Design', 'level': 35},

    ]
    return render(request, 'pages/home.html', context={'skills': skills})
