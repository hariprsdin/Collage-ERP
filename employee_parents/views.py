from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import EmployeeParent


def parent_list(request):
    parents = EmployeeParent.objects.all()
    return render(request, 'employee_parents/parent_list.html', {'parents': parents})


def parent_detail(request, pk):
    parent = get_object_or_404(EmployeeParent, pk=pk)
    return render(request, 'employee_parents/parent_detail.html', {'parent': parent})


def parent_form(request, pk=None):
    parent = get_object_or_404(EmployeeParent, pk=pk) if pk else None

    if request.method == 'POST':
        employee_name = request.POST.get('employee_name', '').strip()
        employee_id = request.POST.get('employee_id', '').strip()
        father_name = request.POST.get('father_name', '').strip()
        mother_name = request.POST.get('mother_name', '').strip()
        guardian_name = request.POST.get('guardian_name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        address = request.POST.get('address', '').strip()
        relation = request.POST.get('relation', 'Parent').strip()

        if not employee_name or not employee_id:
            messages.error(request, 'Employee name and employee ID are required.')
            return render(request, 'employee_parents/parent_form.html', {'parent': parent})

        parent_data = {
            'employee_name': employee_name,
            'employee_id': employee_id,
            'father_name': father_name,
            'mother_name': mother_name,
            'guardian_name': guardian_name,
            'phone': phone,
            'email': email,
            'address': address,
            'relation': relation,
        }

        if parent:
            for key, value in parent_data.items():
                setattr(parent, key, value)
            parent.save()
            messages.success(request, 'Employee parent record updated successfully.')
        else:
            EmployeeParent.objects.create(**parent_data)
            messages.success(request, 'Employee parent record created successfully.')
        return redirect('employee_parents:parent_list')

    return render(request, 'employee_parents/parent_form.html', {'parent': parent})


def parent_delete(request, pk):
    parent = get_object_or_404(EmployeeParent, pk=pk)
    parent.delete()
    messages.success(request, 'Employee parent record deleted successfully.')
    return redirect('employee_parents:parent_list')
