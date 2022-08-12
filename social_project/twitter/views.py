from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Profile, Post, Relationship, Hijos, Consultas
from .forms import UserRegisterForm, PostForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
	posts = Post.objects.filter(user=request.user)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('home')
	else:
		form = PostForm()

	context = {'posts':posts, 'form' : form }
	return render(request, 'twitter/newsfeed.html', context)

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = UserRegisterForm()

	context = {'form' : form}
	return render(request, 'twitter/register.html', context)


def delete(request, post_id):
	post = Post.objects.get(id=post_id)
	post.delete()
	return redirect('home')


def profile(request, username):
	user = User.objects.get(username=username)
	posts = user.posts.all()
	context = {'user':user, 'posts':posts}
	return render(request, 'twitter/profile.html', context)

@login_required
def editar(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			return redirect('home')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm()

	context = {'u_form' : u_form, 'p_form' : p_form}
	return render(request, 'twitter/editar.html', context)

@login_required
def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	return redirect('home')

@login_required
def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.get(from_user=current_user.id, to_user=to_user_id)
	rel.delete()
	return redirect('home')

@login_required
def hijos(request):
    hijos = Hijos.objects.filter(user=request.user)
    context = {'hijos':hijos}
    return render(request, 'twitter/hijos.html', context)

def consultas(request):
    consultas = Consultas.objects.all()
    context={'consultas':consultas}
    return render(request, 'twitter/consultas.html', context)

def consulta(request, id):
    consultas = Consultas.objects.filter(nombre_id = id)
    context={'consultas':consultas}
    return render(request, 'twitter/consulta.html', context)

def vacunacion(request):
    return render(request, 'twitter/vacunacion.html')

def interes(request):
    return render(request, 'twitter/interes.html')

def brotes(request):
    return render(request, 'twitter/brotes.html')



    
    