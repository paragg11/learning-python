23 JUNE 2022

## FIRST HALF

- 🚧 CSCI Lecture 8. 
- 🚧 Reading more on Using generic class-based views
```
Using the mixin classes we've rewritten the views to use slightly less code than before, 
but we can go one step further. REST framework provides a set of already mixed-in generic 
views that we can use to trim down our views.py module even more.

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
```

## VIDEOS

- 🚫 No videos

## ASSIGNMENT

- 🚧 [Passbook](https://github.com/sp18-interns/django-passbook)

## DOUBTS

- No doubt for now 

## LINKS

- [Tutorial 3: Class-based Views](https://www.django-rest-framework.org/tutorial/3-class-based-views/)

## SECOND HALF

- ✅ [Hackerrank solving one problem.]
- 🚧 Understanding concept of Authentication & Permissions

## VIDEOS

- 🚫 No videos

## ASSIGNMENT

- [Passbook](https://github.com/sp18-interns/django-passbook)

## DOUBTS

- For know just understood basic and session authentication.

## LINKS

- [Tutorial 4: Authentication & Permissions](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/)

