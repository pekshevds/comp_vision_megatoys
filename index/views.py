from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseBadRequest
from django.views import View
from server.forms import UploadFileForm
from index.services import save_file, get_faces


class LoadFileView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "index/index.html")

    def post(self, request: HttpRequest) -> JsonResponse:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image_name = save_file(form.cleaned_data.get("file"))
            return JsonResponse({"result": get_faces(image_name)})
        return HttpResponseBadRequest("Ошибка загрузки файла")
