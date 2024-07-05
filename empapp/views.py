from django.shortcuts import render,redirect

# Create your views here.

from empapp.models import Category,Employee

from empapp.forms import CategoryForm,EmployeeForm

from django.views.generic import View


class CategoryCreateView(View):

    def get(self,request,*args,**kwrags):

        form_instance=CategoryForm()

        return render(request,"category_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=CategoryForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("category-add")
        else:
            return render(request,"category_add.html",{"form":form_instance})

class EmployeeCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=EmployeeForm()

        return render(request,"employee_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("employee-add")
        else:
            return render(request,"employee_add.html",{"form":form_instance})

class EmployeeListView(View):

    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all()

        all_cats=Category.objects.all()

        return render(request,"employee_list.html",{"data":qs,"category":all_cats})

class CategoryFilterView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        all_cats=Category.objects.all()

        category=Category.objects.get(id=id)

        employee=Employee.objects.filter(category_name=category)

        return render(request,"category_filter.html",{"data":employee,"category":all_cats})


class EmployeeDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id)

        return render(request,"employee_detail.html",{"data":qs})

class EmployeeUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        emp_object=Employee.objects.get(id=id)

        form_instance=EmployeeForm(instance=emp_object)

        return render(request,"employee_update.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id)

        form_instance=EmployeeForm(request.POST,instance=qs)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("employee-list")
        
        else:

            return render(request,"employee_update.html",{"form":form_instance})

class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Employee.objects.get(id=id).delete()

        return redirect("employee-list")
    