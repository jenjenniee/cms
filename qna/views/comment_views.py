# from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView, CreateView, UpdateView
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.utils.text import slugify
# from django.shortcuts import get_object_or_404
# from qna.models import  Comment
# from django.core.exceptions import PermissionDenied
# from qna.forms import CommentForm

# class CommentUpdate(LoginRequiredMixin, UpdateView):
#     model = Comment
#     form_class = CommentForm

#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated and request.user == self.get_object().author:
#             return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
#         else:
#             raise PermissionDenied


# def delete_comment(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     post = comment.post
#     if request.user.is_authenticated and request.user == comment.author:
#         comment.delete()
#         return redirect(post.get_absolute_url())
#     else:
#         raise PermissionDenied