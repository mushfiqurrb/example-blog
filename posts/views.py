from django.shortcuts import render
import requests

# POSTS VIEW ENDPOINT
##def posts(request):
##    return render(request, 'blog-listing.html')


# POST DETAILS VIEW ENDPOINT
def post_details(request,post_id):


    response = requests.get('https://jsonplaceholder.typicode.com/posts/{}'.format(post_id))

    post_details = response.json()

    return render(request, 'blog-post.html', {"post_details": post_details})

def posts(request):
    # get the list of todos
    response = requests.get('https://jsonplaceholder.typicode.com/posts/')
    # transfor the response to json objects
    posts = response.json()
    return render(request, "blog-listing.html", {"posts": posts})

def post_comments(request,post_id):

    response = requests.get('https://jsonplaceholder.typicode.com/posts/{}/comments'.format(post_id))

    post_comments = response.json()

    return render(request, 'blog-post-comments.html', {"post_comments": post_comments})