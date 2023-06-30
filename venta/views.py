from django.shortcuts import render
from django.http import HttpResponse
from .models import Plataforma, Categoria, Inventario, Coleccion
from .forms import PlataformaForm, CategoriaForm, ColeccionForm
from django.contrib.auth.decorators import login_required

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    return render(request, "venta/index.html")

def nosotros(request):
    return render(request, "venta/nosotros.html")

def carrito(request):
    return render(request, "venta/carrito.html")

def contacto(request):
    return render(request, "venta/usuario/contacto.html")

def formRegistro(request):
    return render(request, "venta/usuario/formRegistro.html")

def micuenta(request):
    return render(request, "venta/usuario/micuenta.html")

def tienda(request):
    return render(request, "venta/tienda.html")


@login_required
def administrador(request):
    request.session["usuario"]="miguel"
    lista_inventario = Inventario.objects.all()
    lista_categorias = Categoria.objects.all()
    lista_plataforma = Plataforma.objects.all()
    usuario=request.session["usuario"]

    context = {"inventario":lista_inventario,"categoria":lista_categorias,"plataforma":lista_plataforma,"usu":usuario}
    return render(request, 'venta/administrador.html',context)



#Listar inventario
@login_required
def lista_inventario(request):
    lista_inventario = Inventario.objects.raw("SELECT * FROM venta_inventario")
    lista_categorias = Categoria.objects.all()
    lista_plataformas = Plataforma.objects.all()
    lista_colecciones = Coleccion.objects.all()
    context = {"inventario":lista_inventario, "plataformas": lista_plataformas, "categorias": lista_categorias, "colecciones":lista_colecciones}
    return render(request,'venta/inventario/inventario_list.html',context)

#agregar inventario
@login_required
def agregar_inventario(request):
    if request.method != "POST":
        lista_categorias = Categoria.objects.all()
        lista_plataformas = Plataforma.objects.all()
        lista_colecciones = Coleccion.objects.all()
        context={"categorias":lista_categorias, "plataformas":lista_plataformas, "colecciones": lista_colecciones}
        return render(request,'venta/inventario/inventario_add.html',context)
    else:
        #rescatamos en variables os valores del formulario (name)
        categoria = request.POST["categoria"]
        plataforma = request.POST["plataforma"]
        coleccion = request.POST["coleccion"]
        nombre_juego = request.POST["nombre_juego"]
        valor = request.POST["valor"]
        stock = request.POST["stock"]
       

        objCategoria = Categoria.objects.get(Id_categoria = categoria)
        objPlataforma = Plataforma.objects.get(Id_plataforma = plataforma)
        objColeccion = Coleccion.objects.get(Id_coleccion = coleccion)

        objInventario = Inventario.objects.create(  
            Id_categoria     = objCategoria,
            Id_plataforma    = objPlataforma,
            Id_coleccion     = objColeccion,
            nombre_juego     = nombre_juego,
            valor            = valor,
            stock            = stock,
            disponible       = "1",)
        
        objInventario.save() #insert en la base de datos
        lista_categorias = Categoria.objects.all()
        lista_plataformas = Plataforma.objects.all()
        lista_colecciones = Coleccion.objects.all()
        context = {"mensaje":"Se guardó el juego al inventario","plataforma":lista_plataformas, "categoria":lista_categorias, "coleccion": lista_colecciones}
        return render(request,'venta/inventario/inventario_add.html',context)

#Buscar Inventario (buscar objeto de inventario para modificar.)
@login_required
def buscar_inventario(request,pk):
    if pk != "":
        inventario = Inventario.objects.get(Id_juego=pk)
        lista_categoria = Categoria.objects.all()
        lista_plataforma = Plataforma.objects.all()
        lista_colecciones = Coleccion.objects.all()
        context={"inventario":inventario, "categorias":lista_categoria, "plataformas":lista_plataforma, "colecciones":lista_colecciones}
        if Inventario:
            return render(request,'venta/inventario/inventario_edit.html',context)
        else:
            context = {"mensaje":"El juego no existe"}
            return render(request,'venta/inventario/inventario_list.html',context)


#eliminar inventario
@login_required
def borrar_inventario(request,pk):
    
    try:
        inventario = Inventario.objects.get(Id_juego=pk)

        inventario.delete() #delete en la BD
        mensaje = "Se eliminó el juego"
        lista_inventario = Inventario.objects.all()
        context={"inventario":lista_inventario, "mensaje":mensaje}
        return render(request,'venta/inventario/inventario_list.html',context)
    except:
        mensaje = "NO se eliminó el juego"
        lista_inventario = Inventario.objects.all()
        context={"inventario":lista_inventario, "mensaje":mensaje}
        return render(request,'venta/inventario/inventario_list.html',context)


