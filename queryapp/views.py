from django.shortcuts import render

from .forms import RegexForm 
import re 

def homeView(request):
    if request.method == 'POST': 
        form = RegexForm(request.POST)
        if form.is_valid() :
            action = request.POST['action']
            regex = form.cleaned_data['regexInput']
            string = form.cleaned_data['stringInput']
            mapping = {
                'full': re.fullmatch,
                'first': re.search,
                'all': re.findall
            }
            matches = mapping[action](regex, string)
            if isinstance(matches, list):
                context = {'form': form, 'match': ", ".join(matches), 'after': True}
            else: 
                context = {'form': form, 'match': matches.group() if matches else None, 'after': True }
            return render(request, 'queryapp/home.html', context)
    else: 
        return render(request, 'queryapp/home.html', {'form': RegexForm(), 'after': False})
