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
print(child.full_name) 

# шаг 6
from datacenter.models import Mark     
marks = Mark.objects.filter(schoolkid=child) 
print(marks)