#modificar inventario
@login_required
def actualizar_inventario(request):
    if request.method == "POST":
        #rescatamos en variables los valores del formulario (name)
        Id_juego = request.POST["Id_juego"]
        categoria = request.POST["categoria"]
        plataforma = request.POST["plataforma"]
        coleccion = request.POST["coleccion"]
        nombre_juego = request.POST["nombre_juego"]
        valor = request.POST["valor"]
        stock = request.POST["stock"]

        objCategoria = Categoria.objects.get(Id_categoria = categoria)
        objPlataforma = Plataforma.objects.get(Id_plataforma = plataforma)
        objColeccion = Coleccion.objects.get(Id_coleccion = coleccion)

        #crea alumno (izp:nombre del campo de la BD, derecho:variable local)
        objInventario = Inventario()
        objInventario.Id_juego      = Id_juego
        objInventario.Id_categoria  = objCategoria
        objInventario.Id_plataforma = objPlataforma
        objInventario.Id_coleccion  = objColeccion
        objInventario.nombre_juego  = nombre_juego
        objInventario.valor         = valor
        objInventario.stock         = stock
        objInventario.activo        = 1
         
        objInventario.save() #update en la base de datos
        lista_categoria = Categoria.objects.all()
        lista_plataforma = Plataforma.objects.all()
        lista_colecciones = Coleccion.objects.all()
        context = {"mensaje":"Se guardó el juego al inventario","plataforma":lista_plataforma, "categoria":lista_categoria, "coleccion":lista_colecciones}
        return render(request,'venta/inventario/inventario_edit.html',context)
    else:
        lista_Inventario = Inventario.objects.all()
        context = {"inventario":lista_Inventario}
        return render(request,'venta/inventario/inventario_list.html',context)




#Listar plataformas
@login_required  
def mostrar_plataformas(request):
    lista_plataformas = Plataforma.objects.all()
    context={"plataformas":lista_plataformas}
    return render(request,'venta/plataforma/plataforma_list.html',context)

#agregar plataformas
@login_required  
def agregar_plataformas(request):
    if request.method == "POST":
        form = PlataformaForm(request.POST)
        if form.is_valid:
            form.save() #insert
            form = PlataformaForm()
            context = {"mensaje": "Se grabo la plataforma", "form": form}
            return render(request,'venta/plataforma/plataforma_add.html',context)
            
    else:
        form = PlataformaForm()
        context = {"form": form}
        return render(request,'venta/plataforma/plataforma_add.html',context)

#eliminar plataformas
@login_required  
def borrar_plataformas(request,pk):
    errores = []
    lista_plataformas = Plataforma.objects.all()
    try:
        plataforma = Plataforma.objects.get(Id_plataforma=pk)
        #Aqui hay que llamar a otra funcion de python que sea una confirmación de lo que borramos.
        if plataforma:
            plataforma.delete() #Delete en la BD
            context={"mensaje": "Plataforma eliminada", "plataformas": lista_plataformas, "errores": errores,}
            return render(request,'venta/plataforma/plataforma_list.html',context)
    except:
        lista_plataformas = Plataforma.objects.all()
        context={"mensaje":"No existe la plataforma", "plataformas": lista_plataformas, "errores": errores,}
        return render(request,'venta/plataforma/plataforma_list.html',context)

#modificar plataformas
@login_required  
def actualizar_plataforma(request, pk):
    try:
        plataforma = Plataforma.objects.get(Id_plataforma=pk)
        context={}
        if plataforma:
            print("Edit encontro la plataforma")
            if request.method == "POST":
                print("edit,es un post")
                form = PlataformaForm(request.POST,instance=plataforma)
                form.save()
                context = {"mensaje": "Se actualizó la plataforma", "form":form, "plataforma":plataforma}
                return render(request, 'venta/plataforma/plataforma_edit.html', context)
            else:
                form = PlataformaForm(instance=plataforma)
                mensaje = ""
                context = {"mensaje": mensaje, "form":form, "plataforma":plataforma}
                return render(request, 'venta/plataforma/plataforma_edit.html', context)
    except:
        mensaje = "No existe la plataforma"
        lista_plataformas = Plataforma.objects.all()
        context = {"mensaje": mensaje, "form":form, "plataforma":lista_plataformas}
        return render(request, 'venta/plataforma/plataforma_list.html', context)


#listar categorias
@login_required  
def mostrar_categorias(request):
    lista_categorias = Categoria.objects.all()
    context={"categorias":lista_categorias}
    return render(request,'venta/categoria/categoria_list.html',context)

