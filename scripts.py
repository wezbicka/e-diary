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
