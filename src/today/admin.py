from django.contrib import admin

from .models import Article, Author, Book, Publication, Article2
from .models import Person, Group, Membership

class ArticleAdmin(admin.ModelAdmin):
	class Meta:
		model = Article
	fields = ("headline", "pub_date", "content", "reporter")

class AuthorAdmin(admin.ModelAdmin):
	class Meta:
		model = Author
	

class PublicationInline(admin.TabularInline):
	model = Publication
		

class Article2Inline(admin.TabularInline):
	model = Article2
		



class Article2Admin(admin.ModelAdmin):
	inlines=[PublicationInline,]
	class Meta:
		model = Article2
	

	

class PublicationAdmin(admin.ModelAdmin):
	inlines=[Article2Inline,]
	class Meta:
		model = Publication
	

	

	



admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publication)
admin.site.register(Article2)


class MembershipInline(admin.TabularInline):
	model = Membership

class GroupAdmin(admin.ModelAdmin):
	class Meta:
		model = Group
	inlines = [MembershipInline,]

class PersonAdmin(admin.ModelAdmin):
	class Meta:
		model = Person
	inlines = [MembershipInline,]



admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Membership)


