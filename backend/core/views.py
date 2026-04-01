import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Visitor, Conversation, CannedResponse


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['visitor_count'] = Visitor.objects.count()
    ctx['visitor_online'] = Visitor.objects.filter(status='online').count()
    ctx['visitor_offline'] = Visitor.objects.filter(status='offline').count()
    ctx['visitor_away'] = Visitor.objects.filter(status='away').count()
    ctx['conversation_count'] = Conversation.objects.count()
    ctx['conversation_website'] = Conversation.objects.filter(channel='website').count()
    ctx['conversation_whatsapp'] = Conversation.objects.filter(channel='whatsapp').count()
    ctx['conversation_facebook'] = Conversation.objects.filter(channel='facebook').count()
    ctx['cannedresponse_count'] = CannedResponse.objects.count()
    ctx['recent'] = Visitor.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def visitor_list(request):
    qs = Visitor.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'visitor_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def visitor_create(request):
    if request.method == 'POST':
        obj = Visitor()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.page_url = request.POST.get('page_url', '')
        obj.country = request.POST.get('country', '')
        obj.browser = request.POST.get('browser', '')
        obj.visits = request.POST.get('visits') or 0
        obj.status = request.POST.get('status', '')
        obj.last_seen = request.POST.get('last_seen') or None
        obj.save()
        return redirect('/visitors/')
    return render(request, 'visitor_form.html', {'editing': False})


@login_required
def visitor_edit(request, pk):
    obj = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.page_url = request.POST.get('page_url', '')
        obj.country = request.POST.get('country', '')
        obj.browser = request.POST.get('browser', '')
        obj.visits = request.POST.get('visits') or 0
        obj.status = request.POST.get('status', '')
        obj.last_seen = request.POST.get('last_seen') or None
        obj.save()
        return redirect('/visitors/')
    return render(request, 'visitor_form.html', {'record': obj, 'editing': True})


@login_required
def visitor_delete(request, pk):
    obj = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/visitors/')


@login_required
def conversation_list(request):
    qs = Conversation.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(visitor_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(channel=status_filter)
    return render(request, 'conversation_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def conversation_create(request):
    if request.method == 'POST':
        obj = Conversation()
        obj.visitor_name = request.POST.get('visitor_name', '')
        obj.agent = request.POST.get('agent', '')
        obj.channel = request.POST.get('channel', '')
        obj.status = request.POST.get('status', '')
        obj.messages = request.POST.get('messages') or 0
        obj.started_at = request.POST.get('started_at') or None
        obj.rating = request.POST.get('rating') or 0
        obj.save()
        return redirect('/conversations/')
    return render(request, 'conversation_form.html', {'editing': False})


@login_required
def conversation_edit(request, pk):
    obj = get_object_or_404(Conversation, pk=pk)
    if request.method == 'POST':
        obj.visitor_name = request.POST.get('visitor_name', '')
        obj.agent = request.POST.get('agent', '')
        obj.channel = request.POST.get('channel', '')
        obj.status = request.POST.get('status', '')
        obj.messages = request.POST.get('messages') or 0
        obj.started_at = request.POST.get('started_at') or None
        obj.rating = request.POST.get('rating') or 0
        obj.save()
        return redirect('/conversations/')
    return render(request, 'conversation_form.html', {'record': obj, 'editing': True})


@login_required
def conversation_delete(request, pk):
    obj = get_object_or_404(Conversation, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/conversations/')


@login_required
def cannedresponse_list(request):
    qs = CannedResponse.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = ''
    return render(request, 'cannedresponse_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def cannedresponse_create(request):
    if request.method == 'POST':
        obj = CannedResponse()
        obj.title = request.POST.get('title', '')
        obj.category = request.POST.get('category', '')
        obj.shortcut = request.POST.get('shortcut', '')
        obj.content = request.POST.get('content', '')
        obj.usage_count = request.POST.get('usage_count') or 0
        obj.active = request.POST.get('active') == 'on'
        obj.save()
        return redirect('/cannedresponses/')
    return render(request, 'cannedresponse_form.html', {'editing': False})


@login_required
def cannedresponse_edit(request, pk):
    obj = get_object_or_404(CannedResponse, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.category = request.POST.get('category', '')
        obj.shortcut = request.POST.get('shortcut', '')
        obj.content = request.POST.get('content', '')
        obj.usage_count = request.POST.get('usage_count') or 0
        obj.active = request.POST.get('active') == 'on'
        obj.save()
        return redirect('/cannedresponses/')
    return render(request, 'cannedresponse_form.html', {'record': obj, 'editing': True})


@login_required
def cannedresponse_delete(request, pk):
    obj = get_object_or_404(CannedResponse, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/cannedresponses/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['visitor_count'] = Visitor.objects.count()
    data['conversation_count'] = Conversation.objects.count()
    data['cannedresponse_count'] = CannedResponse.objects.count()
    return JsonResponse(data)
