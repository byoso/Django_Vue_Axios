from django.shortcuts import render, get_object_or_404
from .models import Poulet
import json
from django.http import JsonResponse

def jsonify(a_query_set):
    """Convert a queryset into a json format"""
    attrs = []
    list_json = []
    if len(a_query_set) > 0:
        for i in a_query_set[0]._meta.fields:
            attrs.append(i.name)
        for i in a_query_set:
            json_object = {}
            for attr in attrs:
                json_object[attr] = str(getattr(i, attr))
            list_json.append(json_object)
        return list_json
    else:
        return []


def index(request):
    print(request.body)
    message = ""
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        if data['nom'] != "" and float(data['poids']) >= 0 :
            try:
                poulet = Poulet(nom=data['nom'], poids=data['poids'])
                poulet.save()
            except:
                print("validation à refaire")#debug
                response = f"Validation imposible : {poulet.nom} existe déjà"
                return JsonResponse({"err":response}, status=400)
            else:
                response = f"Bienvenue {poulet.nom} !"
                poulets = Poulet.objects.all()
                poulets_json = jsonify(poulets)
                return JsonResponse({"msg":response, 'poulets':poulets_json}, status=201)
        else:
            response = "Il faut un nom, et un poids positif"
            return JsonResponse({"err":response}, status=400)

    if request.method == "DELETE":
        data = json.loads(request.body)
        poulet = get_object_or_404(Poulet, id=data['id'])
        print(f'DELETE Method, tuer : {poulet.nom}')#debug
        nom = poulet.nom
        poulet.delete()
        poulets = Poulet.objects.all()
        # print(jsonify(poulets))#debug
        poulets_json = jsonify(poulets)
        response = f"On vient de tuer {nom}"
        return JsonResponse({"msg":response, 'poulets':poulets_json}, status=201)

    poulets = Poulet.objects.all()
    poulets_json = jsonify(poulets)
    context = {}
    context['poulets'] = poulets_json
    return render(request, 'vue/index.html', context)

