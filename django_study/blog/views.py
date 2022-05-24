from django.shortcuts import render, redirect

from .forms import BoardForm

from .models import Board, Post


# Create your views here.


def post(request):
    if request.method == 'POST':
        post = Post()
        post.text = request.POST['text']
        post.save()
        return redirect('post')
    else:
        post = Post.objects.get(id=1)
        return render(request, 'blog/post_list.html', {'post': post})


def board(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']

        board = Board(
            title=title,
            content=content,
            writer=writer,
        )

        board.save()
        return redirect('board')
    else:
        boardForm = BoardForm
        board = Board.objects.all()
        context = {
            'boardForm': boardForm,
            'board': board,
        }

        return render(request, 'blog/board.html', context)


def boardEdit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']

        board.save()
        return redirect('board')

    else:
        boardForm = BoardForm
        return render(request, 'blog/update.html', {'boardForm': boardForm})


def boardDelete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('board')
