# 장고 폼을 정리하는 내용
from .forms import ArticleForm  # Article Model을 바탕으로 만들어진 Form
# 게시글을 생성하기 위한 흐름에 집중해서 이해할 필요 있음
def create(request):
    # 1. 게시글을 작성할 수 있는 페이지를 보여줘야 할 필요가 있음.
    #   (게시글 요청은 GET method로 요청된다!!!)
    # 1.1 ModelForm을 이용해서 빈 인스턴스를 생성한다.
    form = ArticleForm()
    # 1.2 빈 인스턴스를 딕셔너리 형태로 담아서 html로 랜더링해준다.
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)


def new(request):
    # 2. 게시글을 DB에 저장하기 위한 단계
    # DB에 저장되는 요청은 POST요청이다.
    # 2.1 ModelFrom에 전달 받은 데이터를 넣어서 인스턴스를 생성한다.
    form = ArticleForm(request.POST)
    # 2. 인스턴스에 담긴 데이터가 저장해도 되는 데이터인지 검수한다(유효성 검사)
    if form.is_valid(): # 유효성 검사를 통과하면 True, 실패하면 False
        # 2.2.1 유효성 검사를 통과했다면
        article = form.save()  # 필요하다면 저장되는 데이터를 인스턴스로 받을 수 있다.
        # 2.3 저장이 완료 되었으면 디테일 페이지로 이동한다.
        return redirect('articles:detail', article.pk)
    # 2.2.2 유효성 검사를 통과하지 못했다면 (에러 메세지를 보여줘야 한다.)
    # 유효성 검사를 통과하지 못하면 error 메세지가 form에 알아서 담긴다.
    # 에러 메세지가 담긴 form을 딕셔너리로 담아서 렌더링 해준다.
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)


 def 통합본(request):

    if request.method == 'POST':
        # POST
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # GET
        form = ArticleForm()

    # GET, POST요청의 공통된 내용
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)
