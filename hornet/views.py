from django.shortcuts import render


def home(request):
    social_links = [
        {'name': 'cines91', 'link': 'https://www.facebook.com/cines91', 'site': 'Facebook'},
        {'name': 'ilu2112', 'link': 'https://github.com/ilu2112', 'site': 'GitHub'},
        {'name': 'coding-buzz', 'link': 'https://github.com/coding-buzz', 'site': 'GitHub'},
        {'name': 'marcinskiba91', 'link': 'https://www.linkedin.com/in/marcinskiba91', 'site': 'LinkedIn'},
        {'name': 'marcin', 'link': 'mailto:marcin@coding.buzz', 'site': 'coding.buzz'}
    ]
    skills = [
        {'name': 'Java SE/EE', 'level': 90},
        {'name': 'Java Web Frameworks', 'level': 90},
        {'name': 'SAP Hybris', 'level': 50},
        {'name': 'Python', 'level': 90},
        {'name': 'Python Web Frameworks', 'level': 90},
        {'name': 'Ruby on Rails', 'level': 45},
        {'name': 'JavaScript ES5/ES6 + Node', 'level': 75},
        {'name': 'JavaScript MVC Frameworks', 'level': 65},
        {'name': 'HTML, CSS & SCSS', 'level': 90},
        {'name': 'Algorithms & Data Structures', 'level': 95},
        {'name': 'SQL', 'level': 80}
    ]
    skills = sorted(skills, key=lambda s: s['name'])
    context = {
        'social_links': social_links,
        'skills': skills
    }
    return render(request, 'pages/home.html', context)
