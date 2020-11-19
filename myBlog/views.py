import markdown
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category,Link,Tui,Tag,Banner
# 分页插件包
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def index(request):
    allcategory = Category.objects.all()
    # 查询banner
    banner = Banner.objects.filter(is_active=True)[0:4]
    # 首页推荐
    tui = Article.objects.all().filter(tui_id = 1)[0:3]
    # 首页最新文章推荐
    allarticle = Article.objects.all().order_by('-id')[0:10]
    # 热门
    hot = Article.objects.all().order_by('views')[:10]
    # 热门推荐
    remen = Article.objects.all().filter(tui_id = 2)[0:4]

    # 标签
    tags = Tag.objects.all()
    # 友情链接
    link = Link.objects.all()
    context = {
        'allcategory': allcategory,
        'banner': banner,
        'tui': tui,
        'allarticle': allarticle,
        'hot': hot,
        'remen': remen,
        'tags' : tags,
        'link' : link
    }
    return render(request,'index.html',context)

def list(request,lid):

    list = Article.objects.all().filter(category_id = lid) # 获取通过url传过来的lid，然后筛选出文章
    cname = Category.objects.all().get(id = lid) #获取当前文章的栏目名
    remen = Article.objects.all().filter(tui_id = 2)[:6] # 获取热门推荐
    allcategory = Category.objects.all() # 导航所有分类
    tags = Tag.objects.all() # 获取所有文章标签

    # 获取页数
    page = request.GET.get('page')#在URL中获取当前页面数
    paginator = Paginator(list,5)#对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        list = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容


    #   locals()的作用是返回一个包含当前作用域里面的所有变量和它们的值的字典。
    #
    #
    return render(request,'list.html',locals())

def show(request,sid):
    show = Article.objects.all().get(id = sid)
    # show.body = markdown.markdown(show.body,extensions=[
    #     'markdown.extensions.extra',
    #     'markdown.extensions.codehilite',
    #     'markdown.extensions.toc'
    # ])


    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    remen = Article.objects.all().filter(tui_id = 2)[: 6]
    hot = Article.objects.all().order_by('?')[:10]
    previous_blog = Article.objects.filter(create_time__gt=show.create_time,category=show.category.id).first()
    netx_blog = Article.objects.filter(create_time__lt=show.create_time,category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    show.body = markdown.markdown(show.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
    return render(request,'show.html',locals())

def tag(request,tag):

    list = Article.objects.filter(tag__name=tag)  # 通过文章标签进行查询文章
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tname = Tag.objects.get(name=tag)  # 获取当前搜索的标签名
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())

def search(request):
    ss = request.GET.get('search')  # 获取搜索的关键词
    list = Article.objects.filter(title__icontains=ss)  # 获取到搜索关键词通过标题进行匹配
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'search.html', locals())

# 关于我们
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html',locals())












