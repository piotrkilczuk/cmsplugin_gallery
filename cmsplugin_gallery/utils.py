from django.conf import settings
import glob
import os 

TEMPLATES = tuple()

def autodiscover_templates():
    '''Autodiscovers cmsplugin_gallery templates the way 
    'django.template.loaders.filesystem.Loader' and
    'django.template.loaders.app_directories.Loader' work.
    '''
    # obviously, cache for better performance
    global TEMPLATES
    if TEMPLATES:
        return TEMPLATES
    
    templates = [
        ('cmsplugin_gallery/gallery.html', 'gallery.html'),
    ]
    
    dirs_to_scan = []
    if 'django.template.loaders.app_directories.Loader' in settings.TEMPLATE_LOADERS:
        for app in settings.INSTALLED_APPS:
            _ = __import__(app)
            dir = os.path.dirname(_.__file__)
            if not dir in dirs_to_scan:
                dirs_to_scan.append(dir)
    if 'django.template.loaders.filesystem.Loader' in settings.TEMPLATE_LOADERS:
        for dir in settings.TEMPLATE_DIRS:
            if not dir in dirs_to_scan:
                dirs_to_scan.append(dir)
    
    for dir in dirs_to_scan:
        found = glob.glob(os.path.join(dir, 'templates/cmsplugin_gallery/*.html'))
        for file in found:
            dir, file = os.path.split(file)
            key, value = os.path.join(dir.split('/')[-1], file), file 
            f = False
            for _, template in templates:
                if template == file:
                    f = True
            if not f:
                templates.append((key, value,))
            #print os.path.basename(file)
    
    TEMPLATES = sorted(templates, key=lambda template: template[1]) 
    return TEMPLATES