#agregar categorias
@login_required  
def agregar_categorias(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid:
            form.save() #insert
            form = CategoriaForm()
            context = {"mensaje": "Se grabo la categoria", "form": form}
            return render(request,'venta/categoria/categoria_add.html',context)
            
    else:
        form = CategoriaForm()
        context = {"form": form}
        return render(request,'venta/categoria/categoria_add.html',context)

#eliminar categorias
@login_required  
def borrar_categorias(request,pk):
    errores = []
    lista_categorias = Categoria.objects.all()
    try:
        categoria = Categoria.objects.get(Id_categoria=pk)
        #Aqui hay que llamar a otra funcion de python que sea una confirmación de lo que borramos.
        if categoria:
            categoria.delete() #Delete en la BD
            context={"mensaje": "Categoria eliminada", "categorias": lista_categorias, "errores": errores,}
            return render(request,'venta/categoria/categoria_list.html',context)
    except:
        lista_categorias = Categoria.objects.all()
        context={"mensaje":"No existe la categoria", "categorias": lista_categorias, "errores": errores,}
        return render(request,'venta/categoria/categoria_list.html',context)

#modificar categorias
@login_required  
def actualizar_categoria(request, pk):
    try:
        categoria = Categoria.objects.get(Id_categoria=pk)
        context={}
        if categoria:
            print("Edit encontro la categoria")
            if request.method == "POST":
                print("edit,es un post")
                form = CategoriaForm(request.POST,instance=categoria)
                form.save()
                context = {"mensaje": "Se actualizó la categoria", "form":form, "categoria":categoria}
                return render(request,'venta/categoria/categoria_edit.html',context)
            else:
                form = CategoriaForm(instance=categoria)
                mensaje = ""
                context = {"mensaje": mensaje, "form":form, "categoria":categoria}
                return render(request, 'venta/categoria/categoria_edit.html', context)
    except:
        mensaje = "No existe la categoria"
        lista_categorias = Categoria.objects.all()
        context = {"mensaje": mensaje, "form":form, "categoria":lista_categorias}
        return render(request, 'venta/categoria/categoria_list.html', context)



#listar colecciones
@login_required
def mostrar_colecciones(request):
    lista_colecciones = Coleccion.objects.all()
    context={"colecciones":lista_colecciones}
    return render(request,'venta/colecciones/colecciones_list.html',context)

#agregar colecciones
@login_required
def agregar_colecciones(request):
    if request.method == "POST":
        form = ColeccionForm(request.POST)
        if form.is_valid:
            form.save() #insert
            form = ColeccionForm()
            context = {"mensaje": "Se grabo la coleccion", "form": form}
            return render(request,'venta/colecciones/colecciones_add.html',context)
            
    else:
        form = ColeccionForm()
        context = {"form": form}
        return render(request,'venta/colecciones/colecciones_add.html',context)

#eliminar colecciones
@login_required
def borrar_colecciones(request,pk):
    errores = []
    lista_colecciones = Coleccion.objects.all()
    try:
        coleccion = Coleccion.objects.get(Id_coleccion=pk)
        #Aqui hay que llamar a otra funcion de python que sea una confirmación de lo que borramos.
        if coleccion:
            coleccion.delete() #Delete en la BD
            context={"mensaje": "Coleccion eliminada", "colecciones": lista_colecciones, "errores": errores,}
            return render(request,'venta/colecciones/colecciones_list.html',context)
    except:
        lista_colecciones = Coleccion.objects.all()
        context={"mensaje":"No existe la coleccion", "colecciones": lista_colecciones, "errores": errores,}
        return render(request,'venta/colecciones/colecciones_list.html',context)

#modificar colecciones
@login_required
def actualizar_colecciones(request, pk):
    try:
        coleccion = Coleccion.objects.get(Id_coleccion=pk)
        context={}
        if coleccion:
            print("Edit encontro la coleccion")
            if request.method == "POST":
                print("edit,es un post")
                form = ColeccionForm(request.POST,instance=coleccion)
                form.save()
                context = {"mensaje": "Se actualizó la coleccion", "form":form, "coleccion":coleccion}
                return render(request,'venta/colecciones/colecciones_edit.html',context)
            else:
                form = ColeccionForm(instance=coleccion)
                mensaje = ""
                context = {"mensaje": mensaje, "form":form, "coleccion":coleccion}
                return render(request, 'venta/colecciones/colecciones_edit.html', context)
    except:
        mensaje = "No existe la coleccion"
        lista_colecciones = Coleccion.objects.all()
        context = {"mensaje": mensaje, "form":form, "coleccion":lista_colecciones}
        return render(request, 'venta/colecciones/colecciones_list.html', context)


#Filtro de busqueda para nombre de juego en inventario.

#Filtro de busqueda para coleccion en inventario.











# #FUNCION LICENCIA ALEATORIA, realiza una funcion aleatoria que utiliza después la boleta
# def generar_codigo_licencia():
#     caracteres_permitidos = string.ascii_uppercase + string.ascii_lowercase + string.digits
#     longitud_codigo = 10
#     codigo_licencia = ''.join(random.choice(caracteres_permitidos) for _ in range(longitud_codigo))
#     return codigo_licencia

#     # Obtener el nombre y valor del juego desde el Inventario hacia Boleta
# def save(self, *args, **kwargs):
#     inventario = Inventario.objects.get(Id_juego=self.Id_inventario_id)
#     self.nombre_juego = inventario.nombre_juego
#     self.valor = inventario.valor
#     super().save(*args, **kwargs)   
    
#     # Obtener el email desde el Usuario hacia Boleta     
    
# def save(self, *args, **kwargs):   
#     usuario = Usuarios.objects.get(id_usuario=self.Id_usuario_id)
#     self.email = usuario.email
#     super().save(*args, **kwargs)
