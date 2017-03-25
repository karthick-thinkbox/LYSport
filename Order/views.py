from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic.list import ListView
from .models import Order
from .forms import new_ord
from django.template import Template,context
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from  django.db.models import Q

class Orderlist(ListView):
    model=Order
    template_name='home.html'
    
    def post(self ,request,*args,**kwargs):
        ordid=request.POST.get('filter' ,'')
        if ordid:
            
            try:
                row_id=Order.objects.get(order_id=ordid).id
                return redirect('Deatail_page',pk=row_id,currency="USD")
            except Exception as e:
                return render(request,self.template_name,{"Error":str(e) ,"object_list":Order.objects.all()})
        else:
            return render(request,self.template_name,{"Error":"Please Input Order#" ,"object_list":Order.objects.all()})
            
        
    def get_queryset(self):
        
        sort=self.request.GET.get('sortchoice' ,'')
        order_pg=self.request.GET.get('order_pg' ,'')
        qs=super(Orderlist,self).get_queryset()
        
    
        if sort=='' :
            
            return Order.objects.all()
        
        elif sort and order_pg=='asc' :
            return Order.objects.all().order_by(sort)
        elif sort and order_pg=='dsc' :
            return Order.objects.all().order_by('-'+sort)
        
        
class detail(DetailView):
        model=Order
        template_name='detail_page.html'
        def get_context_data(self ,**kwargs):
            context=super(detail,self).get_context_data(**kwargs)
            cur_code=self.kwargs['currency']
            if cur_code=='INR':
                cost=Order.objects.get(id=self.kwargs['pk']).cost_price 
                context['Rupees']=cost*66
                context['cur_code']='INR'
            return context

def logout_page(request):
    logout(request)
    return render (request,'logout.html')
@login_required(login_url='login_page')
def neworeder(request):
    if request.method=="POST":
        ordbox=new_ord(request.POST)
        if ordbox.is_valid():
            ord_id=ordbox.cleaned_data['order_id']
            ord_status=ordbox.cleaned_data['order_stat']
            ord_source=ordbox.cleaned_data['order_source']
            ord_name=ordbox.cleaned_data['prod_name']
            ord_cost=ordbox.cleaned_data['cost_price']
            ord_url=ordbox.cleaned_data['prod_url']
            
            try:
                tmp=Order(order_id=ord_id,
                          order_stat=ord_status,
                          order_source=ord_source,
                          prod_name=ord_name,
                          cost_price=ord_cost,
                          prod_url=ord_url)
                          
                tmp.save()
                form=new_ord()
                return render(request,'neworder.html',{'form':form ,"flg":"Done","ordid":ord_id})
                
            except Exception as e:
                form=new_ord()
                return render(request,'neworder.html',{'form':form ,"Error":str(e)})
                
            
        else:
            form=new_ord()
            return render(request,'neworder.html',{'form':form ,"Error":"Validation"})
            
        
    else:
        form=new_ord()
        return render(request,'neworder.html',{'form':form})
        