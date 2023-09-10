from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Tupperware',
        'amount': 2,
        'description' : 'Tupperware membawa Anda solusi penyimpanan terbaik yang \
        telah dipercaya oleh jutaan orang di seluruh dunia. Produk-produk Tupperware \
        tidak hanya tentang wadah plastik biasa; mereka adalah investasi dalam kualitas hidup Anda. \
        Kami menghadirkan produk berkualitas tinggi yang dirancang khusus untuk menjaga makanan tetap segar, \
        bebas dari bau atau rasa plastik, dan dengan penutup yang kedap udara.',
        'rating': '5/10',
        'reviews' : 'baik dan pengiriman cepat'
    }

    return render(request, "main.html", context)