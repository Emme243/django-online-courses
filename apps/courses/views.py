from django.shortcuts import render


# Create your views here.
def course_list(request):
    courses = [
        {
            "id": 1,
            "level": "beginner",
            "rating": 4.7,
            "title": "Python | From Zero to Hero",
            "instructor": "Alison Walsh",
            "course_image": "images/curso_1.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/women/68.jpg",
        },
        {
            "id": 2,
            "level": "intermediate",
            "rating": 4.9,
            "title": "Python | From Hero to Ñero",
            "instructor": "Alison Walsh",
            "course_image": "images/curso_2.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/women/69.jpg",
        },
    ]
    return render(request, "courses/course_list.html", {"courses": courses})


def course_detail(request):
    course = {
        "title": "Django Apps",
        "link": "course_lessons",
        "image": "images/curso_2.jpg",
        "info": {
            "lessons": 79,
            "duration": 8,
            "instructor": "Ricardo",
            "instructor_image": "https://randomuser.me/api/portraits/men/69.jpg",
        },
        "content": [
            {
                "id": 1,
                "name": "Introduction to Course",
                "lessons": [
                    {"name": "What is this about?", "type": "video"},
                    {"name": "How to use the platform?", "type": "article"},
                ],
            }
        ],
    }
    return render(request, "courses/course_detail.html", {"course": course})


def course_lessons(request):
    lesson = {
        "title": "Django Apps",
        "progress": 30,
        "content": [
            {
                "id": 1,
                "name": "Introduction to Course",
                "total_lessons": 6,
                "complete_lessons": 3,
                "lessons": [
                    {"name": "What is this about?", "type": "video"},
                    {"name": "How to use the platform?", "type": "article"},
                ],
            }
        ],
    }
    return render(request, "courses/course_lessons.html", {"lesson": lesson})
