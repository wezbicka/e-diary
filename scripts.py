from datacenter.models import Schoolkid
from datacenter.models import Mark 
from datacenter.models import Chastisement  
# шаг 4

students = Schoolkid.objects.all()
print(students)

# шаг 5
# Ivan = Schoolkid.objects.filter(full_name__contains="Фролов")
# print(Ivan) 
"""<QuerySet [<Schoolkid: Фролов Каллистрат Арсеньевич 4А>, 
<Schoolkid: Фролов Иван Григорьевич 6А>, 
<Schoolkid: Моисеев Терентий Фролович 6В>, 
<Schoolkid: Горбачев Агап Фролович 9В>]>"""
# i = Ivan.filter(full_name__contains="Иван")
# child = Ivan.filter(full_name__contains="Иван")[0]
child = Schoolkid.objects.filter(full_name__contains="Фролов Иван")[0]
#child_1 = Schoolkid.objects.get(full_name__contains="Фролов Иван")  
# лучший вариантдля этого шага
print(child.full_name) 

# шаг 6
from datacenter.models import Mark     
marks = Mark.objects.filter(schoolkid=child) 
print(marks)

# шаг 7
bad_marks = Mark.objects.filter(schoolkid=child, points__lte=3)  
print(bad_marks) 
"""<QuerySet [<Mark: 2 Фролов Иван Григорьевич>, 
<Mark: 2 Фролов Иван Григорьевич>, 
<Mark: 2 Фролов Иван Григорьевич>, 
<Mark: 3 Фролов Иван Григорьевич>, 
<Mark: 2 Фролов Иван Григорьевич>, 
<Mark: 2 Фролов Иван Григорьевич>, <Mark: 3 Фролов Иван Григорьевич>,
<Mark: 3 Фролов Иван Григорьевич>, <Mark: 3 
Фролов Иван Григорьевич>, <Mark: 3 Фролов Иван Григорьевич>, 
<Mark: 3 Фролов Иван Григорьевич>, <Mark: 3 Фролов Иван Григорьевич>, 
<Mark: 3 Фролов Иван Григорьевич>, <Mark: 2 Фролов Иван Григорьевич>, 
<Mark: 2 Фролов Иван Григорьевич>, <Mark: 2 Фролов Иван Григорьевич>, 
<Mark: 2 Фролов Иван Григорьевич>, <Mark: 2 Фролов Иван Григорьевич>, 
<Mark: 3 Фролов Иван Григорьевич>, <Mark: 3 Фролов Иван Григорьевич>, 
'...(remaining elements truncated)...']>
"""
# шаг 8
Mark.objects.filter(schoolkid=child, points__lte=3).count() # 263
mark = Mark.objects.filter(schoolkid=child, points__lte=3)[0]
print(mark) # 2 Фролов Иван Григорьевич
mark.points = 5
mark.save()
print(mark) #5 Фролов Иван Григорьевич
Mark.objects.filter(schoolkid=child, points__lte=3).count() # 262


# шаг 10
def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=child, points__lte=3)
    for mark in bad_marks:
        mark.points = 5
        mark.save()
   # mark.update()

# шаг 12

сhastisements = Chastisement.objects.filter(schoolkid=child) 
print(сhastisements)

# шаг 13
сhastisements.delete()

# шаг 14

def remove_chastisements(schoolkid):
    сhastisements = Chastisement.objects.filter(schoolkid=schoolkid) 
    сhastisements.delete()

# шаг 15

from datacenter.models import Lesson 
lesson = Lesson.objects.all()
print(lesson)
"""<QuerySet [<Lesson: Изобразительное искусство 1А>, 
<Lesson: Чтение 1А>, <Lesson: 
Труд 1А>, <Lesson: Чтение 1А>, <Lesson: Математика 1А>, 
<Lesson: Математика 1А>, 
<Lesson: Чистописание 1А>, <Lesson: Математика 1А>, 
<Lesson: Музыка 1А>, <Lesson: Русский язык 1А>, <Lesson: Русский язык 1А>,
 <Lesson: Природоведение 1А>, <Lesson: Физкультура 1А>, <Lesson: Труд 1А>, 
 <Lesson: Чистописание 1А>, <Lesson: Музыка 1А>, 
 <Lesson: Изобразительное искусство 1А>, <Lesson: Природоведение 1А>, 
 <Lesson: Физкультура 1А>, <Lesson: Физкультура 1А>, '...(remaining elements truncated)...']> """

 # шаг 16

child_lesson = Lesson.objects.filter(year_of_study=6, group_letter="А")
print(child_lesson)
"""<QuerySet [<Lesson: Математика 6А>, 
<Lesson: Технология 6А>, 
<Lesson: Основы безопасности жизнедеятельности (ОБЖ) 6А>, 
<Lesson: Русский язык 6А>, <Lesson: История 6А>, 
<Lesson: Математика 6А>, <Lesson: Русский язык 6А>, 
<Lesson: Музыка 6А>, 
<Lesson: Физкультура 6А>, 
<Lesson: Обществознание 6А>, 
<Lesson: Краеведение 6А>, 
<Lesson: Технология 6А>, 
<Lesson: Изобразительное искусство 6А>, 
<Lesson: Краеведение 6А>, 
<Lesson: География 6А>, 
<Lesson: Литература 6А>, 
<Lesson: Иностранный язык 6А>, 
<Lesson: Физкультура 6А>, 
<Lesson: История 6А>, 
<Lesson: География 6А>, '...(remaining elements truncated)...']>"""

# шаг 17

child_math_lessons = Lesson.objects.filter(year_of_study=6, group_letter="А", subject__title="Математика")
print(child_math_lessons)
"""<QuerySet [<Lesson: Математика 6А>, 
<Lesson: Математика 6А>,
 <Lesson: Математика 6А>,
  <Lesson: Математика 6А>,
   <Lesson: Математика 6А>, <Lesson
   : Математика 6А>,
    <Lesson: Математика 6А>,
     <Lesson: Математика 6А>,
      <Lesson: Математика 6А>,
       <Lesson: Математика 6А>, <Lesson: Математика 6А>,
        <Lesson: Математика 6А>, <Lesson: Математика 6А>, <Lesson: Математика 6А>,
         <Lesson: Математика 6А>, <Lesson: Математика 6А>, 
<Lesson: Математика 6А>,
 <Lesson: Математика 6А>, <Lesson: Математика 6А>,
  <Lesson: Математика 6А>, '...(remaining elements truncated)...']> """

  # шаг 18

from datacenter.models import Commendation
lesson = child_math_lessons[0]
date = lesson.date
subject = lesson.subject
teacher = lesson.teacher
Commendation.objects.create(
    text="Хвалю",
    created=date,
    schoolkid=child,
    subject=subject,
    teacher=teacher
)

# шаг 19
import random


def create_commendation(child_name, subject):
    schoolkid = get_kid_by_name(child_name)
    child_lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study, 
        group_letter=schoolkid.group_letter,
        subject__title=subject,
    ).order_by('-date').first()
    commendations = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!",
    ]
    commendation = random.choice(commendations)
    Commendation.objects.create(
        text=commendation,
        created=child_lesson.date,
        schoolkid=schoolkid,
        subject=child_lesson.subject,
        teacher=child_lesson.teacher
    )

# шаг 20

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def get_kid_by_name(child_name: str) -> Schoolkid:
    try:
        child = Schoolkid.objects.get(full_name__contains=child_name)
    except MultipleObjectsReturned:
        print("Найдено больше одного ученика")
    except ObjectDoesNotExist:
        print("Не найдено учеников с таким именем")
    return child
