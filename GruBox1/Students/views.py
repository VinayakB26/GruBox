from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from .models import Student, SubjectMarks, SubjectName
from django.db.models import QuerySet,Max
import operator

def home(request):
     return render(request,'home.html')

def StudentDetails(request):
    student=Student.objects.all()
    subject=SubjectMarks.objects.all()
    sub_name=SubjectName.objects.all()
    
    for studs in student:
        if studs.RollNo== int(request.user.username):
            sub = subject.filter(RollNo=studs.RollNo)
            stud = student.filter(RollNo=studs.RollNo)
            
    print(sub_name.values())
    return render (request ,'student.html', {'student':stud[0], 'subject': sub , 'SubjectName':sub_name} )
    #return HttpResponse(stud.RollNo)
    
def ClassTopper(request):
    student=Student.objects.all()
    
    query = SubjectMarks.objects.all().query
    query.group_by = ['Class']
    query = QuerySet(query=query, model=SubjectMarks)
    
    result = dict()
    for i in query:
        if  i.RollNo in result.keys():
            result[i.RollNo]+=i.Marks
        else:
            result[i.RollNo]=i.Marks
    RollNo = max(result.items(), key=operator.itemgetter(1))[0]
    
    return render (request,'topper.html',{'topper' :student.filter(RollNo=RollNo),'TotalMarks':result[RollNo]})

def SubjectTopper (request):
    query = SubjectMarks.objects.all()
    sub_name=SubjectName.objects.all()
#    stud = Student.objects.all()
#    result=dict()
##    for i in query:
##        if i.SubjectId in result.keys():
##            if (result[i.SubjectId]<i.Marks):
##                result[i.SubjectId]=i.Marks
##                result['Topper'+str(i.SubjectId)]=i.RollNo
##        else:
##            result[i.SubjectId]=i.Marks
##            result['Topper'+str(i.SubjectId)]=i.RollNo
#    #query = SubjectName.objects.all()
#    res=[]
#    for i in result.keys():
#        que= query.filter(SubjectId=i)
#        res.append(que[0].SubjectName)
#        res.append(result[i])
#        #res.append()
#    for i in query:
#        request_values = query.filter(SubjectId=i.SubjectId) \
#                 .values('SubjectId') \
#                 .annotate(max_marks=Max('Marks'))
#   
    count_tot=len(list(SubjectMarks.objects.values_list('RollNo', flat=True)))
    dist_count =len( list(set(SubjectMarks.objects.values_list('RollNo', flat=True))))
    res=[]
    count=0
    for i in query :
        sub=query.filter(SubjectId = i.SubjectId)
        res.append(query.filter(Marks=sub.aggregate(Max('Marks'))['Marks__max'])[0])
        count=count+1
        if count*dist_count == count_tot:
            break
    return render (request,'subjecttopper.html',{'res':res, 'SubName': sub_name})

    
    
    
