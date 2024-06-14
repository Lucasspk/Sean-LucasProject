from django.shortcuts import render, redirect, get_object_or_404
from .models import CPU, GPU, PSU, Motherboard
from .forms import GPUWeightForm, CPUWeightForm, PSUWeightForm, MotherboardWeightForm, ComponentSelectionForm


# Create your views here.
def BootstrapFilterView(request):
    return render(request, "bootstrap_form.html",)

def calculate_points_gpu(gpu, rasterization_weight, raytracing_weight, value_weight):
    rasterization_points = ((gpu.average_fps() * rasterization_weight)/138)*(1-value_weight)
    raytracing_points = ((gpu.average_rt_fps() * raytracing_weight)/296)*(1-value_weight)
    value_points = value_weight * ((gpu.average_fps()* rasterization_weight+gpu.average_rt_fps()* raytracing_weight)/gpu.price)*4
    return (rasterization_points + raytracing_points) + value_points


def calculate_points_cpu(cpu, performance_weight, gaming_weight, value_weight):
    performance_points = performance_weight * cpu.appscore
    gaming_points = gaming_weight * (cpu.score1080 + cpu.score1440)/2
    value_points = value_weight*(gaming_points + performance_points)/cpu.price*5
    return (1-value_weight)*(performance_points + gaming_points) + value_points  # Adjust this calculation as needed

def calculate_points_psu(psu, efficiency_weight):
    return (psu.watts * efficiency_weight)  # Adjust this calculation as needed

def calculate_points_motherboard(motherboard, feature_weight):
    return 0  # Adjust this calculation as needed


def select_component(request):
    if request.method == 'POST':
        form = ComponentSelectionForm(request.POST)
        if form.is_valid():
            component_type = form.cleaned_data['component_type']
            return redirect('create_component', component_type=component_type)
    else:
        form = ComponentSelectionForm()
    return render(request, 'select_component.html', {'form': form})

def create_component(request, component_type):
    if component_type == 'gpu':
        form_class = GPUWeightForm
        model_class = GPU
        calculate_points = calculate_points_gpu
    elif component_type == 'cpu':
        form_class = CPUWeightForm
        model_class = CPU
        calculate_points = calculate_points_cpu
    elif component_type == 'psu':
        form_class = PSUWeightForm
        model_class = PSU
        calculate_points = calculate_points_psu
    elif component_type == 'motherboard':
        form_class = MotherboardWeightForm
        model_class = Motherboard
        calculate_points = calculate_points_motherboard
    else:
        return redirect('select_component')

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            weighting_value = form.cleaned_data.get('rasterization_weight', 1) if component_type == 'gpu' else \
                              form.cleaned_data.get('performance_weight', 1) if component_type == 'cpu' else \
                              form.cleaned_data.get('efficiency_weight', 1) if component_type == 'psu' else \
                              form.cleaned_data.get('feature_weight', 1)
            raytracing_weight = form.cleaned_data.get('raytracing_weight', 1) if component_type == 'gpu' else 0
            value_weight = form.cleaned_data.get('value_weight', 1) if component_type == 'gpu' else form.cleaned_data.get('value_weight', 1) if component_type == 'gpu' else 0
            gaming_weight = form.cleaned_data.get('gaming_weight', 1) if component_type == 'cpu' else 0
            max_price = form.cleaned_data.get('max_price', None)

            # Calculate points for existing objects
            objects = model_class.objects.all()
            if max_price is not None:
                objects = objects.filter(price__lte=max_price)
            objects_with_points = [{
                'object': obj,
                'points': calculate_points(obj, weighting_value, raytracing_weight, value_weight) if component_type == 'gpu' else calculate_points(obj, weighting_value, gaming_weight, value_weight) if component_type == 'cpu' else calculate_points(obj, weighting_value)
            } for obj in objects]
            # Sort objects by points
            sorted_objects = sorted(objects_with_points, key=lambda x: x['points'], reverse=True)
            return render(request, 'component_list.html', {'objects': sorted_objects, 'component_type': component_type})
    else:
        form = form_class()

    return render(request, 'create_component.html', {'form': form, 'component_type': component_type})

def component_list(request):
    component_type = request.GET.get('component_type', 'gpu')
    weighting_value = float(request.GET.get('weighting_value', 1))

    if component_type == 'gpu':
        model_class = GPU
        calculate_points = calculate_points_gpu
    elif component_type == 'cpu':
        model_class = CPU
        calculate_points = calculate_points_cpu
    elif component_type == 'psu':
        model_class = PSU
        calculate_points = calculate_points_psu
    elif component_type == 'motherboard':
        model_class = Motherboard
        calculate_points = calculate_points_motherboard
    else:
        model_class = GPU  # Default to GPU
        calculate_points = calculate_points_gpu

    objects = model_class.objects.all()
    objects_with_points = [{
        'object': obj,
        'points': calculate_points(obj, weighting_value)
    } for obj in objects]
    sorted_objects = sorted(objects_with_points, key=lambda x: x['points'], reverse=True)

    return render(request, 'component_list.html', {'objects': sorted_objects, 'component_type': component_type})

def gpu_detail(request, pk):
    gpu = get_object_or_404(GPU, pk=pk)
    return render(request, 'gpu_detail.html', {'gpu': gpu})

def cpu_detail(request, pk):
    cpu = get_object_or_404(CPU, pk=pk)
    return render(request, 'cpu_detail.html', {'cpu': cpu})

def psu_detail(request, pk):
    psu = get_object_or_404(PSU, pk=pk)
    return render(request, 'psu_detail.html', {'psu': psu})

def motherboard_detail(request, pk):
    motherboard = get_object_or_404(Motherboard, pk=pk)
    return render(request, 'motherboard_detail.html', {'motherboard': motherboard})
