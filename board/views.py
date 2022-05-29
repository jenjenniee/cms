from django.shortcuts import render,redirect
from .models import Board
from datetime import datetime
from django.contrib.auth.models import User
from board.forms import  *

# Create your views here.
def Viewboard(request):
    vb = Board.objects.all().order_by('-pk')
    return render(request,'board/Viewboard.html',{'vb':vb})

def Writeboard(request):
    if request.method == 'POST':


        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            Board = form.save(commit=False)
            Board.user = User.objects.get(user_number=user_id)
            Board.board_title = request.POST['board_title']
            Board.board_content = request.POST['board_content']
            Board.board_date = datetime.now()
            Board.category = request.POST.get('category')
            Board.save()
            return redirect('board:Viewboard')
    else:
        form = PostForm()
    return render(request,'board/Writeboard.html',{'form':form})

# 게시판 제목클릭시 들어가는화면
def Boarddetail(request, pk):
    de = Board.objects.get(pk=pk)
    de.board_hits = de.board_hits + 1
    de.save(update_fields=['board_hits'])
    next_board = Board.objects.filter(pk__gt=pk)
    if next_board:
        next_board = next_board[0]

    prev_board = Board.objects.filter(pk__lt=pk)
    if prev_board:
        prev_board = prev_board[0]

    context = {
        'de':de,
        'next_board':next_board,
        'prev_board':prev_board
    }
    return render(request, 'board/Boarddetail.html',context)

#게시판 삭제
def Deleteboard(request,pk):
    # user_id = request.session.get('user_id')
    # if not user_id :
    #     return redirect('/login')
    db = Board.objects.get(pk=pk)
    db.delete()
    return redirect('board:Viewboard')


#게시판 수정
def Editboard(request, pk):
    eb = Board.objects.get(pk=pk)
    if request.method == "POST":
        eb.board_title = request.POST['board_title']
        eb.category = request.POST.get('category')
        eb.board_content = request.POST['board_content']
        
        if request.POST.get('clear') or request.FILES.get('file'):
            eb.board_file = request.FILES.get('file')


        eb.save()
        return redirect('board:Viewboard')
    return render(request,'board/Editboard.html',{'eb':eb})