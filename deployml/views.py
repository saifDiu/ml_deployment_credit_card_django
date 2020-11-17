from django.shortcuts import render
from django.shortcuts import render
import pickle
# Create your views here.

def home(request):

    model = pickle.load(open('model_pickle', 'rb'))



    account_details_list = []
    account_details_list.append(request.POST.get('LIMIT_BAL'))
    account_details_list.append(request.POST.get('EDUCATION'))
    account_details_list.append(request.POST.get('MARRIAGE'))
    account_details_list.append(request.POST.get('AGE'))
    account_details_list.append(request.POST.get('PAY_1'))
    account_details_list.append(request.POST.get('BILL_AMT1'))
    account_details_list.append(request.POST.get('BILL_AMT2'))
    account_details_list.append(request.POST.get('BILL_AMT3'))
    account_details_list.append(request.POST.get('BILL_AMT4'))
    account_details_list.append(request.POST.get('BILL_AMT5'))
    account_details_list.append(request.POST.get('BILL_AMT6'))
    account_details_list.append(request.POST.get('PAY_AMT1'))
    account_details_list.append(request.POST.get('PAY_AMT2'))
    account_details_list.append(request.POST.get('PAY_AMT3'))
    account_details_list.append(request.POST.get('PAY_AMT4'))
    account_details_list.append(request.POST.get('PAY_AMT5'))
    account_details_list.append(request.POST.get('PAY_AMT6'))

    #print(account_details_list)

    ans = model.predict([account_details_list])
    context = {'ans':ans}
    return render(request, 'deployml/home.html', context)
