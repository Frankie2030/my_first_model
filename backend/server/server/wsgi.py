"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import inspect

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()


# ML registry
from ml.registry import MLRegistry
from ml.classifier.random_forest import RandomForestClassifier
from ml.classifier.extra_trees import ExtraTreesClassifier

try:
    # create ML registry
    registry = MLRegistry()
    # Random Forest classifier
    rf = RandomForestClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="classifier",
                            algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="testing",
                            algorithm_version="1.0.2",
                            owner="Frankie",
                            algorithm_description="Random Forest with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier))
    
except Exception as e:
    print("Exception while loading the Random forest algorithm to the registry,", str(e))

try:
    # Extra Trees classifier
    et = ExtraTreesClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="classifier",
                            algorithm_object=et,
                            algorithm_name="extra trees",
                            algorithm_status="testing",
                            algorithm_version="1.0.2",
                            owner="Frankie",
                            algorithm_description="Extra Trees with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(ExtraTreesClassifier))
    
except Exception as e:
    print("Exception while loading the Extra Trees algorithm to the registry,", str(e))