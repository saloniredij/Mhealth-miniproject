from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def bmi(request):
    return render(request, 'bmi.html')

def symptom(request):
    if request.method == "POST":
        cough = request.POST['cough']
        fever = request.POST['fever']
        common = request.POST['common']
        if(cough == 'not' and fever == 'not' and common == 'not'):
            messages.info(request, 'You are healthy. Exercise daily and stay fit.')
            return redirect('symptom')
        elif (cough == 'candc' and fever == 'not' and common == 'not'):
            messages.info(request,'Common cold and Cough')
            return redirect('symptom')
        elif ((cough == 'candc' or cough == 'not' or cough == 'drysore') and (fever == 'not' or fever == 'highfever' or fever == 'normalfever') and common == 'diarrheoa' ):
            messages.info(request, 'Food Poisoning')
            return redirect('symptom')
        elif (cough == 'sputum'):
            messages.info(request, 'Tuberculosis')
            return redirect('symptom/')
        elif (cough != 'sputum' and fever == 'pattern' and common == 'diarrheoa'):
            messages.info(request, 'Typhoid')
            return redirect('symptom/')
        elif (cough == 'sore throat' and (fever == ' not' or fever == 'normalfever') and common == 'not'):
            messages.info(request, 'Throat Infection')
            return redirect('symptom/')
        elif (cough != 'sputum' and (common == 'yellow' or common == 'all')):
            messages.info(request, 'Jaundice')
            return redirect('symptom/')
        elif (cough == 'candc' and (fever == 'normalfever' or fever == 'highfever') and common == 'diarrheoa'):
            messages.info(request, 'Viral')
            return redirect('symptom/')
        
        
        else:
            messages.info(request, 'Uh-oh!Disease not found.')
            return redirect('symptom')

    else:
        return render(request, 'symptom.html')
