from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post
from django.views.generic.edit import FormView
from comment.forms import CommentForm
from django.contrib import messages



# Create your views here.
def post_list_view(request):
	list_objects = Post.published.all()
	paginator = Paginator(list_objects,3)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request,'blog/post/blog.html',{'posts': posts,})


def post_detail_view(request,year,month,day,post):
	post =get_object_or_404(Post, slug = post, status = 'published',publish__year = year,publish__month = month, publish__day = day)
	comments = post.comments.filter(active=True)
	new_comment =None
	#Comment posted
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			# create comment object but dont save to database yet
			new_comment = comment_form.save(commit=False)
			#Assign the current post to the comment
			new_comment.post = post
			# Save the comment to the database
			new_comment.save()
			# return redirect('blog:post_detail_view')

	else:
		comment_form = CommentForm()

	return render(request,'blog/post/bloger.html',{'post':post, 'comments':comments, 'comment_form' : comment_form ,'new_comment':new_comment})

def edit (post):
	pass

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:post_list_view')

class PostSite(FormView):
    template_name = 'create.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list_view')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
