from django.shortcuts import render

def locator_view(request):
    data = request.POST.get('center', 'waterfalls')
    if data == 'waterfalls':
        markers = [{
            'name': 'waterfall 1',
            'location': [-0.6889176, 34.7588609, 13],
        }, {
            'name': 'waterfall 2',
            'location': [-0.6546379, 34.7375175, 13],
        }, {
            'name': 'waterfall 3',
            'location': [-0.6739269, 34.7765193, 18.34],
        }]
    elif data == 'caves':
        markers = [{
            'name': 'cave 1',
            'location': [-0.6743637, 34.7753614, 18.34],
        }, {
            'name': 'cave 2',
            'location': [-0.6780949, 34.7327949, 14],
        }, {
            'name': 'cave 3',
            'location': [-0.7139235, 34.8032076, 14],
        }, {
            'name': 'cave 4',
            'location': [-0.6708163, 34.7420812, 14],
        }]
    elif data == 'hills':
        markers = [{
            'name': 'hill 1',
            'location': [-0.6546379, 34.7900458, 15],
        }, {
            'name': 'hill 2',
            'location': [-0.699619, 34.7898868, 13.85],
        }, {
            'name': 'hill 3',
            'location': [-0.6890251, 34.7851257, 15],
        }, {
            'name': 'hill 4',
            'location': [-0.6773058, 34.7715169],
        }]
    elif data == 'springs':
        markers = [{
            'name': 'spring 1',
            'location': [-0.6301669, 34.633069, 13],
        }, {
            'name': 'spring 2',
            'location': [-0.6546379, 34.7375175, 13],
        }, {
            'name': 'spring 3',
            'location': [-0.6739269, 34.7765193, 18.34],
        }, {
            'name': 'spring 3',
            'location': [-0.6452946, 34.6072171, 12.26],
        }]
    else:
        markers= []
    return render(request, 'index.html', {'markers': markers});
