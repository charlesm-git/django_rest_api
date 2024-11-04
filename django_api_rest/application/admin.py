from django.contrib import admin
from application.models import Project, Issue, Comment, Contributor


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "author", "type", "date_created")


class IssueAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        'id',
        "project",
        "author",
        "status",
        "priority",
        "date_created",
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "issue", "date_created")


class ContributorAdmin(admin.ModelAdmin):
    list_display = ("contributor", "project")


admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contributor, ContributorAdmin)
