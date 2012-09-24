from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse

from permissions.models import Permission

from .models import BootstrapSetup
from .classes import Cleanup, BootstrapModel
from .permissions import (PERMISSION_BOOTSTRAP_VIEW, PERMISSION_BOOTSTRAP_CREATE,
    PERMISSION_BOOTSTRAP_EDIT, PERMISSION_BOOTSTRAP_DELETE,
    PERMISSION_BOOTSTRAP_EXECUTE, PERMISSION_NUKE_DATABASE, PERMISSION_BOOTSTRAP_DUMP)
from .icons import icon_bootstrap_setup_execute, icon_nuke_database, icon_bootstrap_setup_delete
from .forms import BootstrapSetupForm, BootstrapSetupForm_view, BootstrapSetupForm_dump


def bootstrap_setup_list(request):
    Permission.objects.check_permissions(request.user, [PERMISSION_BOOTSTRAP_VIEW])

    context = {
        'object_list': BootstrapSetup.objects.all(),
        'title': _(u'bootstrap setups'),
        'hide_link': True,
        'extra_columns': [
            {'name': _(u'description'), 'attribute': 'description'},
            {'name': _(u'type'), 'attribute': 'get_type_display'},
        ],
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))


def bootstrap_setup_create(request):
    Permission.objects.check_permissions(request.user, [PERMISSION_BOOTSTRAP_CREATE])

    if request.method == 'POST':
        form = BootstrapSetupForm(request.POST)
        if form.is_valid():
            bootstrap = form.save()
            messages.success(request, _(u'Bootstrap created successfully'))
            return HttpResponseRedirect(reverse('bootstrap_setup_list'))
        else:
            messages.error(request, _(u'Error creating bootstrap setup.'))
    else:
        form = BootstrapSetupForm()

    return render_to_response('generic_form.html', {
        'title': _(u'create bootstrap'),
        'form': form,
    },
    context_instance=RequestContext(request))


def bootstrap_setup_edit(request, bootstrap_setup_pk):
    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))

    bootstrap = get_object_or_404(BootstrapSetup, pk=bootstrap_setup_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_BOOTSTRAP_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_BOOTSTRAP_EDIT, request.user, bootstrap)

    if request.method == 'POST':
        form = BootstrapSetupForm(instance=bootstrap, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Bootstrap setup edited successfully'))
            return HttpResponseRedirect(previous)
        else:
            messages.error(request, _(u'Error editing bootstrap setup.'))
    else:
        form = BootstrapSetupForm(instance=bootstrap)

    return render_to_response('generic_form.html', {
        'title': _(u'edit bootstrap setup: %s') % bootstrap,
        'form': form,
        'object': bootstrap,
        'previous': previous,
        'object_name': _(u'bootstrap setup'),
    },
    context_instance=RequestContext(request))


def bootstrap_setup_delete(request, bootstrap_setup_pk):
    bootstrap = get_object_or_404(BootstrapSetup, pk=bootstrap_setup_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_BOOTSTRAP_DELETE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_BOOTSTRAP_DELETE, request.user, bootstrap)

    post_action_redirect = reverse('bootstrap_setup_list')

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            bootstrap.delete()
            messages.success(request, _(u'Bootstrap setup: %s deleted successfully.') % bootstrap)
        except Exception, e:
            messages.error(request, _(u'Bootstrap setup: %(bootstrap)s delete error: %(error)s') % {
                'bootstrap': bootstrap, 'error': e})

        return HttpResponseRedirect(reverse('bootstrap_setup_list'))

    context = {
        'object_name': _(u'bootstrap setup'),
        'delete_view': True,
        'previous': previous,
        'next': next,
        'object': bootstrap,
        'title': _(u'Are you sure you with to delete the bootstrap setup: %s?') % bootstrap,
        'form_icon': icon_bootstrap_setup_delete,
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


def bootstrap_setup_view(request, bootstrap_setup_pk):
    bootstrap = get_object_or_404(BootstrapSetup, pk=bootstrap_setup_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_BOOTSTRAP_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_BOOTSTRAP_VIEW, request.user, bootstrap)

    form = BootstrapSetupForm_view(instance=bootstrap)
    context = {
        'form': form,
        'object': bootstrap,
        'object_name': _(u'bootstrap setup'),
    }

    return render_to_response('generic_detail.html', context,
        context_instance=RequestContext(request))


def bootstrap_setup_execute(request, bootstrap_setup_pk):
    Permission.objects.check_permissions(request.user, [PERMISSION_BOOTSTRAP_EXECUTE])
    bootstrap_setup = get_object_or_404(BootstrapSetup, pk=bootstrap_setup_pk)

    post_action_redirect = reverse('bootstrap_setup_list')

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            bootstrap_setup.execute()
        except Exception, exc:
            messages.error(request, _(u'Error executing bootstrap setup; %s') % exc)
        else:
            messages.success(request, _(u'Bootstrap setup "%s" executed successfully.') % bootstrap_setup)
            return HttpResponseRedirect(next)

    context = {
        'object_name': _(u'bootstrap setup'),
        'delete_view': False,
        'previous': previous,
        'next': next,
        'form_icon': icon_bootstrap_setup_execute,
        'object': bootstrap_setup,
    }

    context['title'] = _(u'Are you sure you wish to execute the database bootstrap named: %s?') % bootstrap_setup

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


def bootstrap_setup_dump(request):
    Permission.objects.check_permissions(request.user, [PERMISSION_BOOTSTRAP_DUMP])

    if request.method == 'POST':
        form = BootstrapSetupForm_dump(request.POST)
        if form.is_valid():
            bootstrap = form.save(commit=False)
            try:
                bootstrap.fixture = BootstrapSetup.objects.dump(format=bootstrap.type)
            except Exception as exception:
                messages.error(request, _(u'Error dumping bootstrap setup; %s') % exception)
            else:
                bootstrap.save()
                messages.success(request, _(u'Bootstrap created successfully.'))
                return HttpResponseRedirect(reverse('bootstrap_setup_list'))
    else:
        form = BootstrapSetupForm_dump()

    return render_to_response('generic_form.html', {
        'title': _(u'dump current setup into a bootstrap setup'),
        'form': form,
    },
    context_instance=RequestContext(request))


def erase_database_view(request):
    Permission.objects.check_permissions(request.user, [PERMISSION_NUKE_DATABASE])

    post_action_redirect = None

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            Cleanup.execute_all()
        except Exception, exc:
            messages.error(request, _(u'Error erasing database; %s') % exc)
        else:
            messages.success(request, _(u'Database erased successfully.'))
            return HttpResponseRedirect(next)

    context = {
        'delete_view': False,
        'previous': previous,
        'next': next,
        'form_icon': icon_nuke_database,
    }

    context['title'] = _(u'Are you sure you wish to erase the entire database and document storage?')
    context['message'] = _(u'All documents, sources, metadata, metadata types, set, tags, indexes and logs will be lost irreversibly!')

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))
