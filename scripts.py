from datacenter.models import Schoolkid

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


