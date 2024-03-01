from django.db import models
import sys
from django.core.management import setup_environ


if __name__ == "__main__":
    
    settings_module = "gdsblog.settings"  
    setup_environ(settings_module)
    
    



class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    content = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()


def create_posts():
    
    post1 = Post.objects.create(
        title="First Post", category="Tech", content="This is the content of the first post."
    )
    post2 = Post.objects.create(
        title="Second Post", category="Travel", content="This is the content of the second post."
    )
    post3 = Post.objects.create(
        title="Third Post", category="News", content="This is the content of the third post."
    )
    print("Created 3 posts successfully!")


def query_posts_by_category(category):
    posts = Post.objects.filter(category=category)
    if posts:
        print(f"Posts in category '{category}':")
        for post in posts:
            print(f"- {post.title} ({post.category})")
    else:
        print(f"No posts found in category '{category}'.")


def update_post_content(post_id, new_content):
    try:
        post = Post.objects.get(pk=post_id)
        post.content = new_content
        post.save()
        print(f"Post '{post.title}' content updated successfully!")
    except Post.DoesNotExist:
        print(f"Post with ID {post_id} not found.")


def delete_post(post_id):
    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
        print(f"Post '{post.title}' deleted successfully!")
    except Post.DoesNotExist:
        print(f"Post with ID {post_id} not found.")


def create_comments():
    
    post1 = Post.objects.get(pk=1)  
    post2 = Post.objects.get(pk=2)  
    post3 = Post.objects.get(pk=3)  
    comment1 = Comment.objects.create(post=post1, content="This is the first comment.")
    comment2 = Comment.objects.create(post=post2, content="This is the second comment.")
    comment3 = Comment.objects.create(post=post3, content="This is the third comment.")
    print("Created 3 comments successfully!")


def query_comments_by_post(post_id):
    comments = Comment.objects.filter(post=post_id)
    if comments:
        print(f"Comments for post ID {post_id}:")
        for comment in comments:
            print(f"- {comment.content}")
    else:
        print(f"No comments found for post ID {post_id}.")


def update_comment_content(comment_id, new_content):
    try:
        comment = Comment.objects.get(pk=comment_id)
        comment.content = new_content
        comment.save()
        print(f"Comment ID {comment_id} content updated successfully!")
    except Comment.DoesNotExist:
        print(f"Comment with ID {comment_id} not found.")


def delete_comment(comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
        print(f"Comment ID {comment_id} deleted successfully!")
    except Comment.DoesNotExist:
        print(f"Comment with ID {comment_id} not found.")



create_posts()
query_posts_by_category("Tech")

update_post_content(1, "Updated content for the first post.")  

delete_post(2)  

create_comments()
query_comments_by_post(1)  


